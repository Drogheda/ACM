#include <stdio.h>
#include <iostream>
#include <string.h>
#include <algorithm>
#include <stdlib.h>
#include <cstring>

using namespace std;
string Haab[] = {"pop", "no", "zip", "zotz", "tzec", "xul", "yoxkin", "mol", "chen", "yax", "zac", "ceh", "mac", "kankin", "muan", "pax", "koyab", "cumhu", "uayet"};
string Holly[] = {"imix", "ik", "akbal", "kan", "chicchan", "cimi", "manik", "lamat", "muluk", "ok", "chuen", "eb", "ben", "ix", "mem", "cib", "caban", "eznab", "canac", "ahau"};
int main()
{
   int n, day, year;
   string month;
   scanf("%d", &n);
   printf("%d\n", n);
   while(n--){
       scanf("%d", &day);
       getchar();
       cin >> month >> year;
       int i, sum = 0;
       for(i = 0; i < 19; i++)
          if(Haab[i] == month)
              break;
       sum = (year * 365) + (i * 20) + day;
       year = sum / 260;
       month = Holly[sum % 20];
       day = sum % 13 + 1;
       cout << day << " " << month << " " << year << endl;
   }
    return 0;
}























