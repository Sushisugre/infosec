#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){

char* p = getenv("SHELL");
printf("address of SHELL %p\n", p);

return 0;
}
