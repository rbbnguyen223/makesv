
undefined4 GameStateNewbie_method_7beb1c(int param_1)

{
  int iVar1;
  int iVar2;
  undefined1 auStack_50 [8];
  undefined4 local_48;
  undefined4 local_44;
  undefined4 local_40;
  undefined4 local_3c;
  undefined4 local_38;
  undefined4 local_34;
  undefined4 local_30;
  undefined4 local_2c;
  int local_28;
  undefined4 local_24;
  undefined4 *local_20;
  undefined4 local_1c;
  undefined4 local_18;
  int local_14;
  
  FUN_007bdec8(&local_14,0);
  iVar1 = local_14;
  iVar2 = *(int *)(local_14 + 4);
  FUN_00caa6e4(local_14,iVar2 + 1);
  *(int *)(*(int *)(iVar1 + 0xc) + iVar2 * 4) = param_1;
  local_1c = 0;
  local_38 = 0;
  local_34 = 0;
  local_18 = 0;
  (**(code **)(*DAT_00ee2aa8 + 0x368))(auStack_50,DAT_00ee2aa8,&local_38,&local_18,&local_1c);
  local_28 = (**(code **)(**(int **)(DAT_00ee2a80 + 0xa4) + 0xac))(*(int **)(DAT_00ee2a80 + 0xa4));
  if (local_28 == 0) {
    local_24 = *(undefined4 *)(param_1 + 0x68);
    local_20 = (undefined4 *)FUN_00c8a9a0(8,1);
    *local_20 = &DAT_00e4d488;
    local_20[1] = local_14;
    FUN_006f5c18(&local_24,&local_28,&local_20);
  }
  else {
    FUN_006f5fa4(&local_40);
    local_48 = local_40;
    local_44 = local_3c;
    (**(code **)(**(int **)(param_1 + 0x68) + 0x98))(&local_2c,*(int **)(param_1 + 0x68),&local_48);
    local_30 = local_2c;
    (**(code **)(**(int **)(DAT_00ee2a80 + 0xa4) + 0xbc))(*(int **)(DAT_00ee2a80 + 0xa4));
  }
  return 0;
}

