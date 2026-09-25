
undefined4 *
FUN_0057a0e4(undefined4 *param_1,undefined4 *param_2,undefined4 *param_3,int *param_4,
            undefined4 param_5,undefined4 param_6)

{
  char *pcVar1;
  undefined4 local_80;
  undefined *local_7c;
  undefined4 local_78;
  undefined *local_74;
  int local_70;
  char *local_6c;
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
  int *local_1c;
  
  FUN_00580a74(&local_1c,1);
  FUN_008942a0(&local_20);
  local_3c = "loginGame";
  local_34 = &DAT_00cf972c;
  local_40 = 9;
  local_38 = 3;
  (**(code **)(*local_20 + 0x9c))(local_20,&local_38,&local_40);
  local_4c = param_2[1];
  local_50 = *param_2;
  local_44 = &DAT_00cfa23c;
  local_48 = 3;
  (**(code **)(*local_20 + 0x9c))(local_20,&local_48,&local_50);
  local_5c = param_3[1];
  local_60 = *param_3;
  local_54 = &DAT_00cf9e6c;
  local_58 = 3;
  (**(code **)(*local_20 + 0x9c))(local_20,&local_58,&local_60);
  pcVar1 = (char *)param_4[1];
  if ((pcVar1 != (char *)0x0) && ((*param_4 != 0 || ((pcVar1 != "" && (*pcVar1 != '\0')))))) {
    local_64 = &DAT_00cfb220;
    local_68 = 3;
    local_70 = *param_4;
    local_6c = pcVar1;
    (**(code **)(*local_20 + 0x9c))(local_20,&local_68,&local_70);
  }
  FUN_008942a0(&local_24);
  local_74 = &DAT_00cfce2c;
  local_78 = 3;
  (**(code **)(*local_24 + 0xb0))(local_24,&local_78,param_6);
  local_28 = local_24;
  FUN_005785c4();
  local_7c = &DAT_00cfce14;
  local_80 = 3;
  local_2c = local_24;
  (**(code **)(*local_20 + 0xb8))(local_20,&local_80,&local_2c);
  local_30 = local_20;
  (**(code **)(*local_1c + 0x98))(local_1c);
  *param_1 = local_1c;
  return param_1;
}

