class Solution:
    def majorityElement(self,nums: list[int]) ->int:
        count=0
        val=0
        for num in nums:
            if count==0:
                val=num
            if num==val:
                count+=1
            else:
                count-=1
        return val
ob=Solution()
nums=[3,2,3]#just take only 2 diff values
print(ob.majorityElement(nums))