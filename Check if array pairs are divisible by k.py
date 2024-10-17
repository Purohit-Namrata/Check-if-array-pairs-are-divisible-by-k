from typing import List
class Solution:
    def canArrange(self,arr:List[int],k:int)->bool:
        mp=[0]*k
        for num in range(len(arr)):
            rem=(num%k)#+k)%k
            if rem<0:
                rem+=k
            mp[rem]+=1
        if(mp[0]%2!=0):
            return False
        n=int(k/2)
        for rem in range(1,n+1):
            if(k==(k-rem)):
                
                if(mp[rem]%2!=0):
                    return False
                else:
                    counterHalf=k-rem
                    if(mp[counterHalf]!=mp[rem]):
                        return False
        return True
    
s=Solution()
print(s.canArrange([10,15,20,30],5))
print(s.canArrange([1, 2, 3, 4, 5, 10, 6, 7, 8, 9], 5))
print(s.canArrange([1,2,3,4,5,6],7))
