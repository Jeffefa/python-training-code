def rotate(nums, k) -> list:
    k = k % len(nums)
    return nums[-k:] + nums[:-k]

# Example usage:
nums = [1, 2, 3, 4, 5, 6]
k = 2
rotated_list = rotate(nums, k)
print(rotated_list)  # Output: [5, 6, 1, 2, 3, 4]