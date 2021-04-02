class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        nums1_size = len(nums1)
        nums2_size = len(nums2)
        total_size = nums1_size + nums2_size
        result = [None] * total_size

        #nums 1
        i = 0
        #nums 2
        j = 0
        k = 0

        while i < nums1_size and j < nums2_size:
            if nums1[i] < nums2[j]:
                result[k] = nums1[i]
                i += 1
                k += 1

            else:
                result[k] = nums2[j]
                j += 1
                k += 1


        while i < nums1_size:
            result[k] = nums1[i]
            i += 1
            k += 1

        while j < nums2_size:
            result[k] = nums2[j]
            j += 1
            k += 1

        print(result)
        result_len = len(result)

        # Even number of elements, 2 mid points
        if result_len % 2 == 0:
            left = int((result_len/2) - 1)
            right = int(result_len/2)
            print("left", left)
            print("right", right)
            median = (result[left] + result[right]) / 2
            #print(median)

        else:
            mid = int((result_len - 1) / 2)
            #print(mid)
            median = result[mid]

        return median
