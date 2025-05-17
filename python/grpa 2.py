task = input()
# <eoi>

if task == 'factorial':
    n = int(input())
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(result)

elif task == 'even_numbers':
    n = int(input())
    for i in range(0, n + 1, 2):  # Start from 0 and increment by 2 to get even numbers
        print(i)

elif task == 'power_sequence':
    n = int(input())
    result = 1
    for _ in range(n):
        print(result)
        result *= 2

elif task == 'sum_not_divisible':
    n = int(input())
    total = sum(i for i in range(1, n) if i % 4 != 0 and i % 5 != 0)
    print(total)

elif task == 'from_k':
    n = int(input())  # Number of outputs to print
    k = int(input())  # Starting number

    count = 0
    for num in range(k, 0, -1):  # Start from k and decrease
        if count == n:  # Stop once we've printed 'n' numbers
            break
        if '5' not in str(num) and '9' not in str(num) and num % 2 != 0:
            reversed_num = int(str(num)[::-1])  # Reverse the digits
            print(reversed_num)
            count += 1

elif task == 'string_iter':
    s = input()
    prev_digit = 1
    for char in s:
        digit = int(char)
        print(digit * prev_digit)
        prev_digit = digit

elif task == 'list_iter':
    lst = input().split()  # Read input as space-separated values
    for item in lst:
        try:
            item_eval = eval(item)  # Convert to its correct type (int, float, etc.)
        except:
            item_eval = item  # Keep as string if conversion fails
        print(f"{item_eval} - type: {type(item_eval)}")

else:
    print("Invalid")
