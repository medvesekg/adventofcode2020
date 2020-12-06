#include <stdio.h>
#include <string.h>
#include <stdlib.h>


struct Definition {
    int min;
    int max;
    char letter;
    char password[50];
};



int readLinesFromStdin(char array[][50]) {
   
    char buffer[50];
    int i = 0;
    
    while(fgets(buffer, 50, stdin) != NULL) {
        strcpy(array[i], buffer);
        i++;
    }

    return i;
}

void parseLines(char lines[][50], int numOfLines, struct Definition definitions[1000]) {
   
   char *ptr;
   
    for(int i = 0; i < numOfLines; i++) {
        struct Definition definition;
        
        char max[5];
        char min[5];
        char c[2];
        char password[50];

        int j = 0, k = 0, l = 0, m = 0;

    	for(; lines[i][j] != '-'; j++) {
            min[j] = lines[i][j];
        }
        
        min[j] = '\0';
        j++;

        for(; lines[i][j+k] != ' '; k++) {
            
            max[k] = lines[i][j+k];
        }
        max[k] = '\0';
        k++;

        

        for(; lines[i][j+k+l] != ':'; l++) {
            c[l] = lines[i][j+k+l];
        }
        c[l] = '\0';
        l += 2;

        for(; lines[i][j+k+l+m] != '\n'; m++) {
            password[m] = lines[i][j+k+l+m];
        }
        password[m] = '\0';
        m++;
            
        definition.max = atoi(max);
        definition.min = atoi(min);
        definition.letter = c[0];
        strcpy(definition.password, password);

        definitions[i] = definition;

    }
}

int validPasswords1(struct Definition definitions[1000], int numOfLines) {
    int valid = 0;

    for(int i = 0; i < numOfLines; i++) {
        struct Definition definition = definitions[i];
        char * password = definition.password;
        int letterCount = 0;
        char letter = definition.letter;
        for(int j = 0; password[j] != '\0'; j++) {
            if(password[j] == letter) {
                letterCount++;
            }
        }
        if(letterCount >= definition.min && letterCount <= definition.max) {
            valid++;
        }
    }

    return valid;
}

int validPasswords2(struct Definition definitions[1000], int numOfLines) {
    int valid = 0;

    for(int i = 0; i < numOfLines; i++) {
        struct Definition definition = definitions[i];
        char * password = definition.password;
        char letter = definition.letter;

        int first = password[definition.min - 1] == letter;
        int second = password[definition.max - 1] == letter;

        if(first ^ second) {
            valid++;
        }
    }

    return valid;
}


int main() {

    if(0 ^ 1) {
        printf("YES\n");
    }
    else {
        printf("NO\n");
    }

    char lines[1000][50];
    struct Definition definitions[1000];
    int numOfLines;

    numOfLines = readLinesFromStdin(lines);
    
    parseLines(lines, numOfLines, definitions);

    int valid = validPasswords2(definitions, numOfLines);

    printf("%i\n", valid);

    return 0;
}