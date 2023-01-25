nums = [int(i) for i in open('17 (6).txt')]
mm = min(x for x in nums if x % 43 == 0)
pairs = []
mmlast = mm % 10
for i in range(len(nums) - 1):
    factor1 = ((nums[i] + nums[i + 1]) % mm == 0)
    factor2 = nums[i] % 10 == mmlast or nums[i + 1] % 10 == mmlast
    if factor1 and not (factor2) or not (factor1) and factor2:
        pairs.append(max(nums[i], nums[i + 1]))
print(len(pairs), max(pairs))
