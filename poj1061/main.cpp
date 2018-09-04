#include <iostream>
#include <cstring>
#include <stdio.h>
#include <stdlib.h>
#include <cmath>
#include <map>
#include <algorithm>
using namespace std;

long long gcd(long long a, long long b)
{
    return (a % b) ? gcd(b, a % b) : b;
}
void exgcd(long long a, long long b, long long &d, long long &x, long long &y)
{
    if(!b){ d = a; x = 1; y = 0; }
    else{ exgcd(b, a % b, d, y, x); y -= x * (a / b); }
}

int main()
{
    long long x, y, m, n, L, a, b, c, d, X, Y, r, t;
    while(cin >> x >> y >> m >> n >> L){
        a = n - m;
        b = L;
        c = x - y;
        d = gcd(a, b);
        if(c % d)
            cout << "Impossible" << endl;
        a = a / d;
        b = b / d;
        c = c / d;
        exgcd(a, b, r, X, Y);
        t = c * X / b;
        X = c * X - t * b;
        if(X < 0)
            X += b;
        cout << X <<endl;
    }
	return 0;
}







