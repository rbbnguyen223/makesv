
undefined4 FBClientSocket_extractMessage(int *param_1)

{
  int iVar1;
  int iVar2;
  uint uVar3;
  code *pcVar4;
  int iVar5;
  int iVar6;
  int iVar7;
  int *piVar8;
  undefined4 uVar9;
  undefined1 auStack_98 [8];
  undefined4 local_90;
  char *local_8c;
  int local_88;
  int local_84;
  int *local_80;
  undefined4 *local_7c;
  undefined4 local_78;
  undefined4 local_74;
  int *local_70;
  undefined4 local_6c;
  undefined4 local_68;
  undefined4 local_64;
  int local_60;
  int *local_5c;
  int local_58;
  int local_54;
  int local_50;
  int local_4c;
  int local_48;
  int local_44;
  int local_40;
  undefined1 auStack_3c [4];
  undefined1 auStack_38 [4];
  undefined1 auStack_34 [4];
  int local_30;
  int *local_2c [2];
  
  local_30 = param_1[7];
  FUN_00cafca8(auStack_34,0);
  FUN_00cafca8(auStack_38,param_1[9]);
  FUN_002fa930(local_2c,&local_30,auStack_34,auStack_38);
  (**(code **)(*local_2c[0] + 0xa4))(local_2c[0],DAT_00ebbd6c);
  if (2 < param_1[9]) {
    iVar6 = 0;
    do {
      while( true ) {
        iVar2 = (**(code **)(*local_2c[0] + 0x98))(local_2c[0]);
        uVar3 = (**(code **)(*local_2c[0] + 0xb8))(local_2c[0]);
        uVar3 = uVar3 & 0xffff;
        if (param_1[8] < (int)uVar3) {
          local_8c = "Message format invalid";
          local_90 = 0x16;
          FUN_00caf618(auStack_3c,&local_90);
          FUN_00ca3ff8(auStack_98,auStack_3c);
        }
        if (param_1[9] + -2 <= (int)uVar3) goto LAB_008a9558;
        if (iVar2 != 99) break;
        FUN_00c71d1c(&local_48,uVar3);
        iVar6 = iVar6 + uVar3 + 3;
        local_40 = local_48;
        (**(code **)(*local_2c[0] + 0x9c))(local_2c[0],&local_40,0,uVar3);
        local_44 = local_48;
        (**(code **)(*param_1 + 0xb4))(param_1);
        iVar2 = param_1[9] - (uVar3 + 3);
        param_1[9] = iVar2;
        if (iVar2 < 3) goto LAB_008a9558;
      }
      FUN_00c71d1c(&local_48,uVar3);
      iVar6 = iVar6 + uVar3 + 3;
      local_4c = local_48;
      (**(code **)(*local_2c[0] + 0x9c))(local_2c[0],&local_4c,0,uVar3);
      local_58 = param_1[0xb];
      local_54 = local_48;
      FUN_00b196c0(&local_50,&local_54,&local_58);
      local_64 = 0;
      local_60 = local_50;
      local_48 = local_50;
      local_68 = 0;
      FUN_002fa930(&local_5c,&local_60,&local_64,&local_68);
      (**(code **)(*local_5c + 0xa4))(local_5c,DAT_00ebbd6c);
      local_70 = local_5c;
      FUN_00895164(&local_6c,&local_70,*(undefined4 *)(local_48 + 4));
      local_78 = local_6c;
      FUN_004d6a30(&local_74,iVar2,&local_78);
      piVar8 = (int *)param_1[0xc];
      pcVar4 = *(code **)(*piVar8 + 0x98);
      FUN_008a91d0(&local_88,0);
      iVar2 = local_88;
      iVar7 = *(int *)(local_88 + 4);
      uVar9 = *(undefined4 *)(param_1[1] + 0x14);
      FUN_00caa6e4(local_88,iVar7 + 1);
      iVar1 = local_88;
      *(undefined4 *)(*(int *)(iVar2 + 0xc) + iVar7 * 4) = uVar9;
      FUN_008a91d0(&local_84,0);
      uVar9 = local_74;
      iVar2 = local_84;
      iVar5 = *(int *)(local_84 + 4);
      FUN_00caa6e4(local_84,iVar5 + 1);
      iVar7 = local_84;
      *(undefined4 *)(*(int *)(iVar2 + 0xc) + iVar5 * 4) = uVar9;
      local_7c = (undefined4 *)FUN_00c8a9a0(0xc,1);
      local_7c[1] = iVar7;
      local_7c[2] = iVar1;
      *local_7c = &DAT_00e5ba18;
      (*pcVar4)(piVar8);
      iVar2 = param_1[9] - (uVar3 + 3);
      param_1[9] = iVar2;
    } while (2 < iVar2);
LAB_008a9558:
    if ((0 < iVar6) && (0 < param_1[9])) {
      local_80 = (int *)param_1[7];
      (**(code **)(*local_80 + 0x98))(local_80,0,&local_80,iVar6,param_1[9]);
    }
  }
  return 0;
}

