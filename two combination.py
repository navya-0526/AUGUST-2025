class solution:
    def generate(self,ind,curr_subset,ans,candidates,target):
        if(target==0):
            ans.append(curr_subset.copy())
            return
        if(target<0 or ind == len(candidates)):
            return
        curr_subset.append(candidates[ind])
        self.generate(ind,curr_subset,ans,candidates,target-candidates[ind])
        curr_subset.pop()
        self.generate(ind+1,curr_subset,ans,candidates,target)
    def combinationsum(self,candidates:list[int], target: int) ->list[list[int]]:
        ind = 0
        curr_subset = []
        ans = []
        self.generate(ind,curr_subset,ans,candidates,target)
        return ans
ob=solution()
candidates = [2,3,6,7]
target = 7
print(ob.combinationsum(candidates,target))