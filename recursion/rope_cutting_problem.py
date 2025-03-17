""" ROPE CUTTING PROBLEM """
#given a rope of length n,
# you need to find the maximum number of pieces you can 
# make such that the length of every piece is in set {a,b,c}
# for the given three values a,b,c

def max_cuts(n,a,b,c):#recursion
    "using the recursion O(n^3) exponetial time complexity"
    if n==0:
        return 0
    if n<0:
        return -1
    res=max(max_cuts(n-a,a,b,c),
            max_cuts(n-b,a,b,c),
            max_cuts(n-c,a,b,c))
    return res+1 if res !=-1 else -1

def max_cuts_memo(n,a,b,c,dp):#memoization
    "using dp memoization O(n) time complexity"
    if n==0:
        return 0
    if n<0:
        return -1
    if dp[n] != -1:
        return dp[n]
    res=max(max_cuts_memo(n-a,a,b,c,dp),
            max_cuts_memo(n-b,a,b,c,dp),
            max_cuts_memo(n-c,a,b,c,dp))
    dp[n]=res+1 if res !=-1 else -1
    return dp[n]

def max_cuts_BU(n,a,b,c):#bottom-up-approach
    "bottom-up-approach O(n) time complexity"
    dp=[-1]*(n+1)
    dp[0]=0
    for i in range(1,n+1):
        if i>=a and dp[i-a]!=-1:
            dp[i]=max(dp[i],dp[i-a]+1)

        if i>=b and dp[i-b]!=-1:
            dp[i]=max(dp[i],dp[i-b]+1)

        if i>=c and dp[i-c]!=-1:
            dp[i]=max(dp[i],dp[i-c]+1)

    return dp[n] if dp[n] != -1 else 0


print("recursion:")
print(max_cuts(5,2,5,1))
print("DP memoization:")
n=5
dp=[-1]*(n+1)
print(max_cuts_memo(n,2,5,1,dp))
print("dp bottom-up:")
print(max_cuts_BU(5,2,5,1))