
undefined4 FBClient_onMessageReceived(int param_1)

{
  undefined4 local_10;
  undefined4 local_c;
  
  local_10 = *(undefined4 *)(param_1 + 0x50);
  local_c = *(undefined4 *)(param_1 + 0x54);
  if (*(int *)(param_1 + 0x40) != 0) {
    *(undefined1 *)(param_1 + 0x30) = 1;
  }
  (**(code **)(**(int **)(param_1 + 0x28) + 0xa0))
            (*(int **)(param_1 + 0x28),&local_10,*(undefined4 *)(param_1 + 0x58));
  return 0;
}

