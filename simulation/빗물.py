# https://www.acmicpc.net/problem/14719

# two pointer

n, m = map(int, input().split()) # 세로길이, 가로길이
nums = list(map(int, input().split()))

left, right = 0, len(nums)-1
left_max, right_max = nums[left], nums[right]
volume = 0
while left < right:
    left_max = max(left_max, nums[left])
    right_max = max(right_max, nums[right])

    if left_max <= right_max:
        volume += left_max - nums[left]
        left += 1
    else:
        volume += right_max - nums[right]
        right -= 1
print(volume)





