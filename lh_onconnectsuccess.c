
undefined4 * LoginHandler_onConnectSuccess_6f6068(undefined4 *param_1,int param_2,int *param_3)

{
  int *piVar1;
  undefined4 local_30;
  undefined4 local_2c;
  undefined4 local_28;
  undefined4 local_24;
  undefined4 local_20;
  undefined4 local_1c;
  undefined1 auStack_18 [4];
  undefined4 local_14 [2];
  
  if (*(int *)(*param_3 + 4) < 1) {
    local_14[0] = 0;
  }
  else {
    local_14[0] = **(undefined4 **)(*param_3 + 0xc);
  }
  FUN_002e2d50(auStack_18,local_14);
  FUN_006f5fa4(&local_28);
  if (*(int *)(*(int *)(param_2 + 4) + 4) < 1) {
    piVar1 = (int *)0x0;
  }
  else {
    piVar1 = (int *)**(undefined4 **)(*(int *)(param_2 + 4) + 0xc);
  }
  local_30 = local_28;
  local_2c = local_24;
  (**(code **)(*piVar1 + 0x98))(&local_1c,piVar1,&local_30);
  local_20 = local_1c;
  (**(code **)(**(int **)(DAT_00ee2a80 + 0xa4) + 0xbc))(*(int **)(DAT_00ee2a80 + 0xa4));
  *param_1 = 0;
  return param_1;
}

