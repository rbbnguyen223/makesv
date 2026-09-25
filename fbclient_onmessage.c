
undefined4 FBClient_onMessage(int *param_1,int *param_2)

{
  undefined4 uStack_5c;
  undefined4 uStack_58;
  undefined4 local_54;
  undefined4 local_50;
  int local_4c;
  int local_48;
  undefined4 local_44;
  undefined *local_40;
  undefined4 local_3c;
  undefined *local_38;
  undefined4 local_34;
  int local_30;
  undefined4 local_2c;
  undefined4 local_28;
  undefined4 local_24;
  int local_20;
  undefined1 auStack_1c [8];
  
  local_3c = 3;
  local_38 = &DAT_00cf9e6c;
  local_30 = (**(code **)(**(int **)(*param_2 + 8) + 0x9c))(*(int **)(*param_2 + 8),&local_3c);
  if (local_30 == 0) {
    uStack_5c = DAT_00ebb0b0;
    uStack_58 = DAT_00ebb0b4;
    FUN_008a2054(&local_2c,&uStack_5c,&local_30);
    local_34 = local_2c;
    (**(code **)(*param_1 + 0xcc))(param_1);
  }
  else {
    local_44 = 3;
    local_40 = &DAT_00cf9e6c;
    (**(code **)(**(int **)(*param_2 + 8) + 0xa0))(auStack_1c,*(int **)(*param_2 + 8),&local_44);
    FUN_00cb5628(&local_4c,auStack_1c);
    param_1[0x10] = local_48;
    param_1[0xf] = local_4c;
    if (param_1[0x13] != 0) {
      local_20 = param_1[0x13];
      (**(code **)(*(int *)param_1[10] + 0xa8))((int *)param_1[10]);
      param_1[0x13] = 0;
    }
    local_24 = 0;
    local_54 = DAT_00ebb0a8;
    local_50 = DAT_00ebb0ac;
    FUN_008a2054(&local_2c,&local_54,&local_24);
    local_28 = local_2c;
    (**(code **)(*param_1 + 0xcc))(param_1);
  }
  param_1[0xe] = 0;
  *(undefined1 *)(param_1 + 0xc) = 0;
  param_1[0xb] = 4;
  return 0;
}

