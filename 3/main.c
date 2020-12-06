#include <stdio.h>

#define WIDTH 31
#define HEIGHT 323



void readMap(char map[HEIGHT][WIDTH]) {
    int row = 0;
    int col = 0;
    char c;
    char prev; 
    

    
    c = getc(stdin);
    while(c != EOF) {
        if(c == '\n') {
            row++;
            col = 0;
        }
        else {
            map[row][col] = c;
            col++;
        }
        c = getc(stdin);
    }
}

int stepThrough(char map[HEIGHT][WIDTH], int stepX, int stepY) {

    int trees = 0;

    for(int x = 0, y = 0; y < HEIGHT; y += stepY, x += stepX) {
        if(x >= WIDTH) {
            x -= WIDTH;
        }


        if(map[y][x] == '#') trees++;

        
    }

    return trees;
}

void drawMap(char map[HEIGHT][WIDTH]) {
    for(int i = 0; i < HEIGHT; i++) {
        for(int j = 0; j < WIDTH; j++) {
            printf("%c", map[i][j]);
        }
        printf("\n");
    }
}


int main() {
  char map[HEIGHT][WIDTH];

    readMap(map);

    long long int trees = 1;
    trees *= stepThrough(map, 1, 1);
    trees *= stepThrough(map, 3, 1);
    trees *= stepThrough(map, 5, 1);
    trees *= stepThrough(map, 7, 1);
    trees *= stepThrough(map, 1, 2);

    printf("%lli\n", trees);
}

