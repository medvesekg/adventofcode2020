#include <stdio.h>

int readStdin(int numbers[]);

int main() {
    const int SUM = 2020;

    int numbers[1000];

    int length = readStdin(numbers);

    for(int i = 0; i < length; i++) {
        for(int j = i + 1; j < length; j++) {
            for(int k = j + 1; k < length; k++) {
                if(numbers[i] + numbers[j] + numbers[k] == SUM) {
                    printf("%i\n", numbers[i] * numbers[j] * numbers[k]);
                } 
            }
            
        }
    }

    return 0;
}

int readStdin(int numbers[]) {
    int num;
    int i = 0;

    while (scanf("%d", &num) == 1) {
        numbers[i] = (int) num;
        i++;
    }

    return i;
}