
undefined4 *
FUN_00578ae4(undefined4 *param_1,undefined4 *param_2,undefined4 *param_3,undefined4 param_4,
            undefined4 param_5)

{
  undefined4 local_70;
  undefined *local_6c;
  undefined4 local_68;
  undefined *local_64;
  undefined4 local_60;
  undefined4 local_5c;
  undefined4 local_58;
  undefined *local_54;
  undefined4 local_50;
  undefined4 local_4c;
  undefined4 local_48;
  undefined *local_44;
  undefined4 local_40;
  char *local_3c;
  undefined4 local_38;
  undefined *local_34;
  int *local_30;
  int *local_2c;
  int *local_28;
  int *local_24;
  int *local_20;
  int *local_1c [2];
  
  FUN_00580a74(local_1c,1);
  FUN_008942a0(&local_20);
  local_34 = &DAT_00cf972c;
  local_3c = "register";
  local_38 = 3;
  local_40 = 8;
  (**(code **)(*local_20 + 0x9c))(local_20,&local_38,&local_40);
  local_4c = param_2[1];
  local_50 = *param_2;
  local_44 = &DAT_00cfa23c;
  local_48 = 3;
  (**(code **)(*local_20 + 0x9c))(local_20,&local_48,&local_50);
  local_5c = param_3[1];
  local_60 = *param_3;
  local_54 = &DAT_00cfb220;
  local_58 = 3;
  (**(code **)(*local_20 + 0x9c))(local_20,&local_58,&local_60);
  FUN_008942a0(&local_24);
  local_64 = &DAT_00cfce2c;
  local_68 = 3;
  (**(code **)(*local_24 + 0xb0))(local_24,&local_68,param_5);
  local_28 = local_24;
  FUN_005785c4();
  local_6c = &DAT_00cfce14;
  local_70 = 3;
  local_2c = local_24;
  (**(code **)(*local_20 + 0xb8))(local_20,&local_70,&local_2c);
  local_30 = local_20;
  (**(code **)(*local_1c[0] + 0x98))(local_1c[0]);
  *param_1 = local_1c[0];
  return param_1;
}

