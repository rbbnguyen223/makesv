
undefined4 *
FUN_0057a32c(undefined4 *param_1,undefined4 *param_2,undefined4 *param_3,undefined4 *param_4,
            int *param_5)

{
  char *pcVar1;
  int local_90;
  char *local_8c;
  undefined4 local_88;
  undefined *local_84;
  undefined4 local_80;
  undefined *local_7c;
  undefined4 local_78;
  undefined4 local_74;
  undefined4 local_70;
  undefined *local_6c;
  undefined4 local_68;
  undefined4 local_64;
  undefined4 local_60;
  undefined *local_5c;
  undefined4 local_58;
  undefined4 local_54;
  undefined4 local_50;
  undefined *local_4c;
  undefined4 local_48;
  char *local_44;
  undefined4 local_40;
  undefined *local_3c;
  int *local_38;
  undefined4 local_34;
  undefined4 local_30;
  undefined4 local_2c;
  int *local_28;
  int *local_24 [2];
  
  FUN_00580a74(local_24,1);
  FUN_008942a0(&local_28);
  local_3c = &DAT_00cf972c;
  local_44 = "loginGame";
  local_48 = 9;
  local_40 = 3;
  (**(code **)(*local_28 + 0x9c))(local_28,&local_40,&local_48);
  local_54 = param_2[1];
  local_58 = *param_2;
  local_4c = &DAT_00cfa23c;
  local_50 = 3;
  (**(code **)(*local_28 + 0x9c))(local_28,&local_50,&local_58);
  local_64 = param_3[1];
  local_68 = *param_3;
  local_5c = &DAT_00ce2720;
  local_60 = 3;
  (**(code **)(*local_28 + 0x9c))(local_28,&local_60,&local_68);
  local_74 = param_4[1];
  local_78 = *param_4;
  local_6c = &DAT_00cfb218;
  local_70 = 3;
  (**(code **)(*local_28 + 0x9c))(local_28,&local_70,&local_78);
  FUN_008942a0(&local_2c);
  local_30 = local_2c;
  FUN_005785c4();
  local_7c = &DAT_00cfce14;
  local_80 = 3;
  local_34 = local_2c;
  (**(code **)(*local_28 + 0xb8))(local_28,&local_80,&local_34);
  pcVar1 = (char *)param_5[1];
  if ((pcVar1 != (char *)0x0) && ((*param_5 != 0 || ((pcVar1 != "" && (*pcVar1 != '\0')))))) {
    local_84 = &DAT_00cfb220;
    local_88 = 3;
    local_90 = *param_5;
    local_8c = pcVar1;
    (**(code **)(*local_28 + 0x9c))(local_28,&local_88,&local_90);
  }
  local_38 = local_28;
  (**(code **)(*local_24[0] + 0x98))(local_24[0]);
  *param_1 = local_24[0];
  return param_1;
}

