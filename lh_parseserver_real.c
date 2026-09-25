
/* WARNING: Type propagation algorithm not settling */

undefined4 * FUN_006f6678(undefined4 *param_1,undefined4 *param_2)

{
  int iVar1;
  int *piVar2;
  int iVar3;
  int *piVar4;
  int iVar5;
  undefined4 uVar6;
  int iVar7;
  int iVar8;
  code *pcVar9;
  int iVar10;
  uint in_fpscr;
  double dVar11;
  double dVar12;
  int local_360;
  int *local_35c;
  int *local_350;
  int local_330;
  undefined4 local_314;
  undefined4 local_310;
  undefined4 local_30c;
  undefined4 local_308;
  undefined4 local_304;
  char *local_300;
  undefined4 local_2fc;
  char *local_2f8;
  undefined1 auStack_2f4 [8];
  undefined1 auStack_2ec [8];
  undefined1 local_2e4 [4];
  undefined4 local_2e0;
  int local_2dc;
  char *local_2d8;
  undefined1 auStack_2d4 [8];
  undefined1 auStack_2cc [8];
  undefined4 local_2c4;
  undefined4 local_2c0;
  undefined1 auStack_2bc [8];
  undefined4 local_2b4;
  undefined *local_2b0;
  undefined4 local_2ac;
  char *local_2a8;
  undefined4 local_2a4;
  char *local_2a0;
  undefined4 local_29c;
  char *local_298;
  undefined4 local_294;
  char *local_290;
  undefined4 local_28c;
  undefined *local_288;
  undefined4 local_284;
  undefined *local_280;
  undefined1 auStack_27c [8];
  undefined4 local_274;
  undefined *local_270;
  undefined4 local_26c;
  undefined4 local_268;
  undefined1 auStack_264 [8];
  undefined4 local_25c;
  char *local_258;
  int local_254;
  char *local_250;
  int local_24c;
  char *local_248;
  undefined4 local_244;
  char *local_240;
  undefined4 local_23c;
  char *local_238;
  undefined4 local_234;
  char *local_230;
  undefined4 local_22c;
  char *local_228;
  undefined4 local_224;
  char *local_220;
  undefined4 local_21c;
  char *local_218;
  undefined4 local_214;
  char *local_210;
  undefined1 auStack_20c [8];
  undefined1 auStack_204 [8];
  undefined1 local_1fc [4];
  undefined4 local_1f8;
  int local_1f4;
  char *local_1f0;
  undefined1 auStack_1ec [8];
  undefined1 auStack_1e4 [8];
  undefined4 local_1dc;
  undefined4 local_1d8;
  undefined1 auStack_1d4 [8];
  undefined4 local_1cc;
  undefined *local_1c8;
  undefined4 local_1c4;
  char *local_1c0;
  undefined4 local_1bc;
  char *local_1b8;
  undefined4 local_1b4;
  char *local_1b0;
  undefined4 local_1ac;
  char *local_1a8;
  undefined4 local_1a4;
  undefined *local_1a0;
  undefined4 local_19c;
  undefined *local_198;
  undefined1 auStack_194 [8];
  undefined4 local_18c;
  undefined *local_188;
  undefined4 local_184;
  undefined4 local_180;
  undefined1 auStack_17c [8];
  undefined4 local_174;
  char *local_170;
  int local_16c;
  char *local_168;
  undefined4 local_164;
  char *local_160;
  int local_15c;
  char *local_158;
  undefined4 local_154;
  char *local_150;
  undefined4 local_14c;
  char *local_148;
  undefined4 local_144;
  char *local_140;
  undefined4 local_13c;
  char *local_138;
  int local_134;
  char *local_130;
  undefined4 local_12c;
  char *local_128;
  undefined4 local_124;
  undefined4 local_120;
  undefined4 local_11c;
  char *local_118;
  undefined4 local_114;
  char *local_110;
  undefined4 local_10c;
  undefined4 local_108;
  undefined4 local_104;
  undefined4 local_100;
  undefined1 auStack_fc [4];
  int local_f8;
  int local_f4;
  undefined1 auStack_f0 [4];
  int local_ec;
  int local_e8;
  undefined4 local_e4;
  int *local_e0;
  int local_dc;
  int local_d8;
  int *local_d4;
  undefined4 local_d0;
  undefined1 auStack_cc [4];
  undefined1 auStack_c8 [4];
  int *local_c4;
  undefined1 auStack_c0 [4];
  int *local_bc;
  undefined1 auStack_b8 [4];
  undefined1 auStack_b4 [4];
  undefined1 auStack_b0 [4];
  undefined1 auStack_ac [4];
  undefined1 auStack_a8 [4];
  int *local_a4;
  int *local_a0;
  int *local_9c;
  int *local_98;
  int *local_94;
  int local_90;
  undefined4 local_8c;
  undefined1 auStack_88 [4];
  undefined1 auStack_84 [4];
  int *local_80;
  undefined1 auStack_7c [4];
  int *local_78;
  undefined1 auStack_74 [4];
  undefined1 auStack_70 [4];
  int local_6c;
  undefined1 auStack_68 [4];
  undefined1 auStack_64 [4];
  undefined1 auStack_60 [4];
  int *local_5c;
  int local_58;
  int *local_54;
  int *local_50;
  int *local_4c;
  undefined1 auStack_48 [4];
  undefined1 auStack_44 [4];
  int local_40;
  undefined1 auStack_3c [4];
  int local_38 [3];
  
  local_100 = param_2[1];
  local_104 = *param_2;
  local_38[1] = 0;
  local_10c = 0;
  local_108 = 0;
  FUN_003b3094(param_1,&local_104,&local_10c,local_38 + 1);
  local_114 = 6;
  local_110 = "notice";
  (**(code **)(*(int *)*param_1 + 0x38))(local_38,(int *)*param_1,&local_114,1);
  if (local_38[0] != 0) {
    local_11c = 6;
    local_118 = "notice";
    (**(code **)(*(int *)*param_1 + 0x38))(auStack_3c,(int *)*param_1,&local_11c,1);
    FUN_00cb5628(&local_124,auStack_3c);
    DAT_00ee2ab8 = local_120;
    DAT_00ee2ab4 = local_124;
  }
  FUN_006f0758(&local_40,0);
  local_128 = "lastServerId";
  local_330 = 0;
  local_12c = 0xc;
  (**(code **)(*(int *)*param_1 + 0x38))(auStack_44,(int *)*param_1,&local_12c,1);
  FUN_00cb5628(&local_134,auStack_44);
  DAT_00ee3a80 = local_134;
  local_138 = "servers";
  DAT_00ee3a84 = local_130;
  local_13c = 7;
  (**(code **)(*(int *)*param_1 + 0x38))(auStack_48,(int *)*param_1,&local_13c,1);
  FUN_0017237c(&local_4c,auStack_48);
LAB_006f6890:
  do {
    local_144 = 6;
    local_140 = "length";
    (**(code **)(*local_4c + 0x38))(&local_50,local_4c,&local_144,1);
    if ((local_50 == (int *)0x0) ||
       (iVar3 = (**(code **)(*local_50 + 0x14))(local_50), iVar3 != 0xff && iVar3 != 1)) {
LAB_006f691c:
      if ((DAT_00ee3a84 == (char *)0x0) ||
         ((DAT_00ee3a80 == 0 && ((DAT_00ee3a84 == "" || (*DAT_00ee3a84 == '\0')))))) {
        if (*(int *)(local_40 + 4) < 1) {
          iVar3 = 0;
        }
        else {
          iVar3 = **(int **)(local_40 + 0xc);
        }
        DAT_00ee3a80 = *(int *)(iVar3 + 4);
        DAT_00ee3a84 = *(char **)(iVar3 + 8);
      }
      local_d8 = local_40;
      FUN_00c3dc4c();
      return param_1;
    }
    dVar12 = (double)VectorSignedToFloat(local_330,(byte)(in_fpscr >> 0x16) & 3);
    if (local_50 == (int *)0x0) {
      dVar11 = 0.0;
    }
    else {
      dVar11 = (double)(**(code **)(*local_50 + 0x28))(local_50);
    }
    in_fpscr = in_fpscr & 0xfffffff | (uint)(dVar12 < dVar11) << 0x1f;
    if (!SUB41(in_fpscr >> 0x1f,0)) goto LAB_006f691c;
    (**(code **)(*local_4c + 0x70))(&local_54,local_4c,local_330);
    local_330 = local_330 + 1;
    local_14c = 8;
    local_148 = "accounts";
    (**(code **)(*local_54 + 0x38))(&local_58,local_54,&local_14c);
    if (local_58 != 0) {
      local_154 = 8;
      local_150 = "accounts";
      (**(code **)(*local_54 + 0x38))(&local_5c,local_54,&local_154,1);
      piVar2 = local_5c;
      if (local_5c == (int *)0x0) {
        piVar4 = (int *)0x0;
      }
      else {
        piVar4 = (int *)__dynamic_cast(local_5c,&DAT_00e948e8,&DAT_00dee708,0);
        if ((piVar4 == (int *)0x0) &&
           ((**(code **)(*piVar2 + 0x58))(&local_dc,piVar2), local_dc == DAT_00ee51f0)) {
          iVar3 = (**(code **)(*piVar2 + 0x6c))(piVar2);
          FUN_006f0758(&local_e0,iVar3);
          piVar4 = local_e0;
          if (0 < iVar3) {
            iVar5 = 0;
            do {
              (**(code **)(*piVar2 + 0x70))(&local_e4,piVar2,iVar5);
              *(undefined4 *)(piVar4[3] + iVar5 * 4) = local_e4;
              iVar5 = iVar5 + 1;
            } while (iVar5 != iVar3);
          }
        }
      }
      local_160 = "userName";
      local_164 = 8;
      (**(code **)(*local_54 + 0x38))(auStack_60,local_54,&local_164,1);
      FUN_00cb5628(&local_15c,auStack_60);
      if ((local_158 != (char *)0x0) &&
         ((local_15c != 0 || ((local_158 != "" && (*local_158 != '\0')))))) {
        local_170 = "userName";
        local_174 = 8;
        (**(code **)(*local_54 + 0x38))(auStack_64,local_54,&local_174,1);
        FUN_00cb5628(auStack_17c,auStack_64);
        FUN_003bca88(&local_16c,auStack_17c);
        local_15c = local_16c;
        local_158 = local_168;
      }
      local_188 = &DAT_00cc7ad0;
      local_18c = 4;
      (**(code **)(*local_54 + 0x38))(auStack_68,local_54,&local_18c,1);
      FUN_00cb5628(auStack_194,auStack_68);
      FUN_003bca88(&local_184,auStack_194);
      local_198 = &DAT_00ccb8d4;
      local_19c = 2;
      (**(code **)(*local_54 + 0x38))(auStack_70,local_54,&local_19c,1);
      FUN_00cb5628(auStack_1d4,auStack_70);
      local_1dc = local_184;
      local_1d8 = local_180;
      local_1a0 = &DAT_00cca338;
      local_1a4 = 2;
      (**(code **)(*local_54 + 0x38))(auStack_74,local_54,&local_1a4,1);
      FUN_00cb5628(auStack_1e4,auStack_74);
      local_1a8 = "health";
      local_1ac = 6;
      (**(code **)(*local_54 + 0x38))(&local_78,local_54,&local_1ac,1);
      if (local_78 == (int *)0x0) {
        local_35c = local_78;
      }
      else {
        local_35c = (int *)(**(code **)(*local_78 + 0x24))(local_78);
      }
      local_1b0 = "userId";
      local_1b4 = 6;
      (**(code **)(*local_54 + 0x38))(auStack_7c,local_54,&local_1b4,1);
      FUN_00cb5628(auStack_1ec,auStack_7c);
      local_1f4 = local_15c;
      local_1f0 = local_158;
      local_1b8 = "level";
      local_1bc = 5;
      (**(code **)(*local_54 + 0x38))(&local_80,local_54,&local_1bc,1);
      iVar3 = 1 - (int)local_80;
      if ((int *)0x1 < local_80) {
        iVar3 = 0;
      }
      local_1fc[0] = (undefined1)iVar3;
      if (iVar3 == 0) {
        if (local_80 == (int *)0x0) {
          local_1f8 = 0;
        }
        else {
          local_1f8 = (**(code **)(*local_80 + 0x24))(local_80);
        }
      }
      local_1c0 = "sessionId";
      local_1c4 = 9;
      (**(code **)(*(int *)*param_1 + 0x38))(auStack_84,(int *)*param_1,&local_1c4,1);
      FUN_00cb5628(auStack_204,auStack_84);
      local_1c8 = &DAT_00cf6894;
      local_1cc = 4;
      (**(code **)(*local_54 + 0x38))(auStack_88,local_54,&local_1cc,1);
      FUN_00cb5628(auStack_20c,auStack_88);
      FUN_0049af1c(&local_6c,auStack_1d4,&local_1dc,auStack_1e4,local_35c,auStack_1ec,&local_1f4,
                   local_1fc,auStack_204,auStack_20c);
      iVar3 = local_6c;
      local_210 = "constance";
      local_214 = 9;
      (**(code **)(*local_54 + 0x38))(&local_8c,local_54,&local_214,1);
      *(undefined4 *)(iVar3 + 0x4c) = local_8c;
      local_21c = 7;
      local_218 = "include";
      (**(code **)(*local_54 + 0x38))(&local_90,local_54,&local_21c,1);
      iVar3 = local_6c;
      if (local_90 != 0) {
        local_224 = 7;
        local_220 = "include";
        (**(code **)(*local_54 + 0x38))(&local_94,local_54,&local_224,1);
        piVar2 = local_94;
        if (local_94 == (int *)0x0) {
          iVar5 = 0;
        }
        else {
          iVar5 = __dynamic_cast(local_94,&DAT_00e948e8,&DAT_00df0758,0);
          if ((iVar5 == 0) &&
             ((**(code **)(*piVar2 + 0x58))(&local_e8,piVar2), local_e8 == DAT_00ee51f0)) {
            iVar8 = (**(code **)(*piVar2 + 0x6c))(piVar2);
            FUN_006f07b8(&local_ec,iVar8);
            iVar5 = local_ec;
            if (0 < iVar8) {
              iVar10 = 0;
              do {
                (**(code **)(*piVar2 + 0x70))(auStack_f0,piVar2,iVar10);
                FUN_00cb5628(&local_30c,auStack_f0);
                iVar7 = *(int *)(iVar5 + 0xc);
                iVar1 = iVar10 * 8;
                *(undefined4 *)(iVar7 + iVar10 * 8) = local_30c;
                iVar10 = iVar10 + 1;
                *(undefined4 *)(iVar7 + iVar1 + 4) = local_308;
              } while (iVar10 != iVar8);
            }
          }
        }
        *(int *)(iVar3 + 0x48) = iVar5;
      }
      iVar5 = local_40;
      iVar3 = local_6c;
      local_360 = 0;
      iVar8 = *(int *)(local_40 + 4);
      FUN_00caa6e4(local_40,iVar8 + 1);
      *(int *)(*(int *)(iVar5 + 0xc) + iVar8 * 4) = iVar3;
LAB_006f6f20:
      do {
        local_228 = "length";
        local_22c = 6;
        (**(code **)(*piVar4 + 0x38))(&local_98,piVar4,&local_22c,1);
        if ((local_98 == (int *)0x0) ||
           (iVar3 = (**(code **)(*local_98 + 0x14))(local_98), iVar3 != 0xff && iVar3 != 1))
        goto LAB_006f6890;
        dVar12 = (double)VectorSignedToFloat(local_360,(byte)(in_fpscr >> 0x16) & 3);
        if (local_98 == (int *)0x0) {
          dVar11 = 0.0;
        }
        else {
          dVar11 = (double)(**(code **)(*local_98 + 0x28))(local_98);
        }
        in_fpscr = in_fpscr & 0xfffffff | (uint)(dVar12 < dVar11) << 0x1f;
        if (!SUB41(in_fpscr >> 0x1f,0)) goto LAB_006f6890;
        (**(code **)(*piVar4 + 0x70))(&local_9c,piVar4,local_360);
        local_360 = local_360 + 1;
        local_230 = "userId";
        local_234 = 6;
        (**(code **)(*local_9c + 0x38))(&local_a0,local_9c,&local_234);
        local_238 = "userId";
        local_23c = 6;
        (**(code **)(*local_54 + 0x38))(&local_a4,local_54,&local_23c,1);
        piVar2 = local_a0;
      } while (local_a0 == local_a4);
      if ((local_a0 != (int *)0x0) && (local_a4 != (int *)0x0)) {
        pcVar9 = *(code **)(*local_a0 + 0x5c);
        uVar6 = (**(code **)(*local_a4 + 0x10))(local_a4);
        iVar3 = (*pcVar9)(piVar2,uVar6);
        if (iVar3 == 0) goto LAB_006f6f20;
      }
      local_244 = 8;
      local_240 = "userName";
      (**(code **)(*local_9c + 0x38))(auStack_a8,local_9c,&local_244,1);
      FUN_00cb5628(&local_24c,auStack_a8);
      local_158 = local_248;
      local_15c = local_24c;
      if ((local_248 != (char *)0x0) &&
         ((local_24c != 0 || ((local_248 != "" && (*local_248 != '\0')))))) {
        local_258 = "userName";
        local_25c = 8;
        (**(code **)(*local_9c + 0x38))(auStack_ac,local_9c,&local_25c,1);
        FUN_00cb5628(auStack_264,auStack_ac);
        FUN_003bca88(&local_254,auStack_264);
        local_15c = local_254;
        local_158 = local_250;
      }
      local_274 = 4;
      local_270 = &DAT_00cc7ad0;
      (**(code **)(*local_54 + 0x38))(auStack_b0,local_54,&local_274,1);
      FUN_00cb5628(auStack_27c,auStack_b0);
      FUN_003bca88(&local_26c,auStack_27c);
      local_280 = &DAT_00ccb8d4;
      local_284 = 2;
      (**(code **)(*local_54 + 0x38))(auStack_b4,local_54,&local_284,1);
      FUN_00cb5628(auStack_2bc,auStack_b4);
      local_2c4 = local_26c;
      local_2c0 = local_268;
      local_288 = &DAT_00cca338;
      local_28c = 2;
      (**(code **)(*local_54 + 0x38))(auStack_b8,local_54,&local_28c,1);
      FUN_00cb5628(auStack_2cc,auStack_b8);
      local_290 = "health";
      local_294 = 6;
      (**(code **)(*local_54 + 0x38))(&local_bc,local_54,&local_294,1);
      if (local_bc == (int *)0x0) {
        local_350 = local_bc;
      }
      else {
        local_350 = (int *)(**(code **)(*local_bc + 0x24))(local_bc);
      }
      local_298 = "userId";
      local_29c = 6;
      (**(code **)(*local_9c + 0x38))(auStack_c0,local_9c,&local_29c,1);
      FUN_00cb5628(auStack_2d4,auStack_c0);
      local_2dc = local_15c;
      local_2d8 = local_158;
      local_2a0 = "level";
      local_2a4 = 5;
      (**(code **)(*local_9c + 0x38))(&local_c4,local_9c,&local_2a4,1);
      iVar3 = 1 - (int)local_c4;
      if ((int *)0x1 < local_c4) {
        iVar3 = 0;
      }
      local_2e4[0] = (undefined1)iVar3;
      if (iVar3 == 0) {
        if (local_c4 == (int *)0x0) {
          local_2e0 = 0;
        }
        else {
          local_2e0 = (**(code **)(*local_c4 + 0x24))(local_c4);
        }
      }
      local_2a8 = "sessionId";
      local_2ac = 9;
      (**(code **)(*(int *)*param_1 + 0x38))(auStack_c8,(int *)*param_1,&local_2ac,1);
      FUN_00cb5628(auStack_2ec,auStack_c8);
      local_2b0 = &DAT_00cf6894;
      local_2b4 = 4;
      (**(code **)(*local_9c + 0x38))(auStack_cc,local_9c,&local_2b4,1);
      FUN_00cb5628(auStack_2f4,auStack_cc);
      FUN_0049af1c(&local_16c,auStack_2bc,&local_2c4,auStack_2cc,local_350,auStack_2d4,&local_2dc,
                   local_2e4,auStack_2ec,auStack_2f4);
      iVar3 = local_16c;
      local_2f8 = "constance";
      local_2fc = 9;
      (**(code **)(*local_54 + 0x38))(&local_d0,local_54,&local_2fc,1);
      iVar5 = local_16c;
      *(undefined4 *)(iVar3 + 0x4c) = local_d0;
      local_300 = "include";
      local_304 = 7;
      (**(code **)(*local_54 + 0x38))(&local_d4,local_54,&local_304,1);
      piVar2 = local_d4;
      if (local_d4 == (int *)0x0) {
        iVar3 = 0;
      }
      else {
        iVar3 = __dynamic_cast(local_d4,&DAT_00e948e8,&DAT_00df0758,0);
        if ((iVar3 == 0) &&
           ((**(code **)(*piVar2 + 0x58))(&local_f4,piVar2), local_f4 == DAT_00ee51f0)) {
          iVar8 = (**(code **)(*piVar2 + 0x6c))(piVar2);
          FUN_006f07b8(&local_f8,iVar8);
          iVar3 = local_f8;
          if (0 < iVar8) {
            iVar10 = 0;
            do {
              (**(code **)(*piVar2 + 0x70))(auStack_fc,piVar2,iVar10);
              FUN_00cb5628(&local_314,auStack_fc);
              iVar7 = *(int *)(iVar3 + 0xc);
              iVar1 = iVar10 * 8;
              *(undefined4 *)(iVar7 + iVar10 * 8) = local_314;
              iVar10 = iVar10 + 1;
              *(undefined4 *)(iVar7 + iVar1 + 4) = local_310;
            } while (iVar10 != iVar8);
          }
        }
      }
      iVar10 = local_40;
      iVar8 = local_16c;
      *(int *)(iVar5 + 0x48) = iVar3;
      iVar3 = *(int *)(local_40 + 4);
      FUN_00caa6e4(local_40,iVar3 + 1);
      *(int *)(*(int *)(iVar10 + 0xc) + iVar3 * 4) = iVar8;
      goto LAB_006f6f20;
    }
  } while( true );
}

