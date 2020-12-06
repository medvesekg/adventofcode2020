#include <stdio.h>
#include <string.h>

#define ROWS 128
#define COLUMNS 8



int readInput(char lines[1000][50]) {

    char buffer[50];

    int i = 0;
    while(scanf("%s", buffer) != EOF) {
        strcpy(lines[i], buffer);
        i++;
    }

    return i;


}

int findRow(char line[]) {
    char c;
    int min = 0;
    int max = ROWS - 1;
    int rows = ROWS;

    for(int i = 0; i < 7; i++) {
        c = line[i];
        if(c == 'F') {
            rows /=2;
            max -= rows;
        }
        else if(c == 'B') {
            rows /=2;
            min += rows;

        }
    }
    return min;
}

int findColumn(char line[]) {
    char c;
    int min = 0;
    int max = COLUMNS - 1;
    int columns = COLUMNS;

    for(int i = 7; i < 10; i++) {
        c = line[i];
        if(c == 'L') {
            columns /=2;
            max -= columns;
        }
        else if(c == 'R') {
            columns /=2;
            min += columns;

        }
    }

    return min;
}

int findSeatId(int row, int column) {
    return (row * 8) + column;
}


int main() {
  char lines[1000][50];
  int numOfLines = readInput(lines);

  int seats[ROWS][COLUMNS] = {0};

  int highestId = 0;

  for(int i = 0; i < numOfLines; i++) {
    int row = findRow(lines[i]);
    int column = findColumn(lines[i]);
    int seatId = findSeatId(row, column);
    //printf("%s row %i, column %i, seat ID %i\n", lines[i], row, column, seatId);

    seats[row][column] = 1;

    if(seatId > highestId) {
        highestId = seatId;
    }
  }

  printf("Highest seat id: %i\n", highestId);

  int firstSeat = 0;
  int stop = 0;
  for(int i = 0; i < ROWS; i++) {
      for(int j = 0; j < COLUMNS; j++) {
          if(!firstSeat && seats[i][j] == 1) {
              firstSeat = 1;
          }

          if(firstSeat && seats[i][j] != 1) {
              printf("Your seat is in row %i, column %i, seat ID %i\n", i, j, findSeatId(i, j));
              stop = 1;
              break;
          }
      }
      if(stop) {
          break;
      }
  }
}
