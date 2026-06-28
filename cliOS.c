/* 
   cliOS PRE-ALPHA BUILD
   copyleft 2026 driswillis156 & pizzawizard32
   
   license: just do whatever you want with my code, 
   but keep the credits intact, yeah thats it lol.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    int choice;

     printf("===== ###  #     #   ##     ## =====\n");
     printf("=====#     #     #  #  #   #=====\n");
     printf("=====#     #     #  #  #   #=====\n");
     printf("===== ###  # #   #   ##  ##===== \n");
     printf("  \n");
     printf("==cliOS PRE-ALPHA TEST===\n");
     printf("=======by driswillis=====\n");
     printf("==choose an application==\n");
     printf(" 1. CLIwrite (W.I.P)\n");
     printf(" 2. CLIpaint (W.i.P)\n");
     printf(" 3. CLIsnake (could be unstable)\n");
     printf(" ===more are coming out soon, so yeah, just.. dont use this OS mainstream lol=== \n");
     printf(" ===MISC: type 4 to open cyniz 404 bot (NEEDS PYTHON3 FOR THE CODE TO WORK)=== \n)");
     printf(" anyways type your choice here: ");

     scanf("%d", &choice);

     if (choice == 1) {
         char c;
         printf(" ====CLIwrite==== \n");
         printf(" press ctrl+c to exit\n");

         while ((c = getchar()) != '\n' && c != EOF);

         while (1) {
             c = getchar();
             putchar(c);
         }
     }
     else if (choice == 2) {
     printf(" === CLIpaint not added yet=== \n");
     }
     else if (choice == 3) {
     printf(" === CLIsnake not added yet === \n");
     }
    else if (choice == 4) {
        char name[50];
        char command[100];

        printf("\n--- CYNIZ 404 by driswillis and pizzawizard32 ---\n");
        printf("WHAT'S YOUR NAME.: ");

        while (getchar() != '\n');
        fgets(name, sizeof(name), stdin);
        name[strcspn(name, "\n")] = 0;

        snprintf(command, sizeof(command), "python3 cyniz404.py \"%s\"", name);
        system(command);
    }

     return 0;
}
