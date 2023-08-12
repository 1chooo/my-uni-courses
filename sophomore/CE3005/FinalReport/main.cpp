#include <iostream>
#include <climits>

using namespace std;

int main(){
    int times,stage;
    cin>>times;
    int d[11][11];

    for(int b=0;b<times;b++){

        for(int c=1;c<=3;c++){
            cin>>d[0][c];
        }
        for(int c=1;c<=3;c++){
            for(int e=4;e<=6;e++){
                cin>>d[c][e];
            }
        }
        for(int c=4;c<=6;c++){
            for(int e=7;e<=9;e++){
                cin>>d[c][e];
            }
        }
        for(int c=7;c<=9;c++){
            cin>>d[c][10];
        }
        cin>>stage;

    //---------------------------------
        if(stage==1){ //stage1�ɡA���S���T��h(n)�A���̤p��
            int small;
            small=INT_MAX;
            for(int i=1;i<=3;i++){
                if(small>d[0][i]){
                    small=d[0][i];
                }
            }
            cout<<small<<endl;
        }
        if(stage==2){//stage2�ɡAS>>A>>D�BS>>A>>E...�̦������h�j�Mstage2�Ҧ����|��g(n)+h(n)�A���̤p��f(n)
            int small,temp;
            small=INT_MAX;
            for(int j=0;j<3;j++){
                temp=d[0][j+1]+min(min(d[j+1][4],d[j+1][5]),d[j+1][6]);
                if(small>temp){
                        small=temp;
                    }
            }
            cout<<small<<endl;
        }
        if(stage==3){//stage3�ɡAS>>A>>D>>G�BS>>A>>D>>H...�̦������h�j�Mstage3�Ҧ����|��g(n)+h(n)�A���̤p��f(n)
            int small,temp;
            small=INT_MAX;
            int i=0;

            for(int n=1;n<=3;n++){
                for(int j=4;j<=6;j++){
                    temp=d[0][n]+d[n][j]+ min(min(d[j][7],d[j][8]),d[j][9]);
                    if(small>temp){
                        small=temp;
                    }
                }
            }
            cout<<small<<endl;
        }
        if(stage==4||stage==5){//stage4�M5�ɡAS>>A>>D>>G>>T�BS>>A>>D>>H>>T...�̦������h�j�Mstage4�M5�Ҧ����|��g(n)+h(n)�A���̤p��f(n)
            int small,temp;
            small=INT_MAX;
            int i=0;
            for(int n=1;n<=3;n++){
                for(int j=4;j<=6;j++){
                    for(int k=7;k<=9;k++){
                        temp=d[0][n]+d[n][j]+d[j][k]+d[k][10];
                        if(small>temp){
                        small=temp;
                        }
                    }
                }
            }
            cout<<small<<endl;
        }
    }
    return 0;
}
