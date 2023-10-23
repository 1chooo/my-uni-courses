#include <iostream>
using namespace std;

int main(){
for (int i = 2, j = 1;j < 10;(i==9)?(i=(++j/j)+1):(i++))
{ 
 
int tmp = i * j; 
cout << i << "*" << j; 
cout << ((tmp>=10)? "=": "= ") ; 
if(i == 9){cout << i*j << endl;} //hi
else
{ {
 cout << i*j << " "; }

}
} 
 
return 0;
}