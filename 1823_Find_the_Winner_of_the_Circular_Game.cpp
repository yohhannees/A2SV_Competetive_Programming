class Solution
{
public:
    int findTheWinner(int n, int k)
    {
        vector<int> A;
        int i = 1;
        while (i <= n)
        {
            A.push_back(i);
            i++;
        }
        int t = 0;
        while (A.size() != 1)
        {
            i = 1;

            while (i < k)
            {
                if (t >= A.size())
                {
                    t = 0;
                }
                t++;
                if (t >= A.size())
                {
                    t = 0;
                }
                i++;
            }
            A.erase(A.begin() + t);
        }
        return A[0];
    }
};