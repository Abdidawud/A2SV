class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans=[]
        value_dict={'1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g',
            '8':'h','9':'i','10#':'j','11#':'k','12#':'l','13#':'m',
            '14#':'n','15#':'o','16#':'p','17#':'q','18#':'r','19#':'s',
            '20#':'t','21#':'u','22#':'v','23#':'w','24#':'x','25#':'y','26#':'z'}

        i=0
        j=1
        
        if len(s)==2:
            ans.append(value_dict[s[i]])
            ans.append(value_dict[s[j]])

     

        else:
            while j<=len(s)-1:
                if j==len(s)-1:
                    ans.append(value_dict[s[i]])
                    ans.append(value_dict[s[j]])
                    i+=2
                    j+=2
                
                else:
                    if s[j+1]=='#':
                        ans.append(value_dict[s[i:j+2]])
                        i=j+2
                        j=i+1
                    else:
                        ans.append(value_dict[s[i]])
                        i+=1
                        j+=1
            if i==len(s)-1:
                ans.append(value_dict[s[i]])
                i+=1 

        return(''.join(ans))
