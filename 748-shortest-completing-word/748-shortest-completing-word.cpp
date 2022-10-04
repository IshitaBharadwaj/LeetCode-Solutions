class Solution {
public:
    string shortestCompletingWord(string licensePlate, vector<string>& words) {
        int freq[26]={0};
        for(int i=0;i<licensePlate.length();i++){
            if(licensePlate[i]>=65 && licensePlate[i]<=90){
                freq[(int)licensePlate[i]-65]++;
            }
        }
        for(int i=0;i<licensePlate.length();i++){
            if(licensePlate[i]>=97 && licensePlate[i]<=122){
                freq[(int)licensePlate[i]-97]++;
            }
        }
        int min_len=20;
        string min_len_word="";
        for(int i=0;i<words.size();i++){
            if(words[i].length()<min_len){
                int check[26]={0};
                for(int j=0;j<words[i].length();j++){
                    check[(int)words[i][j]-97]++;
                }
                bool flag=true;
                for(int k=0;k<26;k++){
                    if(freq[k]>check[k]){
                        flag=false;
                        break;
                    }
                }
                if (flag==true){
                    min_len=words[i].length();
                    min_len_word=words[i];
                }
            }
        }
        return min_len_word;
        
    }
};