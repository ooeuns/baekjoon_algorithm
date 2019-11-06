#include <bits/stdc++.h>
#define INF 0x3f3f3f3f
using namespace std;
int a[105][105],flag[105];
int main()
{
        int n,m;
        while(~scanf("%d%d",&n,&m))
        {
            for(int i=1;i<=n;i++)
                for(int j=1;j<=n;j++)
                    scanf("%d",&a[i][j]);

            memset(flag,INF,sizeof(flag));
            queue <int> q;
            q.push(m);
            flag[m]=0;
            while(!q.empty())
            {
                m=q.front(); q.pop();
                for(int i=1;i<=n;i++)
                    if(a[m][i]==1&&flag[i]==INF)
                    {
                        flag[i]=flag[m]+1;
                        q.push(i);
                    }
            }

            int sign=0;
            for(int i=0;i<n;i++)
            {
                sign=0;
                for(int j=1;j<=n;j++)
                    if(flag[j]==i)
                    {
                        if(sign==0)
                        {
                            printf("%d",j);
                            sign=1;
                        }
                        else printf(" %d",j);
                    }
                if(sign==1) printf("\n");
            }

        }

        return 0;
}