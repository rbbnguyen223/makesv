
undefined8 Response_getContent(undefined4 param_1,int *param_2)

{
  int iVar1;
  int iVar2;
  
  iVar2 = *param_2;
  iVar1 = *(int *)(iVar2 + 4);
  FUN_00caa6e4(iVar2,iVar1 + 1);
  iVar2 = *(int *)(iVar2 + 0xc);
  *(undefined4 *)(iVar2 + iVar1 * 8) = 3;
  *(undefined **)(iVar2 + iVar1 * 8 + 4) = &DAT_00cf972c;
  iVar2 = *param_2;
  iVar1 = *(int *)(iVar2 + 4);
  FUN_00caa6e4(iVar2,iVar1 + 1);
  iVar2 = *(int *)(iVar2 + 0xc);
  *(undefined4 *)(iVar2 + iVar1 * 8) = 7;
  *(char **)(iVar2 + iVar1 * 8 + 4) = "content";
  return CONCAT44(param_2,param_1);
}

