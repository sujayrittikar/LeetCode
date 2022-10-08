#include <map>
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        std::map<char, char> s_t;
        std::map<char, char> t_s;
        
        for (int i=0; i<s.length(); i++)
        {
            if (s_t.find(s[i]) == s_t.end() && t_s.find(t[i]) == t_s.end())
            {
                s_t.insert({s[i], t[i]});
                t_s.insert({t[i], s[i]});
            }
            
            else if ((s_t.find(s[i]) != s_t.end() && s_t[s[i]]!=t[i]) || (t_s.find(t[i]) != t_s.end() && t_s[t[i]]!=s[i]))
                return false;
 
        }
        return true;
    }
};