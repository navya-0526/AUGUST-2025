#majority element 229
class Solution:
    def majorityElement(self,  nums: list[int]) ->list[int]:
        if not nums:
            return[]
        c1=c2=0
        val1=val2=None
        for num in nums:
            if num==val1:
                c1+=1
            elif num==val2:
                c2+=1
            elif c1==0:
                val1=num
                c1=1
            elif c2==0:
                val2=num
                c2=1
            else:
                c1-=1
                c2-=1
        arr=[]
        n=len(nums)
        if nums.count(val1)>n//3:
            arr.append(val1)
        if nums.count(val2)>n//3:
            arr.append(val2)
        return arr
obj=Solution()
print(obj.majorityElement([0,0,0]))
