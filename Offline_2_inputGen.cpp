#include<bits/stdc++.h>
using namespace std;

int main(){
    ofstream myfile;
    myfile.open("input7.txt");

    int n=10000000;
    int mod=99;
    int mod2=545;
    myfile<<n<<" "<<356788899<<"\n";

    srand(time(0));
    for(int i=0; i<n; i++)
    {
        int x = (rand()%mod)+1;
        int y= rand();
        int z=(rand()%mod2)+1;

        myfile<<x<<" "<<y<<" "<<z<<endl;
    }
    myfile.close();
}
