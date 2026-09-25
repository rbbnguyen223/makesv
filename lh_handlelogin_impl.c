
undefined4 * LoginHandler_handleLogin_impl(undefined4 *param_1,uint *param_2)

{
  int iVar1;
  int *piVar2;
  undefined1 local_c;
  undefined1 local_b;
  
  piVar2 = (int *)*param_2;
  iVar1 = 1 - (int)piVar2;
  if ((int *)0x1 < piVar2) {
    iVar1 = 0;
  }
  local_c = (undefined1)iVar1;
  if (iVar1 == 0) {
    if ((piVar2 == (int *)0x0) || (iVar1 = (**(code **)(*piVar2 + 0x24))(piVar2), iVar1 == 0)) {
      local_b = 0;
    }
    else {
      local_b = 1;
    }
  }
  FUN_006f6328(&local_c);
  *param_1 = 0;
  return param_1;
}

