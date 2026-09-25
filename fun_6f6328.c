
undefined4 FUN_006f6328(char *param_1)

{
  uint uVar1;
  undefined4 local_d0;
  undefined4 local_cc;
  undefined1 local_c8 [8];
  undefined4 local_c0;
  undefined4 local_bc;
  undefined4 local_b8;
  undefined4 local_b4;
  undefined4 local_b0;
  undefined4 local_ac;
  undefined4 local_a8;
  undefined4 local_a4;
  uint local_a0;
  uint local_9c;
  undefined1 local_98 [8];
  uint local_90;
  uint local_8c;
  undefined4 local_88;
  undefined4 local_84;
  int local_80;
  char *local_7c;
  undefined4 local_78;
  undefined4 local_74;
  undefined4 local_70;
  undefined4 local_6c;
  undefined1 local_68 [8];
  undefined4 local_60;
  undefined4 local_5c;
  undefined4 local_58;
  undefined4 local_54;
  undefined4 local_50;
  undefined4 local_4c;
  int local_48;
  char *local_44;
  undefined4 local_40;
  undefined4 local_3c;
  undefined4 local_38;
  undefined4 local_34;
  undefined1 local_2c [8];
  
  if (*param_1 == '\0') {
    uVar1 = (uint)(byte)param_1[1];
  }
  else {
    uVar1 = 0;
  }
  FUN_006f5fa4(&local_38);
  if ((DAT_00eb45d0 == (char *)0x0) ||
     ((DAT_00eb45cc == 0 && ((DAT_00eb45d0 == "" || (*DAT_00eb45d0 == '\0')))))) {
    local_b4 = DAT_00eabf30;
    local_b8 = DAT_00eabf2c;
    local_a4 = DAT_00ec00f8;
    local_ac = DAT_00eabf28;
    local_a8 = DAT_00ec00f4;
    local_b0 = DAT_00eabf24;
    local_c0 = local_38;
    local_bc = local_34;
    local_c8[0] = 1;
    local_cc = 0;
    local_d0 = 0;
    FUN_0057a32c(local_2c,&local_a8,&local_b0,&local_b8,&local_c0,local_c8,&local_d0);
  }
  else if (uVar1 == 0) {
    local_78 = DAT_00ec00f4;
    local_74 = DAT_00ec00f8;
    local_88 = local_38;
    local_84 = local_34;
    local_98[0] = 1;
    local_a0 = uVar1;
    local_9c = uVar1;
    local_90 = uVar1;
    local_8c = uVar1;
    local_80 = DAT_00eb45cc;
    local_7c = DAT_00eb45d0;
    FUN_0057a9a0(local_2c,&local_78,&local_80,&local_88,&local_90,local_98,&local_a0);
  }
  else {
    local_3c = DAT_00ec00f8;
    local_4c = DAT_00eabf28;
    local_54 = DAT_00eabf30;
    local_40 = DAT_00ec00f4;
    local_50 = DAT_00eabf24;
    local_58 = DAT_00eabf2c;
    local_60 = local_38;
    local_5c = local_34;
    local_68[0] = 1;
    local_6c = 0;
    local_70 = 0;
    local_48 = DAT_00eb45cc;
    local_44 = DAT_00eb45d0;
    FUN_0057a6fc(local_2c,&local_40,&local_48,&local_50,&local_58,&local_60,local_68,&local_70);
  }
  (**(code **)(**(int **)(DAT_00ee2a80 + 0xa4) + 0xbc))(*(int **)(DAT_00ee2a80 + 0xa4));
  return 0;
}

