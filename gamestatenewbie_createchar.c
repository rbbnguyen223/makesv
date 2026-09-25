
undefined4 GameStateNewbie_CreateCharacter(void)

{
  int *piVar1;
  undefined4 uVar2;
  int iVar3;
  int *piVar4;
  int in_r3;
  int unaff_r4;
  int unaff_r5;
  code *pcVar5;
  int unaff_r8;
  undefined8 uVar6;
  undefined4 in_stack_0000001c;
  undefined1 in_stack_00000030;
  undefined1 in_stack_00000040;
  undefined4 in_stack_00000048;
  undefined4 in_stack_0000004c;
  undefined1 in_stack_00000050;
  undefined4 in_stack_00000058;
  undefined4 in_stack_0000005c;
  undefined1 in_stack_00000060;
  undefined1 in_stack_00000070;
  undefined1 in_stack_00000080;
  undefined1 in_stack_00000090;
  undefined1 in_stack_000000a0;
  undefined1 in_stack_000000b0;
  undefined1 in_stack_000000c0;
  undefined1 in_stack_000000d0;
  undefined4 in_stack_00000104;
  char *in_stack_00000108;
  undefined4 in_stack_0000010c;
  char *in_stack_00000110;
  undefined4 in_stack_00000114;
  char *in_stack_00000118;
  undefined4 in_stack_0000011c;
  undefined *in_stack_00000120;
  undefined1 in_stack_00000124;
  undefined4 in_stack_0000012c;
  char *in_stack_00000130;
  undefined1 in_stack_00000134;
  undefined1 in_stack_0000013c;
  undefined1 in_stack_00000144;
  undefined1 in_stack_0000014c;
  undefined1 in_stack_00000154;
  undefined1 in_stack_0000015c;
  undefined4 in_stack_00000164;
  int *in_stack_00000184;
  undefined4 in_stack_00000188;
  undefined4 *in_stack_0000018c;
  int *in_stack_00000190;
  undefined4 in_stack_00000194;
  int *in_stack_00000198;
  undefined4 in_stack_0000019c;
  int *in_stack_000001a0;
  undefined4 in_stack_000001a4;
  undefined4 in_stack_000001a8;
  int *in_stack_000001ac;
  undefined4 in_stack_000001b0;
  int *in_stack_000001b4;
  undefined4 in_stack_000001b8;
  int *in_stack_000001bc;
  undefined4 in_stack_000001c0;
  undefined4 in_stack_000001c4;
  int *in_stack_000001c8;
  int *in_stack_000001cc;
  undefined4 in_stack_000001d0;
  undefined4 in_stack_000001d4;
  undefined4 in_stack_000001d8;
  int *in_stack_000001dc;
  undefined4 in_stack_000001e4;
  int *in_stack_000001e8;
  undefined4 in_stack_000001ec;
  undefined4 in_stack_000001f0;
  
  uVar2 = (**(code **)(in_r3 + 0x130))();
  FUN_00bb50f8(&stack0x00000200,uVar2,&stack0x00000164,&stack0x0000015c);
  *(undefined4 *)(unaff_r8 + -0x170) = 0;
  *(undefined4 *)(unaff_r8 + -0x16c) = 0;
  *(undefined4 *)(unaff_r8 + -0x160) = 0;
  *(undefined4 *)(unaff_r8 + -0x15c) = 0;
  uVar2 = FUN_00c8a9a0(8);
  FUN_00c8179c();
  in_stack_00000120 = &DAT_00cc8934;
  in_stack_0000011c = 4;
  FUN_00cafca8(&stack0x00000180,3);
  FUN_00c81a50(uVar2,&stack0x0000011c,&stack0x00000180,0);
  in_stack_000001f0 = uVar2;
  FUN_004293f8(&stack0x000001f4,&stack0x000001ec,&stack0x000000d0,&stack0x000000c0);
  in_stack_000000b0 = 1;
  in_stack_000000a0 = 1;
  in_stack_00000090 = 1;
  in_stack_00000080 = 1;
  in_stack_00000070 = 1;
  in_stack_00000060 = 1;
  FUN_00c510a0(&stack0x000001e8,&stack0x000000b0,&stack0x000000a0,&stack0x00000090);
  FUN_00cafca8(&stack0x000001e0,0x46);
  FUN_004eb7a8(&stack0x000001dc,&stack0x000001e0,&stack0x0000022c);
  in_stack_000001d8 = 0;
  in_stack_00000058 = 0;
  in_stack_0000005c = 0;
  in_stack_00000048 = 0;
  in_stack_0000004c = 0;
  in_stack_00000050 = 0;
  in_stack_00000040 = 0;
  (**(code **)(*in_stack_000001dc + 0xb8))(&stack0x000001e4,in_stack_000001dc,0x1c,&stack0x00000050)
  ;
  in_stack_000001d4 = in_stack_000001e4;
  (**(code **)(*in_stack_000001e8 + 0x1ec))(&stack0x00000028,in_stack_000001e8,&stack0x000001d4);
  (**(code **)(*in_stack_000001e8 + 0x1ec))(&stack0x00000028,in_stack_000001e8);
  uVar6 = (**(code **)(**(int **)(unaff_r4 + 0x34) + 0x1b4))(*(int **)(unaff_r4 + 0x34));
  (**(code **)(*in_stack_000001e8 + 0x1b8))
            (in_stack_000001e8,*in_stack_000001e8,(int)uVar6,(int)((ulonglong)uVar6 >> 0x20));
  uVar6 = (**(code **)(**(int **)(unaff_r4 + 0x34) + 0x1bc))(*(int **)(unaff_r4 + 0x34));
  (**(code **)(*in_stack_000001e8 + 0x1c0))
            (in_stack_000001e8,*in_stack_000001e8,(int)uVar6,(int)((ulonglong)uVar6 >> 0x20));
  (**(code **)(*in_stack_000001e8 + 0x274))(in_stack_000001e8,*in_stack_000001e8,0,0x3ff80000);
  (**(code **)(*in_stack_000001e8 + 0x11c))(in_stack_000001e8,*in_stack_000001e8,0,0);
  in_stack_000001cc = in_stack_000001e8;
  in_stack_00000134 = 1;
  (**(code **)(**(int **)(unaff_r4 + 0x40) + 0x2fc))
            (*(int **)(unaff_r4 + 0x40),&stack0x000001cc,&stack0x00000134);
  in_stack_00000130 = "Ahri_Hon_Gio.wav";
  in_stack_0000012c = 0x10;
  FUN_003cfb8c(&stack0x000001c8,&stack0x0000012c,&stack0x00000228);
  in_stack_00000124 = 1;
  in_stack_00000030 = 1;
  (**(code **)(*in_stack_000001c8 + 0xa4))(in_stack_000001c8,&stack0x00000124,&stack0x00000030);
  FUN_002b27b4(&stack0x000001c4);
  in_stack_000001bc = in_stack_000001e8;
  uVar2 = FUN_00c8a9a0(8,1);
  FUN_00c8179c();
  in_stack_00000118 = "alpha";
  in_stack_00000114 = 5;
  FUN_00cafca8(&stack0x0000017c,1);
  FUN_00c81a50(uVar2,&stack0x00000114,&stack0x0000017c,0);
  in_stack_000001b8 = 0;
  in_stack_000001c0 = uVar2;
  FUN_002ca140(&stack0x000001b4,&stack0x000001bc,0,0x3fe00000);
  in_stack_000001b0 = in_stack_000001c4;
  (**(code **)(*in_stack_000001b4 + 0xb0))(&stack0x000001ac,in_stack_000001b4,&stack0x000001b0);
  piVar1 = in_stack_000001ac;
  if (((in_stack_000001ac == (int *)0x0) ||
      (((iVar3 = (**(code **)(*in_stack_000001ac + 0x10))(in_stack_000001ac), iVar3 == 0 ||
        (iVar3 = __dynamic_cast(iVar3,*(undefined4 *)(unaff_r5 + 0x9ac),
                                *(undefined4 *)(unaff_r5 + 0x1d34),0), iVar3 == 0)) &&
       (iVar3 = (**(code **)(*piVar1 + 0xc))(piVar1,*(undefined4 *)(unaff_r5 + 0x1d34)), iVar3 == 0)
       ))) && (in_stack_000001ac != (int *)0x0)) {
    FUN_00cb0ad4();
  }
  FUN_002b27b4(&stack0x000001a8);
  in_stack_000001a0 = in_stack_000001e8;
  uVar2 = FUN_00c8a9a0(8,1);
  FUN_00c8179c();
  in_stack_00000108 = "scaleX";
  in_stack_00000104 = 6;
  FUN_00cafe38(&stack0x00000174,"scaleX",0,0x3ff00000);
  FUN_00c81a50(uVar2,&stack0x00000104,&stack0x00000174,0);
  in_stack_00000110 = "scaleY";
  in_stack_0000010c = 6;
  FUN_00cafe38(&stack0x00000178,"scaleY",0,0x3ff00000);
  FUN_00c81a50(uVar2,&stack0x0000010c,&stack0x00000178,0);
  in_stack_0000019c = 0;
  in_stack_000001a4 = uVar2;
  FUN_002ca140(&stack0x00000198,&stack0x000001a0,0,0x3fe00000);
  in_stack_00000194 = in_stack_000001a8;
  (**(code **)(*in_stack_00000198 + 0xb0))(&stack0x00000190,in_stack_00000198,&stack0x00000194);
  piVar1 = in_stack_00000190;
  if (in_stack_00000190 == (int *)0x0) {
    piVar4 = (int *)0x0;
  }
  else {
    iVar3 = (**(code **)(*in_stack_00000190 + 0x10))(in_stack_00000190);
    if (((iVar3 != 0) &&
        (piVar4 = (int *)__dynamic_cast(iVar3,*(undefined4 *)(unaff_r5 + 0x9ac),
                                        *(undefined4 *)(unaff_r5 + 0x1d34),0), piVar4 != (int *)0x0)
        ) || (piVar4 = (int *)(**(code **)(*piVar1 + 0xc))
                                        (piVar1,*(undefined4 *)(unaff_r5 + 0x1d34)),
             piVar4 != (int *)0x0)) goto LAB_007c30f8;
  }
  if (in_stack_00000190 != (int *)0x0) {
    FUN_00cb0ad4();
  }
LAB_007c30f8:
  pcVar5 = *(code **)(*piVar4 + 0xb8);
  in_stack_0000018c = (undefined4 *)FUN_00c8a9a0(8,1);
  *in_stack_0000018c = &DAT_00e4d3d8;
  in_stack_0000018c[1] = in_stack_0000001c;
  in_stack_00000188 = 0;
  (*pcVar5)(&stack0x00000184,piVar4,&stack0x0000018c,&stack0x00000188);
  piVar1 = in_stack_00000184;
  if (((in_stack_00000184 == (int *)0x0) ||
      (((iVar3 = (**(code **)(*in_stack_00000184 + 0x10))(in_stack_00000184), iVar3 == 0 ||
        (iVar3 = __dynamic_cast(iVar3,*(undefined4 *)(unaff_r5 + 0x9ac),
                                *(undefined4 *)(unaff_r5 + 0x1d34),0), iVar3 == 0)) &&
       (iVar3 = (**(code **)(*piVar1 + 0xc))(piVar1,*(undefined4 *)(unaff_r5 + 0x1d34)), iVar3 == 0)
       ))) && (in_stack_00000184 != (int *)0x0)) {
    FUN_00cb0ad4();
  }
  return 0;
}

