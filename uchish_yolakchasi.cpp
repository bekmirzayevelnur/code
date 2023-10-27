#include<bits/stdc++.h>

using namespace std;
queue< pair <pair <int,int>, vector<int> > > q;

int n,l;
int a[1010];
void print (vector<int> v)
{
  for (int i = 0;i<v.size();i++) cout << v[i] << " ";
}
void bfs ()
{
  while (!q.empty()){
    pair <pair <int,int>, vector<int> >   t;
    t = q.front();
    q.pop();
    int  p = t.first.second, ind = t.first.first;
    vector<int> w = t.second;
    if (ind == n - 1) break;
    if (p < l){
      ind++;
      pair <int, int> d1(ind,p + a[ind]),b1(ind,p);
      pair <pair <int,int>, vector<int> > b(b1,w);
      w.push_back(ind);
      pair <pair <int,int>, vector<int> > d(d1,w);
    if ( p + a[ind] == l)  {
      print(w);
      return;
    }  
    if ( p + a[ind] < l)  {
      q.push(d);
    }
    q.push(b);
      
    }
  }
  cout << "no";
}

int main()
{
  cin >> n >> l;
  for (int i = 0;i<n;i++)
  {
    cin >> a[i];
  }
  vector<int> g;
  pair <int, int> f(-1,0);
  pair <pair <int,int>, vector<int> >  d(f,g);
  
  q.push(d);
  bfs();  
}
