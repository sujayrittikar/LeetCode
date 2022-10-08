#include <bits/stdc++.h>
class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        
        for (int i=0; i<nums.size(); i++)
        {
            std::vector<int> l = std::vector<int>(nums.begin(), nums.begin()+i);
            std::vector<int> r = std::vector<int>(nums.begin()+i+1, nums.end());
            
            int lsum = accumulate(l.begin(), l.end(), 0);
            int rsum = accumulate(r.begin(), r.end(), 0);
            
            if (lsum==rsum)
                return i;
            
        }
    return -1;
    }
};