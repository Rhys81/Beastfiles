class Prime:
    # where 0 is the first number and 5 is the last number
    for num in range(0, 5 + 1):
        if num > 1:
            for x in range(2, num):
                if (num % x) == 0:
                    break
            else:
                print(num)