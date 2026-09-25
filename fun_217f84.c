
undefined4 * FUN_00217f84(undefined4 *param_1,undefined4 *param_2)

{
  int iVar1;
  undefined4 local_a0;
  undefined4 local_9c;
  undefined4 local_98;
  undefined4 local_94;
  undefined4 local_90;
  char *local_8c;
  undefined4 local_88;
  char *local_84;
  undefined4 local_80;
  undefined4 local_7c;
  undefined4 local_78;
  undefined4 local_74;
  undefined4 local_70;
  char *local_6c;
  undefined4 local_68;
  undefined4 local_64;
  undefined4 local_60;
  char *local_5c;
  undefined4 local_58;
  char *local_54;
  undefined4 local_50;
  undefined4 local_4c;
  undefined4 local_48;
  char *local_44;
  undefined4 local_40;
  undefined4 local_3c;
  undefined4 local_38;
  char *local_34;
  undefined4 local_30;
  char *local_2c;
  undefined4 local_28;
  int local_24;
  undefined4 local_20;
  char *local_1c;
  
  local_24 = param_2[1];
  if (local_24 == 0) {
    *param_1 = 0;
  }
  else {
    local_28 = *param_2;
    local_20 = 6;
    local_1c = "neash.";
    iVar1 = FUN_003bcbd8(&local_28,&local_20);
    if (iVar1 == 0) {
      local_50 = *param_2;
    }
    else {
      local_40 = *param_2;
      local_3c = param_2[1];
      local_34 = "openfl.";
      local_30 = 6;
      local_38 = 7;
      local_2c = "neash.";
      FUN_003bc210(&local_80,&local_40,&local_30,&local_38);
      *param_2 = local_80;
      param_2[1] = local_7c;
      local_50 = local_80;
    }
    local_4c = param_2[1];
    local_48 = 7;
    local_44 = "native.";
    iVar1 = FUN_003bcbd8(&local_50,&local_48);
    if (iVar1 == 0) {
      local_78 = *param_2;
    }
    else {
      local_68 = *param_2;
      local_64 = param_2[1];
      local_5c = "openfl.";
      local_60 = 7;
      local_58 = 7;
      local_54 = "native.";
      FUN_003bc210(&local_80,&local_68,&local_58,&local_60);
      *param_2 = local_80;
      param_2[1] = local_7c;
      local_78 = local_80;
    }
    local_74 = param_2[1];
    local_70 = 6;
    local_6c = "flash.";
    iVar1 = FUN_003bcbd8(&local_78,&local_70);
    if (iVar1 == 0) {
      local_80 = *param_2;
    }
    else {
      local_98 = *param_2;
      local_94 = param_2[1];
      local_8c = "openfl.";
      local_88 = 6;
      local_90 = 7;
      local_84 = "flash.";
      FUN_003bc210(&local_80,&local_98,&local_88,&local_90);
      *param_2 = local_80;
      param_2[1] = local_7c;
    }
    local_9c = param_2[1];
    local_a0 = local_80;
    FUN_0034debc(param_1,&local_a0);
  }
  return param_1;
}

