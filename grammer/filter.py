import sys

nums = [3,5,4,8,9]
nums1 = list(filter(lambda n: n%2 != 0, nums))
nums2 = [n for n in nums if n%2 == 0]

print(nums1)
sys.stdout.write(str(nums1)+"\n")
print(nums2)
sys.stdout.write(str(nums2)+"\n")