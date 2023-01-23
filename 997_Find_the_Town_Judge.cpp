
class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
     vector<vector<int> >A(n+1,vector<int>(n+1,0));
        int ans=-1;
        for(int i=0;i<trust.size();i++)
        {
            A[trust[i][0]][trust[i][1]]=1;
        }
        for(int i=1;i<n+1;i++)
        {
            int count=0;
            for(int j=1;j<(n+1);j++)
            {
                if(A[i][j]==0)
                {
                    count++;
                }
                else
                {
                    break;
                }
            }
            if(count==n)
            {
                ans=i;
                break;
            }
        }
        if(ans!=-1)
        {
            for(int i=1;i<n+1;i++)
            {
                if(i!=ans &&  A[i][ans]!=1)
                {
                    return -1;
                }
            }
        }
        return ans;
    }
};
