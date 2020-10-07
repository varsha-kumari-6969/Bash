
import difflib as df

def lcs(X, Y, Z): 
    s=df.SequenceMatcher(None , X , Z)
    s1=s.get_matching_blocks(0 , len(X) , 0 , len(Z))
    for i in s1:
        if i[0]==0 and i[1]==0:
            s2=X[0:0+i[2]]
            s3=df.SequenceMatcher(None, s2, Y)
                len1=s.get_matching_blocks(0 , s1[2] , 0 , len(Y))
                for i in len1:
                    if s3[0]==0 and s3[1]==0:
                        return len1[2]
                else:
                    return 0
    else:
        return 0
T=int(input())
L=[]
ans=[]

for i in range(T):
    x=input()
    L.append(x)

S=int(input())
for i in range(S):
    s=input()
    s1=s.split(" ")
    s2=L[int(s1[0])-1]
    s3=L[int(s1[1])-1]
    s4=L[int(s1[2])-1]
    ans.append(lcs(s2,s3,s4))

for i in ans:
    print(i) 
