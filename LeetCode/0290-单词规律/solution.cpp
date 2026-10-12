#include <string>
#include <vector>
#include <sstream>
#include <unordered_map>
using namespace std;

class Solution{
public:
    bool wordPattern(string pattern, string s){
        vector<string> words;
        istringstream iss(s);
        string w;
        while(iss >> w){
            words.push_back(w);
        }
        
        if(pattern.size() != words.size()){
            return false;
        }

        unordered_map<char,string> p2w;
        unordered_map<string,char> w2p;

        for(size_t i = 0; i < pattern.size();++i){
            char c = pattern[i];
            const string& word = words[i];

            if(p2w.count(c) && p2w[c] != word){
                return false;
            }
            if(w2p.count(word) && w2p[word] != c){
                return false;
            }

            p2w[c] = word;
            w2p[word] = c;
        }

        return true;
    }
};
