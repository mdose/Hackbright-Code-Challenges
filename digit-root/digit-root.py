def find_digit_root(num):
    if num <= 9:
        return num
    else:
        return find_digit_root(sum([int(char) for char in str(num)]))

# print find_digit_root(123)

nums = [20, 13, 4, 1111, 17]
sorted_nums = sorted(nums)
print sorted(sorted_nums, key=lambda num: find_digit_root(num))

 # NOTE: when do complex sorting by more than one factor, is works backwards to
 # how you would do it in English. Ex. Sort by regular nums first (to make sure
 # 4 comes before 13;this is called stable sorting), THEN sort by the digit root
 # using lambda (it would be the opposite via normal intution)
