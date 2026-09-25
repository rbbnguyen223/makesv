
int * FBClient_onMessageReceived_handler
                (int *param_1,int param_2,undefined4 *param_3,int *param_4,undefined1 param_5)

{
  undefined1 uVar1;
  int iVar2;
  int *piVar3;
  undefined4 uVar4;
  undefined8 uVar5;
  undefined4 local_40;
  undefined4 local_3c;
  undefined4 local_38;
  undefined4 local_34;
  undefined4 local_30;
  undefined4 local_2c;
  
  switch(*param_3) {
  case 4:
    uVar4 = param_3[1];
    iVar2 = memcmp(uVar4,&DAT_00d1f9bc,5);
    if (iVar2 == 0) {
      FUN_00167694(&local_30,param_4);
      *(undefined4 *)(param_2 + 0x54) = local_2c;
      *(undefined4 *)(param_2 + 0x50) = local_30;
      *param_1 = *param_4;
      return param_1;
    }
    iVar2 = memcmp(uVar4,&DAT_00d1d2b8,5);
    if (iVar2 == 0) {
      uVar4 = FUN_00171e28(param_4);
      *(undefined4 *)(param_2 + 0x58) = uVar4;
      *param_1 = *param_4;
      return param_1;
    }
    break;
  case 5:
    iVar2 = memcmp(param_3[1],"state",6);
    if (iVar2 == 0) {
      uVar4 = FUN_00171e28(param_4);
      *(undefined4 *)(param_2 + 0x2c) = uVar4;
      *param_1 = *param_4;
      return param_1;
    }
    break;
  case 6:
    uVar4 = param_3[1];
    iVar2 = memcmp(uVar4,"socket",7);
    if (iVar2 == 0) {
      piVar3 = (int *)*param_4;
      if (piVar3 == (int *)0x0) {
        iVar2 = 0;
      }
      else {
        iVar2 = (**(code **)(*piVar3 + 0x10))(piVar3);
        if ((iVar2 == 0) ||
           (iVar2 = __dynamic_cast(iVar2,&DAT_00e948e8,&DAT_00e5ba00,0), iVar2 == 0)) {
          iVar2 = (**(code **)(*piVar3 + 0xc))(piVar3,&DAT_00e5ba00);
        }
      }
      *(int *)(param_2 + 0x28) = iVar2;
      *param_1 = *param_4;
      return param_1;
    }
    iVar2 = memcmp(uVar4,"userId",7);
    if (iVar2 == 0) {
      FUN_00167694(&local_38,param_4);
      *(undefined4 *)(param_2 + 0x48) = local_34;
      *(undefined4 *)(param_2 + 0x44) = local_38;
      *param_1 = *param_4;
      return param_1;
    }
    break;
  case 7:
    iVar2 = memcmp(param_3[1],"session",8);
    if (iVar2 == 0) {
      FUN_00167694(&local_40,param_4);
      *(undefined4 *)(param_2 + 0x40) = local_3c;
      *(undefined4 *)(param_2 + 0x3c) = local_40;
      *param_1 = *param_4;
      return param_1;
    }
    break;
  case 8:
    break;
  case 9:
    iVar2 = memcmp(param_3[1],"isCheckIO",10);
    if (iVar2 == 0) {
      uVar1 = FUN_001933e8(param_4);
      *(undefined1 *)(param_2 + 0x68) = uVar1;
      *param_1 = *param_4;
      return param_1;
    }
    break;
  case 10:
    break;
  case 0xb:
    break;
  case 0xc:
    uVar4 = param_3[1];
    iVar2 = memcmp(uVar4,"currentTries",0xd);
    if (iVar2 == 0) {
      uVar4 = FUN_00171e28(param_4);
      *(undefined4 *)(param_2 + 0x38) = uVar4;
      *param_1 = *param_4;
      return param_1;
    }
    iVar2 = memcmp(uVar4,"requestQueue",0xd);
    if (iVar2 == 0) {
      piVar3 = (int *)*param_4;
      if (piVar3 == (int *)0x0) {
        iVar2 = 0;
      }
      else {
        iVar2 = (**(code **)(*piVar3 + 0x10))(piVar3);
        if ((iVar2 == 0) ||
           (iVar2 = __dynamic_cast(iVar2,&DAT_00e948e8,&DAT_00e1fc74,0), iVar2 == 0)) {
          iVar2 = (**(code **)(*piVar3 + 0xc))(piVar3,&DAT_00e1fc74);
        }
      }
      *(int *)(param_2 + 0x4c) = iVar2;
      *param_1 = *param_4;
      return param_1;
    }
    iVar2 = memcmp(uVar4,"onDisconnect",0xd);
    if (iVar2 == 0) {
      *(int *)(param_2 + 0x10) = *param_4;
      *param_1 = *param_4;
      return param_1;
    }
    break;
  case 0xd:
    break;
  case 0xe:
    uVar4 = param_3[1];
    iVar2 = memcmp(uVar4,"eventListeners",0xf);
    if (iVar2 == 0) {
      piVar3 = (int *)*param_4;
      if (piVar3 == (int *)0x0) {
        iVar2 = 0;
      }
      else {
        iVar2 = (**(code **)(*piVar3 + 0x10))(piVar3);
        if ((iVar2 == 0) ||
           (iVar2 = __dynamic_cast(iVar2,&DAT_00e948e8,&DAT_00e04690,0), iVar2 == 0)) {
          iVar2 = (**(code **)(*piVar3 + 0xc))(piVar3,&DAT_00e04690);
        }
      }
      *(int *)(param_2 + 0x24) = iVar2;
      *param_1 = *param_4;
      return param_1;
    }
    iVar2 = memcmp(uVar4,"isReconnecting",0xf);
    if (iVar2 == 0) {
      uVar1 = FUN_001933e8(param_4);
      *(undefined1 *)(param_2 + 0x30) = uVar1;
      *param_1 = *param_4;
      return param_1;
    }
    break;
  case 0xf:
    iVar2 = memcmp(param_3[1],"onIOThreadAlive",0x10);
    if (iVar2 == 0) {
      *(int *)(param_2 + 0x20) = *param_4;
      *param_1 = *param_4;
      return param_1;
    }
    break;
  case 0x10:
    break;
  case 0x11:
    uVar4 = param_3[1];
    iVar2 = memcmp(uVar4,"numReconnectTries",0x12);
    if (iVar2 == 0) {
      uVar4 = FUN_00171e28(param_4);
      *(undefined4 *)(param_2 + 0x34) = uVar4;
      *param_1 = *param_4;
      return param_1;
    }
    iVar2 = memcmp(uVar4,"onConnectionError",0x12);
    if (iVar2 == 0) {
      *(int *)(param_2 + 0xc) = *param_4;
      *param_1 = *param_4;
      return param_1;
    }
    iVar2 = memcmp(uVar4,"onMessageReceived",0x12);
    if (iVar2 == 0) {
      *(int *)(param_2 + 0x14) = *param_4;
      *param_1 = *param_4;
      return param_1;
    }
    break;
  case 0x12:
    uVar4 = param_3[1];
    iVar2 = memcmp(uVar4,"onConnectionOpened",0x13);
    if (iVar2 == 0) {
      *(int *)(param_2 + 4) = *param_4;
      *param_1 = *param_4;
      return param_1;
    }
    iVar2 = memcmp(uVar4,"onConnectionFailed",0x13);
    if (iVar2 == 0) {
      *(int *)(param_2 + 8) = *param_4;
      *param_1 = *param_4;
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
    break;
  case 0x17:
    break;
  case 0x18:
    iVar2 = memcmp(param_3[1],"lastReceiveIOThreadAlive",0x19);
    if (iVar2 == 0) {
      piVar3 = (int *)*param_4;
      if (piVar3 == (int *)0x0) {
        uVar5 = 0;
      }
      else {
        uVar5 = (**(code **)(*piVar3 + 0x28))(piVar3);
      }
      *(undefined8 *)(param_2 + 0x60) = uVar5;
      *param_1 = *param_4;
      return param_1;
    }
  }
  FUN_008af534(param_1,param_2,param_3,param_4,param_5);
  return param_1;
}

