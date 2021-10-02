main()
{
  printf("This is my shell\n");
  setuid(0);
  setgid(0);
  system("/bin/dash");
}
