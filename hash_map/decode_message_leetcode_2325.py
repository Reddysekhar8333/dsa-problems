dici={}
key="the quick brown fox jumps over the lazy dog"
'''
temp=1
for i in key:
    if i!=" " and i not in dici:
        dici[i]=temp
        temp+=1
print(dici)
'''
dic=dict()
tmp=97
#print("\n")
for i in key:
    if i!=" " and i not in dic:
        dic[i]=chr(tmp)
        tmp+=1
print(dic)
message = "vkbs bs t suepuv"
ans=""
for i in message:
    if i==" ":
        ans+=" "
    else:
        ans+=dic[i]
print(ans)



    

