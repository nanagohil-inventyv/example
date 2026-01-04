#include <iostream>
#include <bits/stdc++.h>
#include <fstream>
using namespace std;
typedef long long ll;

void solve()
{
    ifstream file("input.txt");
    if (!file)
    {
        cout << "File not found!" << endl;
        return;
    }
    string diranddis;
    int dial = 50;
    int password = 0;
    while (file >> diranddis)
    {
        string direction = diranddis.substr(0, 1);
        int distance = stoi(diranddis.substr(1));
        if (direction == "L")
        {
            dial -= distance;

            if (dial < 0)
            {
               
                dial = (dial  + 100) % 100;
                
                if(dial >= 1 && dial <= 99)
                    password++;
                else if(dial == 0){
                    password++;
                }
                
            }
        }
        else
        {
            dial += distance;

            if (dial > 99)
            {

                dial %= 100;
                if(dial >= 1)
                    password++;
                else if(dial == 0){
                    password++;
                }
            }
        }
        // if( dial == 0){
        //     password++;
        // }
        
    }

    cout << "password " << password << endl;
}
int main()
{

    // int t;
    // cin >> t;
    // while (t--)
    solve();
    return 0;
}