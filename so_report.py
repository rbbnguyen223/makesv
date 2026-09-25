# -*- coding: utf-8 -*-
# so_report.py - So sanh cac ban libApplicationMain*.so voi ban goc trong APK
#
# Cach chay (trong thu muc nay):   python so_report.py
# Ket qua: so_report.txt (gui lai cho Claude doc)
#
# Script se:
#   - Lay ban GOC tu file .apk trong thu muc (lib/*/libApplicationMain.so)
#   - Tinh SHA256, kich thuoc, thoi gian sua, loai ELF (ARM/ARM64/x86) cua moi ban
#   - Gom cac ban GIONG HET nhau thanh mot nhom
#   - Liet ke tung vung byte khac voi ban goc (offset, byte cu -> byte moi)
#   - Neu co file installed.so (keo tu LDPlayer) thi cung so sanh de biet dang chay ban nao

import hashlib
import sys
import zipfile
from datetime import datetime
from pathlib import Path

BASE = Path(__file__).resolve().parent
REPORT = BASE / "so_report.txt"
CRASH_PC = 0x7AF92C          # dia chi trong crash.txt (offset trong libApplicationMain.so)
NEAR = 0x2000                # coi la "gan diem crash" neu trong khoang nay
MAX_RANGES = 40

ELF_MACHINE = {0x03: "x86", 0x28: "ARM (armeabi-v7a)", 0x3E: "x86_64", 0xB7: "AArch64 (arm64-v8a)"}

lines = []


def out(s=""):
    print(s)
    lines.append(s)


def elf_info(data: bytes) -> str:
    if data[:4] != b"\x7fELF":
        return "KHONG PHAI ELF"
    cls = {1: "32-bit", 2: "64-bit"}.get(data[4], "?")
    machine = int.from_bytes(data[18:20], "little")
    return f"ELF {cls}, {ELF_MACHINE.get(machine, hex(machine))}"


def diff_ranges(a: bytes, b: bytes, merge_gap=8):
    n = min(len(a), len(b))
    CH = 1 << 20
    total = 0
    ranges = []
    cur = None
    for base in range(0, n, CH):
        ca = a[base:base + CH]
        cb = b[base:base + CH]
        if ca == cb:
            continue
        for j in range(len(ca)):
            if ca[j] != cb[j]:
                off = base + j
                total += 1
                if cur is not None and off - cur[1] <= merge_gap:
                    cur[1] = off
                else:
                    if cur is not None:
                        ranges.append(cur)
                    cur = [off, off]
    if cur is not None:
        ranges.append(cur)
    return total, ranges


def main():
    # ---- 1. Ban goc tu APK ----
    apks = sorted(BASE.glob("*.apk"))
    originals = {}
    if not apks:
        out("!! Khong tim thay file .apk trong thu muc, chi so sanh voi nhau.")
    else:
        apk = apks[0]
        out(f"APK: {apk.name}")
        with zipfile.ZipFile(apk) as z:
            for name in z.namelist():
                if name.startswith("lib/") and name.endswith("/libApplicationMain.so"):
                    originals[name] = z.read(name)
        for name, data in originals.items():
            out(f"  ban goc: {name}  {len(data)} B  {elf_info(data)}  sha256={hashlib.sha256(data).hexdigest()[:16]}")
    out()

    # ---- 2. Cac ung vien ----
    cands = sorted(BASE.glob("libApplicationMain*.so")) + sorted(BASE.glob("installed*.so"))
    infos = []
    for p in cands:
        data = p.read_bytes()
        st = p.stat()
        infos.append({
            "path": p,
            "data": data,
            "size": len(data),
            "mtime": datetime.fromtimestamp(st.st_mtime),
            "sha": hashlib.sha256(data).hexdigest(),
            "elf": elf_info(data),
        })
    infos.sort(key=lambda x: x["mtime"], reverse=True)

    out("=== DANH SACH (moi nhat truoc) ===")
    for i in infos:
        out(f"{i['mtime']:%Y-%m-%d %H:%M:%S}  {i['size']:>10} B  {i['sha'][:16]}  {i['elf']:<28} {i['path'].name}")
    out()

    # ---- 3. Nhom giong het ----
    groups = {}
    for i in infos:
        groups.setdefault(i["sha"], []).append(i["path"].name)
    out("=== NHOM GIONG HET NHAU (cung SHA256) ===")
    for sha, names in groups.items():
        out(f"[{sha[:16]}] " + ", ".join(names))
    out()

    # ---- 4. So sanh voi ban goc ----
    out("=== KHAC BIET SO VOI BAN GOC ===")
    done = set()
    for i in infos:
        if i["sha"] in done:
            continue
        done.add(i["sha"])
        same = groups[i["sha"]]
        # chon ban goc cung kich thuoc, neu khong co thi ban goc ARM 32-bit dau tien
        orig_name, orig = None, None
        for name, data in originals.items():
            if len(data) == i["size"]:
                orig_name, orig = name, data
                break
        if orig is None and originals:
            orig_name, orig = next(iter(originals.items()))
        out(f"--- {', '.join(same)}")
        if orig is None:
            out("    (khong co ban goc de so sanh)")
            continue
        if len(orig) != i["size"]:
            out(f"    CANH BAO: kich thuoc khac ban goc ({i['size']} vs {len(orig)}) tu {orig_name}")
        total, ranges = diff_ranges(orig, i["data"])
        if total == 0:
            out(f"    GIONG HET ban goc ({orig_name})  -> ban 'sach'")
            continue
        near = [r for r in ranges if r[0] - NEAR <= CRASH_PC <= r[1] + NEAR]
        out(f"    {total} byte khac, {len(ranges)} vung, so voi {orig_name}"
            + (f"  | {len(near)} vung GAN diem crash 0x{CRASH_PC:X}" if near else ""))
        for r in ranges[:MAX_RANGES]:
            s, e = r
            ln = min(e - s + 1, 16)
            flag = "  <== GAN DIEM CRASH" if r in near else ""
            out(f"      0x{s:08X}-0x{e:08X} ({e - s + 1} B): {orig[s:s + ln].hex(' ')} -> {i['data'][s:s + ln].hex(' ')}{flag}")
        if len(ranges) > MAX_RANGES:
            out(f"      ... con {len(ranges) - MAX_RANGES} vung nua")
    out()
    out("Luu y: offset o day la offset TRONG FILE; dia chi trong crash.txt la dia chi ao, thuong gan bang nhau nhung khong dam bao.")

    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nDa ghi bao cao: {REPORT}")


if __name__ == "__main__":
    main()
