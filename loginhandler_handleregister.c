
undefined4 FUN_006f6158(undefined4 *param_1,undefined4 param_2)

{
  int local_88;
  int local_84;
  undefined1 local_80 [8];
  undefined4 local_78;
  undefined4 local_74;
  undefined4 local_70;
  undefined4 local_6c;
  undefined4 local_68;
  undefined4 local_64;
  undefined4 local_60;
  undefined4 local_5c;
  undefined1 local_58 [8];
  undefined4 local_50;
  undefined4 local_4c;
  undefined4 local_48;
  undefined4 local_44;
  undefined4 local_40;
  int local_3c;
  undefined4 local_38;
  undefined4 local_34;
  undefined4 local_30;
  undefined4 local_2c;
  undefined1 local_24 [4];
  
  FUN_006f5fa4(&local_30);
  if (DAT_00eb45d0 == 0) {
    local_74 = param_1[1];
    local_78 = *param_1;
    local_64 = DAT_00ec00f8;
    local_68 = DAT_00ec00f4;
    local_70 = local_30;
    local_6c = local_2c;
    local_80[0] = 1;
    local_88 = DAT_00eb45d0;
    local_84 = DAT_00eb45d0;
    FUN_00578ae4(local_24,&local_68,&local_70,&local_78,param_2,local_80,&local_88);
  }
  else {
    local_40 = DAT_00eb45cc;
    local_4c = param_1[1];
    local_50 = *param_1;
    local_38 = DAT_00ec00f4;
    local_34 = DAT_00ec00f8;
    local_48 = local_30;
    local_44 = local_2c;
    local_58[0] = 1;
    local_5c = 0;
    local_60 = 0;
    local_3c = DAT_00eb45d0;
    FUN_0057a0e4(local_24,&local_38,&local_40,&local_48,&local_50,param_2,local_58,&local_60);
  }
  (**(code **)(**(int **)(DAT_00ee2a80 + 0xa4) + 0xbc))(*(int **)(DAT_00ee2a80 + 0xa4));
  return 0;
}

