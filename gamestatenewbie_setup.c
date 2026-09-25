
int * GameStateNewbie_setup_7be044
                (int *param_1,int param_2,undefined4 *param_3,int *param_4,undefined1 param_5)

{
  int iVar1;
  undefined4 uVar2;
  int iVar3;
  undefined1 uVar4;
  int *piVar5;
  int iVar6;
  undefined4 local_70;
  undefined4 local_6c;
  undefined4 local_68;
  undefined4 local_64;
  int local_60;
  int local_5c;
  undefined4 local_58;
  undefined4 local_54;
  undefined4 local_50;
  undefined4 local_4c;
  undefined4 local_48;
  undefined4 local_44;
  undefined4 local_40;
  undefined4 local_3c;
  undefined4 local_38;
  undefined4 local_34;
  undefined4 local_30;
  undefined4 local_2c [2];
  
  switch(*param_3) {
  case 3:
    iVar1 = memcmp(param_3[1],&DAT_00cfbcb4,4);
    if (iVar1 == 0) {
      piVar5 = (int *)*param_4;
      if (piVar5 == (int *)0x0) {
        iVar1 = 0;
      }
      else {
        iVar1 = (**(code **)(*piVar5 + 0x10))(piVar5);
        if ((iVar1 == 0) ||
           (iVar1 = __dynamic_cast(iVar1,&DAT_00e948e8,&DAT_00e897d0,0), iVar1 == 0)) {
          iVar1 = (**(code **)(*piVar5 + 0xc))(piVar5,&DAT_00e897d0);
        }
      }
      *(int *)(param_2 + 0x58) = iVar1;
      *param_1 = *param_4;
      return param_1;
    }
    break;
  case 4:
    break;
  case 5:
    uVar2 = param_3[1];
    iVar1 = memcmp(uVar2,"card1",6);
    if (iVar1 == 0) {
      FUN_007bd0b4(local_2c,param_4);
      *(undefined4 *)(param_2 + 0x20) = local_2c[0];
      *param_1 = *param_4;
      return param_1;
    }
    iVar1 = memcmp(uVar2,"card2",6);
    if (iVar1 == 0) {
      FUN_007bd0b4(&local_30,param_4);
      *(undefined4 *)(param_2 + 0x24) = local_30;
      *param_1 = *param_4;
      return param_1;
    }
    iVar1 = memcmp(uVar2,"card3",6);
    if (iVar1 == 0) {
      FUN_007bd0b4(&local_34,param_4);
      *(undefined4 *)(param_2 + 0x28) = local_34;
      *param_1 = *param_4;
      return param_1;
    }
    iVar1 = memcmp(uVar2,"panel",6);
    if (iVar1 == 0) {
      piVar5 = (int *)*param_4;
      if (piVar5 == (int *)0x0) {
        iVar1 = 0;
      }
      else {
        iVar1 = (**(code **)(*piVar5 + 0x10))(piVar5);
        if ((iVar1 == 0) ||
           (iVar1 = __dynamic_cast(iVar1,&DAT_00e948e8,&DAT_00e91258,0), iVar1 == 0)) {
          iVar1 = (**(code **)(*piVar5 + 0xc))(piVar5,&DAT_00e91258);
        }
      }
      *(int *)(param_2 + 0x40) = iVar1;
      *param_1 = *param_4;
      return param_1;
    }
    iVar1 = memcmp(uVar2,"heros",6);
    if (iVar1 == 0) {
      piVar5 = (int *)*param_4;
      if (piVar5 == (int *)0x0) {
        iVar1 = 0;
      }
      else {
        iVar1 = __dynamic_cast(piVar5,&DAT_00e948e8,&DAT_00dee708);
        if ((iVar1 == 0) &&
           ((**(code **)(*piVar5 + 0x58))(&local_60,piVar5), local_60 == DAT_00ee51f0)) {
          iVar3 = (**(code **)(*piVar5 + 0x6c))(piVar5);
          FUN_007bdec8(&local_5c,iVar3);
          iVar1 = local_5c;
          if (0 < iVar3) {
            iVar6 = 0;
            do {
              (**(code **)(*piVar5 + 0x70))(&local_58,piVar5,iVar6);
              *(undefined4 *)(*(int *)(local_5c + 0xc) + iVar6 * 4) = local_58;
              iVar6 = iVar6 + 1;
            } while (iVar6 != iVar3);
          }
        }
      }
      *(int *)(param_2 + 0x60) = iVar1;
      *param_1 = *param_4;
      return param_1;
    }
    iVar1 = memcmp(uVar2,"title",6);
    if (iVar1 == 0) {
      FUN_0016c400(&local_38,param_4);
      *(undefined4 *)(param_2 + 0x6c) = local_38;
      *param_1 = *param_4;
      return param_1;
    }
    break;
  case 6:
    break;
  case 7:
    uVar2 = param_3[1];
    iVar1 = memcmp(uVar2,"err_msg",8);
    if (iVar1 == 0) {
      FUN_0016f1d4(&local_3c,param_4);
      *(undefined4 *)(param_2 + 0x4c) = local_3c;
      *param_1 = *param_4;
      return param_1;
    }
    iVar1 = memcmp(uVar2,"next_bt",8);
    if (iVar1 == 0) {
      piVar5 = (int *)*param_4;
      if (piVar5 == (int *)0x0) {
        iVar1 = 0;
      }
      else {
        iVar1 = (**(code **)(*piVar5 + 0x10))(piVar5);
        if ((iVar1 == 0) ||
           (iVar1 = __dynamic_cast(iVar1,&DAT_00e948e8,&DAT_00e89e38,0), iVar1 == 0)) {
          iVar1 = (**(code **)(*piVar5 + 0xc))(piVar5,&DAT_00e89e38);
        }
      }
      *(int *)(param_2 + 0x50) = iVar1;
      *param_1 = *param_4;
      return param_1;
    }
    break;
  case 8:
    iVar1 = memcmp(param_3[1],"intro_lb",9);
    if (iVar1 == 0) {
      FUN_0016f1d4(&local_40,param_4);
      *(undefined4 *)(param_2 + 0x48) = local_40;
      *param_1 = *param_4;
      return param_1;
    }
    break;
  case 9:
    uVar2 = param_3[1];
    iVar1 = memcmp(uVar2,"_instance",10);
    if (iVar1 == 0) {
      piVar5 = (int *)*param_4;
      if (piVar5 == (int *)0x0) {
        iVar1 = 0;
      }
      else {
        iVar1 = (**(code **)(*piVar5 + 0x10))(piVar5);
        if ((iVar1 == 0) ||
           (iVar1 = __dynamic_cast(iVar1,&DAT_00e948e8,&DAT_00e4d530,0), iVar1 == 0)) {
          iVar1 = (**(code **)(*piVar5 + 0xc))(piVar5,&DAT_00e4d530);
        }
      }
      DAT_00eb7fe8 = iVar1;
      *param_1 = *param_4;
      return param_1;
    }
    iVar1 = memcmp(uVar2,"hero_name",10);
    if (iVar1 == 0) {
      piVar5 = (int *)*param_4;
      if (piVar5 == (int *)0x0) {
        iVar1 = 0;
      }
      else {
        iVar1 = (**(code **)(*piVar5 + 0x10))(piVar5);
        if ((iVar1 == 0) ||
           (iVar1 = __dynamic_cast(iVar1,&DAT_00e948e8,&DAT_00e58830,0), iVar1 == 0)) {
          iVar1 = (**(code **)(*piVar5 + 0xc))(piVar5,&DAT_00e58830);
        }
      }
      *(int *)(param_2 + 0x5c) = iVar1;
      *param_1 = *param_4;
      return param_1;
    }
    iVar1 = memcmp(uVar2,"loginData",10);
    if (iVar1 == 0) {
      piVar5 = (int *)*param_4;
      if (piVar5 == (int *)0x0) {
        iVar1 = 0;
      }
      else {
        iVar1 = (**(code **)(*piVar5 + 0x10))(piVar5);
        if ((iVar1 == 0) ||
           (iVar1 = __dynamic_cast(iVar1,&DAT_00e948e8,&DAT_00e386d8,0), iVar1 == 0)) {
          iVar1 = (**(code **)(*piVar5 + 0xc))(piVar5,&DAT_00e386d8);
        }
      }
      *(int *)(param_2 + 0x68) = iVar1;
      *param_1 = *param_4;
      return param_1;
    }
    iVar1 = memcmp(uVar2,"animArrow",10);
    if (iVar1 == 0) {
      FUN_0016c400(&local_44,param_4);
      *(undefined4 *)(param_2 + 0x70) = local_44;
      *param_1 = *param_4;
      return param_1;
    }
    iVar1 = memcmp(uVar2,"sparkAnim",10);
    if (iVar1 == 0) {
      FUN_0016c400(&local_48,param_4);
      *(undefined4 *)(param_2 + 0x74) = local_48;
      *param_1 = *param_4;
      return param_1;
    }
    break;
  case 10:
    uVar2 = param_3[1];
    iVar1 = memcmp(uVar2,"cur_cardid",0xb);
    if (iVar1 == 0) {
      uVar2 = FUN_00171e28(param_4);
      *(undefined4 *)(param_2 + 0x2c) = uVar2;
      *param_1 = *param_4;
      return param_1;
    }
    iVar1 = memcmp(uVar2,"pre_cardid",0xb);
    if (iVar1 == 0) {
      uVar2 = FUN_00171e28(param_4);
      *(undefined4 *)(param_2 + 0x30) = uVar2;
      *param_1 = *param_4;
      return param_1;
    }
    iVar1 = memcmp(uVar2,"_card_icon",0xb);
    if (iVar1 == 0) {
      piVar5 = (int *)*param_4;
      if (piVar5 == (int *)0x0) {
        iVar1 = 0;
      }
      else {
        iVar1 = (**(code **)(*piVar5 + 0x10))(piVar5);
        if ((iVar1 == 0) ||
           (iVar1 = __dynamic_cast(iVar1,&DAT_00e948e8,&DAT_00e11c08,0), iVar1 == 0)) {
          iVar1 = (**(code **)(*piVar5 + 0xc))(piVar5,&DAT_00e11c08);
        }
      }
      *(int *)(param_2 + 0x34) = iVar1;
      *param_1 = *param_4;
      return param_1;
    }
    break;
  case 0xb:
    uVar2 = param_3[1];
    iVar1 = memcmp(uVar2,"choose_name",0xc);
    if (iVar1 == 0) {
      FUN_00167694(&local_68,param_4);
      DAT_00eb7fe0 = local_68;
      DAT_00eb7fe4 = local_64;
      *param_1 = *param_4;
      return param_1;
    }
    iVar1 = memcmp(uVar2,"hb_value_lb",0xc);
    if (iVar1 == 0) {
      FUN_0016f1d4(&local_4c,param_4);
      *(undefined4 *)(param_2 + 0x38) = local_4c;
      *param_1 = *param_4;
      return param_1;
    }
    iVar1 = memcmp(uVar2,"selectFrame",0xc);
    if (iVar1 == 0) {
      FUN_0016c400(&local_50,param_4);
      *(undefined4 *)(param_2 + 0x44) = local_50;
      *param_1 = *param_4;
      return param_1;
    }
    iVar1 = memcmp(uVar2,"methodLogin",0xc);
    if (iVar1 == 0) {
      FUN_00167694(&local_70,param_4);
      *(undefined4 *)(param_2 + 0x7c) = local_6c;
      *(undefined4 *)(param_2 + 0x78) = local_70;
      *param_1 = *param_4;
      return param_1;
    }
    break;
  case 0xc:
    iVar1 = memcmp(param_3[1],"atk_value_lb",0xd);
    if (iVar1 == 0) {
      FUN_0016f1d4(&local_54,param_4);
      *(undefined4 *)(param_2 + 0x3c) = local_54;
      *param_1 = *param_4;
      return param_1;
    }
    break;
  case 0xd:
    iVar1 = memcmp(param_3[1],"android_tf_id",0xe);
    if (iVar1 == 0) {
      uVar2 = FUN_00171e28(param_4);
      *(undefined4 *)(param_2 + 100) = uVar2;
      *param_1 = *param_4;
      return param_1;
    }
    break;
  case 0xe:
    iVar1 = memcmp(param_3[1],"_is_first_down",0xf);
    if (iVar1 == 0) {
      piVar5 = (int *)*param_4;
      if ((piVar5 == (int *)0x0) || (iVar1 = (**(code **)(*piVar5 + 0x24))(piVar5), iVar1 == 0)) {
        uVar4 = 0;
      }
      else {
        uVar4 = 1;
      }
      *(undefined1 *)(param_2 + 0x54) = uVar4;
      *param_1 = *param_4;
      return param_1;
    }
  }
  FUN_00819628(param_1,param_2,param_3,param_4,param_5);
  return param_1;
}

