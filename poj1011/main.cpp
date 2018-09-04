#include <iostream>
#include <cstring>
#include <stdio.h>
#include <stdlib.h>
#include <cmath>
#include <map>
#include <algorithm>
using namespace std;

int main()
{
    char s[10];
    int n;
    while(scanf("%s%d", s, &n) != EOF){
        if(n == 0){
            printf("1\n");
            continue;
        }
        int r[10], p = 0;
        for(int i = strlen(s) - 1, j = 0; i >= 0; i--){
            if(s[i] == '.'){
                p = (strlen(s) - 1 - i) * n;
                i--;
            }
            r[j] = s[i] - '0';
            j++;
        }

        int t[1000], t_len = 5, k = 4;
        memcpy(t, r, sizeof(int) * 5);
        while(--n){
            int sum[1000] = {0};
            for(int i = 0; i < 5; i++){                           // r * t
                int temp = 0;
                k = i;
                for(int j = 0; j < t_len; j++){
                    sum[k] = r[i] * t[j] + temp + sum[k];
                    int mid_sum = sum[k];
                    if(sum[k] > 9){
                        sum[k] = sum[k] % 10;
                        temp = mid_sum / 10;
                    }
                    else
                        temp = 0;
                    k++;
                    if(k == t_len + i)
                        sum[k] = temp;
                }
            }
            for(int m = 0; m <= k; m++)
                t[m] = sum[m];
            t_len = k + 1;
        }

        int temp1 = 0, temp2 = k;
        for(int i = 0; i <= k; i++){        //去后缀
            if(t[i] != 0){
                temp1 = i;
                if(temp1 > p)
                    temp1 = p;
                break;
            }
        }
        for(int i = k; i >= 0; i--){        //去小数点前的0
            if(t[i] != 0){
                temp2 = i;
                if(p > temp2)
                    temp2 = p - 1;
                break;
            }
        }
        for(int i = temp2; i >= temp1; i--){
            if(i == p - 1)
                printf(".");
            printf("%d", t[i]);
        }
        printf("\n");
    }
	return 0;
}







