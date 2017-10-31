def find_digit_root(num):
    if num <= 9:
        return num
    else:
        return find_digit_root(sum([int(char) for char in str(num)]))

# print find_digit_root(123)

nums = [20, 13, 4, 1111, 17]
sorted_nums = sorted(nums)
print sorted(sorted_nums, key=lambda num: find_digit_root(num))
