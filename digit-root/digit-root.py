def find_digit_root(num):
    if num <= 9:
        return num
    else:
        return find_digit_root(sum([int(char) for char in str(num)]))

print find_digit_root(123)
