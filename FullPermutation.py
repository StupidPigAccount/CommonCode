From: https://blog.csdn.net/qq_31601743/article/details/82053201
# 全排列 Python
def permutation(nums, start, end):
  if start == end:
    # 打印排列结果
    print(nums)
  else:
    for i in range(len(nums)):
      nums[i], nums[start] = nums[start], nums[i]
      permutation(nums, start + 1, end)
      nums[i], nums[start] = nums[start], nums[i]
