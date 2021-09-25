#include <stdio.h>
void func(void)
{
  int a  = 0;
  char buf [12];
  int b = 1;

  gets(buf);
}
int main (int argc, char ** argv)
{
  func();
  printf("Function called\n");
}
