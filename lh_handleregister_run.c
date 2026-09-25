
undefined4 * LoginHandler_handleRegister_run(undefined4 *param_1,int param_2,int *param_3)

{
  int iVar1;
  int *piVar2;
  undefined1 auStack_20 [8];
  
  if (((0 < *(int *)(*param_3 + 4)) &&
      (piVar2 = (int *)**(undefined4 **)(*param_3 + 0xc), piVar2 != (int *)0x0)) &&
     ((iVar1 = (**(code **)(*piVar2 + 0x10))(piVar2), iVar1 == 0 ||
      (iVar1 = __dynamic_cast(iVar1,&DAT_00e948e8,&DAT_00dfc050,0), iVar1 == 0)))) {
    (**(code **)(*piVar2 + 0xc))(piVar2,&DAT_00dfc050);
  }
  if (*(int *)(*(int *)(param_2 + 4) + 4) < 1) {
    piVar2 = (int *)0x0;
  }
  else {
    piVar2 = (int *)**(undefined4 **)(*(int *)(param_2 + 4) + 0xc);
  }
  (**(code **)(*piVar2 + 0x36c))(auStack_20,piVar2);
  *param_1 = 0;
  return param_1;
}

