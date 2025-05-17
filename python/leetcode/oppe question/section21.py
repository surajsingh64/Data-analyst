def count_odd_three_digit_nums(nums):
    count = 0
    for num in nums:
        abs_num = abs(num)
        if 100 <= abs_num <= 999 and num % 2 == 1:
            count += 1
    return count