
undefined4 *
LoginHandler_method_6ef638
          (undefined4 *param_1,undefined4 param_2,undefined4 *param_3,undefined4 param_4)

{
  int iVar1;
  undefined4 uVar2;
  
  switch(*param_3) {
  case 3:
    iVar1 = memcmp(param_3[1],&DAT_00cd3f88,4);
    if (iVar1 == 0) {
      FUN_006ef074(param_1);
      return param_1;
    }
    break;
  case 4:
    break;
  case 5:
    break;
  case 6:
    break;
  case 7:
    uVar2 = param_3[1];
    iVar1 = memcmp(uVar2,"isLogin",8);
    if (iVar1 == 0) {
      FUN_00caeeac(param_1,DAT_00eb45b4);
      return param_1;
    }
    iVar1 = memcmp(uVar2,"onLogin",8);
    if (iVar1 == 0) {
      *param_1 = DAT_00eb45c4;
      return param_1;
    }
    iVar1 = memcmp(uVar2,"session",8);
    if (iVar1 == 0) {
      FUN_00caf618(param_1,&DAT_00eb45cc);
      return param_1;
    }
    iVar1 = memcmp(uVar2,"Connect",8);
    if (iVar1 == 0) {
      FUN_006ef174(param_1);
      return param_1;
    }
    iVar1 = memcmp(uVar2,"topUser",8);
    if (iVar1 == 0) {
      FUN_006eeff4(param_1);
      return param_1;
    }
    break;
  case 8:
    uVar2 = param_3[1];
    iVar1 = memcmp(uVar2,"readIMEI",9);
    if (iVar1 == 0) {
      FUN_006ef1d4(param_1);
      return param_1;
    }
    iVar1 = memcmp(uVar2,"feedback",9);
    if (iVar1 == 0) {
      FUN_006ef054(param_1);
      return param_1;
    }
    break;
  case 9:
    break;
  case 10:
    uVar2 = param_3[1];
    iVar1 = memcmp(uVar2,"onFullData",0xb);
    if (iVar1 == 0) {
      *param_1 = DAT_00eb45c8;
      return param_1;
    }
    iVar1 = memcmp(uVar2,"friendList",0xb);
    if (iVar1 == 0) {
      FUN_006eebdc(param_1);
      return param_1;
    }
    iVar1 = memcmp(uVar2,"readGvGLog",0xb);
    if (iVar1 == 0) {
      FUN_006ef134(param_1);
      return param_1;
    }
    iVar1 = memcmp(uVar2,"topSession",0xb);
    if (iVar1 == 0) {
      FUN_006eeb7c(param_1);
      return param_1;
    }
    break;
  case 0xb:
    uVar2 = param_3[1];
    iVar1 = memcmp(uVar2,"handleLogin",0xc);
    if (iVar1 == 0) {
      FUN_006ef5f4(param_1);
      return param_1;
    }
    iVar1 = memcmp(uVar2,"validateSnS",0xc);
    if (iVar1 == 0) {
      FUN_006ef614(param_1);
      return param_1;
    }
    iVar1 = memcmp(uVar2,"parseServer",0xc);
    if (iVar1 == 0) {
      FUN_006ef5d4(param_1);
      return param_1;
    }
    break;
  case 0xc:
    uVar2 = param_3[1];
    iVar1 = memcmp(uVar2,"handleLogout",0xd);
    if (iVar1 == 0) {
      FUN_006ef1f4(param_1);
      return param_1;
    }
    iVar1 = memcmp(uVar2,"verifyIAPios",0xd);
    if (iVar1 == 0) {
      FUN_006ef154(param_1);
      return param_1;
    }
    break;
  case 0xd:
    uVar2 = param_3[1];
    iVar1 = memcmp(uVar2,"registerEvent",0xe);
    if (iVar1 == 0) {
      FUN_006ef1b4(param_1);
      return param_1;
    }
    iVar1 = memcmp(uVar2,"getServerList",0xe);
    if (iVar1 == 0) {
      FUN_006ef0f4(param_1);
      return param_1;
    }
    iVar1 = memcmp(uVar2,"readPvPVIPLog",0xe);
    if (iVar1 == 0) {
      FUN_006eeb9c(param_1);
      return param_1;
    }
    iVar1 = memcmp(uVar2,"readBattleLog",0xe);
    if (iVar1 == 0) {
      FUN_006ef0b4(param_1);
      return param_1;
    }
    iVar1 = memcmp(uVar2,"friendListSnS",0xe);
    if (iVar1 == 0) {
      FUN_006ef094(param_1);
      return param_1;
    }
    break;
  case 0xe:
    uVar2 = param_3[1];
    iVar1 = memcmp(uVar2,"handleRegister",0xf);
    if (iVar1 == 0) {
      FUN_006eebfc(param_1);
      return param_1;
    }
    iVar1 = memcmp(uVar2,"openATMPayment",0xf);
    if (iVar1 == 0) {
      FUN_006ef194(param_1);
      return param_1;
    }
    break;
  case 0xf:
    iVar1 = memcmp(param_3[1],"sendCardPayment",0x10);
    if (iVar1 == 0) {
      FUN_006ef014(param_1);
      return param_1;
    }
    break;
  case 0x10:
    iVar1 = memcmp(param_3[1],"verifyIAPAndroid",0x11);
    if (iVar1 == 0) {
      FUN_006ef0d4(param_1);
      return param_1;
    }
    break;
  case 0x11:
    uVar2 = param_3[1];
    iVar1 = memcmp(uVar2,"friendRequestList",0x12);
    if (iVar1 == 0) {
      FUN_006eebbc(param_1);
      return param_1;
    }
    iVar1 = memcmp(uVar2,"getServerConstant",0x12);
    if (iVar1 == 0) {
      FUN_006ef114(param_1);
      return param_1;
    }
    break;
  case 0x12:
    iVar1 = memcmp(param_3[1],"validateSnSMapping",0x13);
    if (iVar1 == 0) {
      FUN_006ef034(param_1);
      return param_1;
    }
    break;
  case 0x13:
    break;
  case 0x14:
    break;
  case 0x15:
    break;
  case 0x16:
    iVar1 = memcmp(param_3[1],"convertByteArray2Bytes",0x17);
    if (iVar1 == 0) {
      FUN_006ef5b4(param_1);
      return param_1;
    }
  }
  FUN_00ca36e4(param_1,param_2,param_3,param_4);
  return param_1;
}

