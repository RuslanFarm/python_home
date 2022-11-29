with open('4414.txt') as f:
    nums = [int(_) for _ in f.readlines()]
    pairs = 0
    maxrazn = -999999999
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if ((nums[i] - nums[j]) % 36 == 0 and (nums[i] % 13 == 0 or nums[j] % 13 == 0)):
                pairs += 1
                maxrazn = max(maxrazn, nums[i] - nums[j])
    print(pairs, maxrazn)
