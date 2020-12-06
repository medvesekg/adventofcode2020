#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Passport {
    char* byr;
    char* iyr;
    char* eyr;
    char* hgt;
    char* hcl;
    char* ecl;
    char* pid;
    char* cid;
};

struct KeyValue {
    char * key;
    char * value;
};

char * getFieldName(char * c) {

    *c = getc(stdin);

    if(*c == '\n' || *c == EOF) {
        return NULL;
    }
    else {
        char* field = malloc(4 * sizeof(char));

        field[0] = *c;
        field[1] = getc(stdin);
        field[2] = getc(stdin);
        field[3] = '\0';

        *c = field[2];

        return field;
    }
}

char * getFieldValue(char * c) {
    char* value = malloc(10 * sizeof(char));
    int i = 0;
    while(1) {
        *c = getc(stdin);
        if(*c != '\n' && *c != ' ') {
            value[i] = *c;
            i++;
        } else {
            break;
        }
        
    } 

    return value;
}

struct KeyValue getField(char * c) {
    struct KeyValue keyValue;
    keyValue.key = NULL;
    keyValue.value = NULL;

    char * key = getFieldName(c);
    if(key == NULL) {
        return keyValue;
    }

    keyValue.key= key;
    getc(stdin);
    keyValue.value = getFieldValue(c);

    return keyValue;
}


char * loadPassports() {
    
    char* passports = malloc(100000 * sizeof(char));

    char c;
    int i = 0;
    do {
        c = getc(stdin);
        passports[i] = c;
        i++;

    } while(c != EOF);

    passports[i] = '\0';

    return passports;
        
}


int readPassports(struct Passport * passports) {
    char c;
    
    struct Passport passport = {.byr = NULL, .iyr = NULL, .eyr = NULL, .hgt = NULL, .ecl = NULL, .pid = NULL, .cid = NULL};
    int i = 0;

    while(c != EOF) {
        struct KeyValue k = getField(&c);

        if(k.key == NULL) {
            passports[i] = passport;
            passport.byr = NULL;
            passport.iyr = NULL;
            passport.eyr = NULL;
            passport.hgt = NULL;
            passport.hcl = NULL;
            passport.ecl = NULL;
            passport.pid = NULL;
            passport.cid = NULL;
            i++;
        }
        else if(strcmp(k.key, "byr") == 0) {
            passport.byr = k.value;
        }
        else if(strcmp(k.key, "iyr") == 0) {
            passport.iyr = k.value;
        }
        else if(strcmp(k.key, "eyr") == 0) {
            passport.eyr = k.value;
        }
        else if(strcmp(k.key, "hgt") == 0) {
            passport.hgt = k.value;
        }
        else if(strcmp(k.key, "hcl") == 0) {
            passport.hcl = k.value;
        }
        else if(strcmp(k.key, "ecl") == 0) {
            passport.ecl = k.value;
        }
        else if(strcmp(k.key, "pid") == 0) {
            passport.pid = k.value;
        }
        else if(strcmp(k.key, "cid") == 0) {
            passport.cid = k.value;
        }
    }

    return i;
}

int validateByr(char * byr) {
    if (byr == NULL) return 0;

    int i_byr = atoi(byr);
    return i_byr >= 1920 && i_byr <= 2002;
}

int validateIyr(char * iyr) {
    if (iyr == NULL) return 0;

    int i_iyr = atoi(iyr);
    return i_iyr >= 2010 && i_iyr <= 2020;
}

int validateEyr(char * eyr) {
    if (eyr == NULL) return 0;

    int i_eyr = atoi(eyr);
    return i_eyr >= 2020 && i_eyr <= 2030;
}

int validateHgt(char * hgt) {
    if(hgt == NULL) return 0;

    int height;
    char unit[3];

    sscanf(hgt, "%i%s", &height, unit);
    if(strcmp(unit, "cm") == 0) {
        return height >= 150 && height <= 193;
    }
    else if(strcmp(unit, "in") == 0 ){
        return height >= 59 && height <= 76;
    }


    return 0;
}

int validateHcl(char * hcl) {
    if (hcl == NULL) return 0;

    char string[7] = {'#'};
    sscanf(hcl, "#%s", string);
    for(int i = 0; i < 6; i++) {
        if(!(string[i] >= 97 && string[i] <= 102) && !(string[i] >= 48 && string[i] <= 57)) {
            return 0;
        }
    }

    return 1;
}

int validateEcl(char * ecl) {
    if (ecl == NULL) return 0;
    
    char valid[7][4] = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"};
    for(int i = 0; i < 7; i++) {
        if(strcmp(ecl, valid[i]) == 0) {
            return 1;
        }
    }
    return 0;
}

int validatePid(char * pid) {
    if(pid == NULL) return 0;

    for(int i = 0; i < 9; i++) {
        if(!(pid[i] >= 48 && pid[i] <= 57) ) {
            return 0;
        }
    }
    if(pid[9] != '\0') return 0;
    return 1;
}


int main() {
    struct Passport * passports = malloc(1000 * sizeof(struct Passport));
    struct Passport passport;
    int numOfPassports = readPassports(passports);
    int valid = 0;

    for(int i=0; i < numOfPassports; i++) {
        passport = passports[i];
        if(validateByr(passport.byr) && 
            validateIyr(passport.iyr) && 
            validateEyr(passport.eyr) && 
            validateHgt(passport.hgt) && 
            validateHcl(passport.hcl) && 
            validateEcl(passport.ecl) && 
            validatePid(passport.pid)) {            
                valid++;
        }
    }
    printf("Valid: %i Total: %i\n", valid, numOfPassports);
}



