import sys

nums = [3,5,4,8,9]
nums = list(filter(lambda n: n%2 != 0, nums))

print(nums)
sys.stdout.write(str(nums))