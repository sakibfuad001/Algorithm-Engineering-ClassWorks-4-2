#include<bits/stdc++.h>
using namespace std;

struct Edge{
    char first;
    char second;
    int stageNo;
    int fuelCost;
    int hotelCost;
};
map<char, int> distancemap;
map<char, char> parent;
map<char, char>::iterator parent_it;
map<char, int>::iterator dist_it;
vector<Edge> vec;
vector<Edge>::iterator it;



void printPath(char ch)
{
    if(parent[ch]=='1')
    {
        cout<<ch<<"-->";
        return;
    }
    printPath(parent[ch]);
    cout<<ch<<"-->";
}

void Dijkstra(char source){

    priority_queue<char> Q;
    char first;
    Q.push(source);
    distancemap[source]=0;
    parent[source]='1';
    while(!Q.empty())
    {
       first = Q.top();
       Q.pop();

        for(it=vec.begin(); it!=vec.end(); it++)
        {
            if((*it).first==first)
            {
                if(distancemap[first]+(*it).fuelCost+(*it).hotelCost < distancemap[(*it).second])
                {
                    distancemap[(*it).second]=distancemap[first]+(*it).fuelCost+(*it).hotelCost;
                    Q.push((*it).second);
                    parent[(*it).second]=(*it).first;
                }
            }
        }
    }

}

void init(int n)
{
    char ch='a';
    distancemap['s']=1000000;
    for(int i=0; i<n-1; i++)
    {

        //distancemap.insert(pair<char,int>(ch,1000000));
        distancemap[ch]=1000000;
        //cout<<ch<< " "<<distancemap[ch]<<endl;
        ch=ch+1;

    }

}
int main()
{



    ifstream myfile;
    myfile.open("1405117_input.txt");
    long long stage, edgeNo,nodeNo, minCost=10000000;
    if(!myfile)
    {
        cout<<"Unable to read the file"<<endl;
        exit(1);
    }
    myfile>>stage>>nodeNo>>edgeNo;

    init(nodeNo);
    for(int i=1; i<=edgeNo; i++)
    {
        Edge edge;
        myfile>>edge.first>>edge.second>>edge.stageNo>>edge.fuelCost>>edge.hotelCost;
        vec.push_back(edge);
        //cout<<edge.first<<" "<<edge.second<<" "<<edge.stageNo<<" "<<edge.fuelCost<<" "<<edge.hotelCost<<endl;
    }

//    for(it=vec.begin(); it!=vec.end(); it++)
//    {
//        cout<<(*it).first<<" "<<(*it).second<<endl;
//    }

    myfile.close();

    Dijkstra('s');

    //prints minimum distances
//    for(dist_it=distancemap.begin(); dist_it!=distancemap.end(); dist_it++)
//    {
//        cout<<(*dist_it).first<<" "<<(*dist_it).second<<endl;
//    }

    char finalMinDest;
    for(int i=0; i<vec.size(); i++)
    {
        if(vec[i].stageNo==stage)
        {
            if(minCost>distancemap[vec[i].second])
            {
                minCost=distancemap[vec[i].second];
                finalMinDest=vec[i].second;
                //cout<<minCost<<endl;
            }
        }
    }

    cout<<"--------------***ROUTE***-------------"<<endl;
    printPath(parent[finalMinDest]);
    cout<<finalMinDest<<endl<<endl;
    cout<<"Minimum Cost: "<<minCost<<endl;

    //printing shortest path


    return 0;
}
