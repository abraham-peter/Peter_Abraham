#include <stdio.h>
#include <stdlib.h>

void unitati(int x) {
    switch (x) {
        case 1: printf("unu"); break;
        case 2: printf("doi"); break;
        case 3: printf("trei"); break;
        case 4: printf("patru"); break;
        case 5: printf("cinci"); break;
        case 6: printf("sase"); break;
        case 7: printf("sapte"); break;
        case 8: printf("opt"); break;
        case 9: printf("noua"); break;
    }
}

void sprezece(int x) {
    switch (x) {
        case 10: printf("zece"); break;
        case 11: printf("unsprezece"); break;
        case 12: printf("doisprezece"); break;
        case 13: printf("treisprezece"); break;
        case 14: printf("paisprezece"); break;
        case 15: printf("cincisprezece"); break;
        case 16: printf("saisprezece"); break;
        case 17: printf("saptesprezece"); break;
        case 18: printf("optsprezece"); break;
        case 19: printf("nouasprezece"); break;
    }
}

void zeci(int x) {
    int z = x / 10;
    int u = x % 10;
    switch (z) {
        case 2: printf("douazeci"); break;
        case 3: printf("treizeci"); break;
        case 4: printf("patruzeci"); break;
        case 5: printf("cincizeci"); break;
        case 6: printf("saizeci"); break;
        case 7: printf("saptezeci"); break;
        case 8: printf("optzeci"); break;
        case 9: printf("nouazeci"); break;
    }
    if (u != 0) {
        printf(" si ");
        unitati(u);
    }
}

void sute(int x) {
    int s = x / 100;
    int rest = x % 100;

    if (s == 1) {
        printf("o suta");
    } else {
        unitati(s);
        printf(" sute");
    }

    if (rest != 0) {
        printf(" ");
        if (rest < 10)
            unitati(rest);
        else if (rest < 20)
            sprezece(rest);
        else
            zeci(rest);
    }
}

void mii(int x) {
    int m = x / 1000;
    int rest = x % 1000;

    if (m == 1) {
        printf("o mie");
    } else {
        if (m < 10)
            unitati(m);
        else if (m < 20)
            sprezece(m);
        else if (m < 100)
            zeci(m);
        else
            sute(m);
        printf(" mii");
    }

    if (rest != 0) {
        printf(" ");
        if (rest < 10)
            unitati(rest);
        else if (rest < 20)
            sprezece(rest);
        else if (rest < 100)
            zeci(rest);
        else
            sute(rest);
    }
}

void nume_numar(int x) {
    if (x == 0) {
        printf("zero");
    } else if (x < 10) {
        unitati(x);
    } else if (x < 20) {
        sprezece(x);
    } else if (x < 100) {
        zeci(x);
    } else if (x < 1000) {
        sute(x);
    } else if (x < 1000000) {
        mii(x);
    } else {
        printf("un milion");
    }
}

int main() {
    int x;
    scanf("%d", &x);
    nume_numar(x);
    return 0;
}

