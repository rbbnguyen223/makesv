
void LoginHandler_handleRegister(undefined4 param_1,int param_2)

{
  int iVar1;
  
  iVar1 = memcmp(param_1,param_2 + 0xbb19c0);
  if (iVar1 == 0) {
    FUN_00baf35c();
  }
  else {
    iVar1 = memcmp();
    if (iVar1 == 0) {
      FUN_00baf83c();
    }
    else {
      FUN_00ca36e4();
    }
  }
  return;
}

