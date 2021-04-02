class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        num_length = 2*n
        my_arr = []

        for i in range(0, int(num_length/2)):
            my_arr.append(nums[i])
            my_arr.append(nums[n+i])

        return my_arr


        
