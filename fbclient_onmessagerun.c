
undefined4 * FBClient_onMessageRun(undefined4 *param_1,int param_2,int *param_3)

{
  int iVar1;
  undefined4 uVar2;
  int *piVar3;
  undefined1 auStack_30 [8];
  undefined1 local_28;
  int *local_20;
  int local_1c;
  
  if (((0 < *(int *)(*param_3 + 4)) &&
      (piVar3 = (int *)**(undefined4 **)(*param_3 + 0xc), piVar3 != (int *)0x0)) &&
     ((iVar1 = (**(code **)(*piVar3 + 0x10))(piVar3), iVar1 == 0 ||
      (iVar1 = __dynamic_cast(iVar1,&DAT_00e948e8,&DAT_00dfc050,0), iVar1 == 0)))) {
    (**(code **)(*piVar3 + 0xc))(piVar3,&DAT_00dfc050);
  }
  if (*(int *)(*(int *)(param_2 + 4) + 4) < 1) {
    iVar1 = 0;
  }
  else {
    iVar1 = **(int **)(*(int *)(param_2 + 4) + 0xc);
  }
  (**(code **)(**(int **)(iVar1 + 0xb4) + 0xe0))(auStack_30,*(int **)(iVar1 + 0xb4));
  if (*(int *)(*(int *)(param_2 + 4) + 4) < 1) {
    iVar1 = 0;
  }
  else {
    iVar1 = **(int **)(*(int *)(param_2 + 4) + 0xc);
  }
  (**(code **)(**(int **)(iVar1 + 0xac) + 0xd8))(&local_20,*(int **)(iVar1 + 0xac));
  uVar2 = (**(code **)(*local_20 + 0xec))(local_20);
  if (*(int *)(*(int *)(param_2 + 4) + 4) < 1) {
    iVar1 = 0;
  }
  else {
    iVar1 = **(int **)(*(int *)(param_2 + 4) + 0xc);
  }
  (**(code **)(**(int **)(iVar1 + 0xac) + 0xd8))(&local_1c,*(int **)(iVar1 + 0xac));
  local_28 = 1;
  FUN_004206b8(auStack_30,uVar2,*(undefined4 *)(local_1c + 0xb4));
  *param_1 = 0;
  return param_1;
}

