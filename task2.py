test_string = "Hello! 111---000. I'm test string. Digits: 754."


def handle_string(string):
    letters_count = 0
    digits_count = 0
    for sign in string:
        if sign.isalpha():
            letters_count += 1
        elif sign.isdigit():
            digits_count += 1
    return "Result:\nLetters - {}\nDigits - {}".format(
        letters_count, digits_count)

print (handle_string(test_string))
