def checkSum(a, b, c):
        return (a + b + c)



class Solution:


    def threeSum(self, nums: List[int]) -> List[List[int]]:


        result_list = []
        nums.sort()

        if len(nums) < 1:
            return result_list

        if len(nums) > 3000:
            return result_list

        for i, a in enumerate(nums):

            if i > 0 and a == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = a + nums[left] + nums[right]
                if total > 0:
                    right -= 1

                elif total < 0:
                    left += 1

                else:
                    temp_list = [a, nums[left], nums[right]]
                    result_list.append(temp_list)
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1


        return result_list
                    
