#include<bits/stdc++.h>
using namespace std;

struct Info{
    int T;//available time
    int X;//hiring cost
    int Y;//speed

    //sorts inorder of less time,greater speed,less cost
    bool operator<(Info other) const
    {
        if((T<other.T) || (T==other.T && Y>other.Y) || (T==other.T && Y==other.Y && X<other.X))
        {
            return true;
        }
        return false;
    }
};

vector<Info>::iterator it;



int main()
{
    //cout<<"hi\n";
    ifstream myfileRead;
    ofstream myfileWrite;
    long long int N, D, minimum_cost=0, area_rem, k=0;
    int real_time=1, real_cost=0, real_speed=0;

    clock_t time_req;
    time_req=clock();

    myfileRead.open("1405117_input3.txt");

    if(!myfileRead)
    {
        cout<<"Unable to read the file"<<endl;
        exit(1);
    }

    myfileRead>>N>>D;

    //cin>>N>>D;

    area_rem=D;

    vector<Info> vec;
    for(long long int i=0; i<N; i++)
    {
        Info temp;
        myfileRead>>temp.T>>temp.X>>temp.Y;

        vec.push_back(temp);

    }

    myfileRead.close();

    sort(vec.begin(), vec.end());


    /*
    for(it=vec.begin(); it!=vec.end(); it++)
    {
        cout<<"Time:"<<(*it).T<<" Cost:"<<(*it).X<<" Speed:"<<(*it).Y<<endl;
    }
    */

    while(1)
    {
        if(area_rem<=0) break;

        if(vec[k].T == real_time && vec[k].Y>real_speed)
        {
            //cout<<"hi2"<<endl;
            real_speed = vec[k].Y;
            minimum_cost = minimum_cost + vec[k].X;
        }

        while(1)
        {
            if(vec[k].T==real_time && k<N) k++;
            else break;
        }
        if(k == N) break;
        area_rem = area_rem - (real_speed*(vec[k].T - real_time));
        real_time = vec[k].T;

        //cout<<"real_time"<<real_time<<endl;
        //cout<<"rem_area"<<area_rem<<endl;

    }

    myfileWrite.open("1405117_output3.txt");
    if(!myfileWrite)
    {
        cout<<"Unable to open the output file"<<endl;
        exit(1);
    }

    time_req=(clock()-time_req)/double(CLOCKS_PER_SEC)*1000;
    myfileWrite<<minimum_cost<<" "<<time_req;
    cout<<minimum_cost<<" "<<time_req<<endl;





}



