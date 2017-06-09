test_num1 = 1
test_num2 = 10
test_num3 = 2


def handle_numbers(number1, number2, number3):
    count_div_numbers = 0
    div_numbers_list = []

    for number in range(number1, number2 + 1):
        if number % number3 == 0:
            count_div_numbers += 1
            div_numbers_list.append(str(number))
    if div_numbers_list:
        return "Result:\n{}, because {} are divisible by {}".\
            format(count_div_numbers, ', '.join(div_numbers_list), number3)
    else:
        return "Result:\nThere are no divisible numbers by {} in given range".\
            format(number3)

print (handle_numbers(test_num1, test_num2, test_num3))
