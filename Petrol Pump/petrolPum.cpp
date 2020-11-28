/*
27 / 11 / 2020
@author: z_tjona

Tema: ckk implementation
*/

#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <cmath>
using namespace std;

/*===========================================================
DEFS
===========================================================*/
int ckk(vector<int> nums);

void printVector(const vector<int> &vals)
{
    for (auto i = vals.begin(); i != vals.end(); ++i)
        cout << *i << " ";

    cout << endl;
}

/*===========================================================
MAIN
===========================================================*/
int main()
{
    string line = "";

    getline(cin, line);

    stringstream ss(line);

    string word; // for storing each word

    vector<int> valores;
    while (ss >> word)
    {
        int val = stoi(word);   // a entero
        valores.push_back(val); // en vector
    }

    // sort vector
    sort(valores.begin(), valores.end());

    // printVector(valores);
    const int sum = accumulate(valores.begin(), valores.end(), 0);

    int diff = ckk(valores);
    // cout << diff;

    int resp = (sum - diff) / 2 + diff;
    cout << resp;

    return 0;
}

/*===========================================================
FUNCIONES
===========================================================*/
int ckk(vector<int> nums)
{
    if (nums.size() == 0)

        return 0;
    else if (nums.size() == 1)
        return nums[0];

    // else
    int bigger = nums.back();
    nums.pop_back();
    int secondBigger = nums.back();
    nums.pop_back();

    vector<int> lLeft(nums);
    vector<int> lRight(nums);

    int dif = bigger - secondBigger;
    if (dif > 0)
    {
        lLeft.push_back(dif);
        sort(lLeft.begin(), lLeft.end());
    }

    lRight.push_back(bigger + secondBigger);

    // printVector(lLeft);
    // printVector(lRight);

    int rL = ckk(lLeft);
    int rR = ckk(lRight);
    if (rL < rR)
        return rL;
    else
        return rR;
}
//===========================================================