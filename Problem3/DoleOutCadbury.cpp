/*
21 / 11 / 2020
@author: z_tjona

Tema: 
*/

#include <iostream>
using namespace std;

/*===========================================================
DEFS
===========================================================*/

int proc(int length, int width){
    int a = length;
    int b = width;

    int r = 1;
    int s  =0;
    int q;

    while (r > 0)
    {
        q = a/b;
        r = a - b*q;
        s += q;
        a = b;
        b = r;
    }
    return s; 
}

/*===========================================================
MAIN
===========================================================*/
int main()
{
    int lMin, lMax, rMin, rMax;
    cin >> lMin;
    cin >> lMax;
    cin >> rMin;
    cin >> rMax;

    int resp = 0;
    for (int i = lMin; i <= lMax; i++)
    {
        for (int j = rMin; j <= rMax; j++)
        {
            resp += proc(i, j);
        }
    }
    cout << resp;
    return 0;
}

/*===========================================================
FUNCIONES
===========================================================*/

//===========================================================
