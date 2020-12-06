#include <stdio.h>
#include <string.h>



int readLines(char lines[][50]) {
    char buffer[50];
    int i = 0;
    while (fgets(buffer, 50, stdin) != NULL) {
        strcpy(lines[i], buffer);
        i++;
    } 
    return i;
}


int main() {
    char lines[3000][50];

    int numOfLines = readLines(lines);

    char c;
    char prev_c;
    int group = 0;
    int currentGroupMembers = 1;
    int groupMembers[3000] = {0};
    int answers[3000][122] = {0};
   
    for(int i = 0; i < numOfLines; i++) {
        for(int j = 0; lines[i][j] != '\0'; j++) {
            c = lines[i][j];

            if(c != '\n') {
                answers[group][c]++;
            }

            if(c == '\n' && prev_c != '\n') {
                currentGroupMembers++;
            }
            
            if(c == '\n' && prev_c == '\n') {
                currentGroupMembers--;
                groupMembers[group] = currentGroupMembers;
                group++;
                currentGroupMembers = 1;
            }
            
            prev_c = c;
        }    
    }
    groupMembers[group] = currentGroupMembers == 1 ? currentGroupMembers : currentGroupMembers - 1;


    int sum = 0;

    for(int i = 0; i < group + 1; i++) {
        int num = 0;
        printf("Group %i\n", i);
        for(int j = 97; j <= 122; j++) {
            printf("Members %i Question %c Answers %i\n", groupMembers[i], j, answers[i][j]);
            if(answers[i][j] == groupMembers[i]) {
                num++;
            }
        }
        printf("\n");
        sum += num;
    }
    
    printf("%i\n", sum);
}