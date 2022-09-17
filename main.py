number = int(input("Введите число: "))

#TODO

def array_digit(number_all: int) -> list:
    list_digit = []
    while number_all:
        digit = number_all % 10
        list_digit.append(digit)
        number_all = number_all // 10
    list_digit.reverse()
    return list_digit


def square_digit(arr_digit: list) -> bool:
    res_number = 0
    for item in range(len(arr_digit)):
        res_number += arr_digit[item] ** 2
    if res_number != 1 and res_number > 0:
        array_digit(res_number)
        list_array_result = array_digit(res_number)
        square_digit(array_digit(list_array_result))
    elif res_number == 1:
        return True
    else:
        return False


array_digit(number)
list_result = square_digit(array_digit)
print(list_result)