#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int main ( void ) 
{
    char choice = '0';

    printf("Installing dependencies\n");
    system("pip install -r requirements.txt > out.log");

    printf("Select:\n \t(B) Build\n \t(R) Run\n");
    while (choice != 'B' && choice != 'R') {
        scanf("%c", &choice);
    }
    
    if (choice == 'B') {
        printf("Building Simulation.exe");
        system("pyinstaller Simulation.spec");
        printf("Cleaning up....\n");
        system("rm -rf build || RD /S /Q build");
        system("rm out.log || del out.log");
        printf("Build complete!, Simulation.exe is included in ./dist directory");
    } else if (choice == 'R') {
        system("rm out.log || del out.log");
        system("python Simulation.py");
    }

    return 0;
}