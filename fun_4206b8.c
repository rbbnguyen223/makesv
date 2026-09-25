
undefined4 FUN_004206b8(undefined4 *param_1,uint param_2,int param_3)

{
  uint uVar1;
  undefined4 uVar2;
  uint uVar3;
  int local_dc;
  undefined1 auStack_d8 [8];
  undefined4 local_d0;
  undefined4 local_cc;
  undefined4 local_c8;
  undefined4 local_c4;
  undefined4 local_c0;
  undefined4 local_bc;
  undefined4 local_b8;
  undefined4 local_b4;
  undefined4 local_b0;
  undefined4 local_ac;
  undefined1 auStack_a8 [8];
  undefined4 local_a0;
  undefined1 *local_9c;
  undefined4 local_98;
  undefined *local_94;
  undefined4 local_90;
  undefined4 local_8c;
  undefined4 local_88;
  char *local_84;
  undefined4 local_80;
  undefined4 local_7c;
  undefined4 local_78;
  undefined4 local_74;
  undefined4 local_70;
  undefined4 local_6c;
  undefined4 local_68;
  char *local_64;
  undefined4 local_60;
  undefined4 local_5c;
  undefined4 local_58;
  undefined4 local_54;
  undefined4 local_50;
  undefined4 local_4c;
  undefined4 local_48;
  char *local_44;
  undefined4 local_40;
  undefined4 local_3c;
  undefined4 local_38;
  char *local_34;
  undefined4 local_30;
  undefined4 local_2c;
  undefined4 local_28;
  undefined4 local_24;
  
  local_34 = "TEXT_FEED_TITLE_EVO_EX";
  local_24 = 0;
  local_38 = 0x16;
  local_dc = param_3;
  FUN_003a1300(&local_30,&local_38,&local_24);
  local_28 = 0;
  local_44 = "TEXT_FEED_MSG_EVO_EX";
  local_48 = 0x14;
  FUN_003a1300(&local_40,&local_48,&local_28);
  uVar3 = param_2 >> 0x1f;
  local_58 = local_40;
  local_54 = local_3c;
  FUN_0041e30c(&local_50,&local_58);
  local_74 = param_1[1];
  local_78 = *param_1;
  local_70 = local_50;
  local_6c = local_4c;
  local_64 = "[hero_name]";
  local_40 = local_50;
  local_3c = local_4c;
  local_68 = 0xb;
  FUN_003bc210(&local_60,&local_70,&local_68,&local_78);
  local_b0 = local_60;
  local_ac = local_5c;
  local_84 = "[next_star]";
  local_88 = 0xb;
  local_40 = local_60;
  local_3c = local_5c;
  uVar1 = uVar3;
  if (*(int *)(DAT_00eab0fc + 4) <= (int)param_2) {
    uVar1 = 1;
  }
  if (uVar1 == 0) {
    local_90 = *(undefined4 *)(*(int *)(DAT_00eab0fc + 0xc) + param_2 * 8);
    local_8c = *(undefined4 *)(*(int *)(DAT_00eab0fc + 0xc) + param_2 * 8 + 4);
  }
  else {
    local_8c = 0;
    local_90 = 0;
  }
  if (local_dc < 1) {
    local_a0 = 0;
    local_9c = &DAT_00cc7b44;
  }
  else {
    local_94 = &DAT_00ce204c;
    local_98 = 2;
    FUN_00cb806c(auStack_d8,&local_dc);
    FUN_00cb6f20(&local_a0,&local_98,auStack_d8);
  }
  FUN_00cb6f20(auStack_a8,&local_90,&local_a0);
  FUN_003bc210(&local_80,&local_b0,&local_88,auStack_a8);
  local_c0 = local_30;
  local_c8 = local_80;
  local_40 = local_80;
  local_bc = local_2c;
  local_c4 = local_7c;
  local_3c = local_7c;
  if (*(int *)(DAT_00eab0f0 + 4) <= (int)param_2) {
    uVar3 = 1;
  }
  if (uVar3 != 0) {
    uVar2 = 0;
    local_b4 = 0;
    local_b8 = 0;
  }
  else {
    local_b8 = *(undefined4 *)(*(int *)(DAT_00eab0f0 + 0xc) + param_2 * 8);
    uVar2 = *(undefined4 *)(*(int *)(DAT_00eab0f0 + 0xc) + param_2 * 8 + 4);
  }
  local_cc = 0;
  local_d0 = 0;
  if (uVar3 == 0) {
    local_b4 = uVar2;
  }
  FUN_0041ea74(&local_c0,&local_c8,&local_b8,&local_d0);
  return 0;
}

