class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        arr  = []
        for index, num in enumerate(nums):
            complement = target - num
            if complement in my_map:
                arr.append(my_map[complement])
                arr.append(index)
                #return(my_map[complement], index)
            my_map[num] = index
        return arr