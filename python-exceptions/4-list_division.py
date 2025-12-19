#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divide element by element 2 lists."""
    result_list = []
    for i in range(list_length):
        result = 0
        try:
            num1 = my_list_1[i]
            num2 = my_list_2[i]
            result = num1 / num2
        except ZeroDivisionError:
            print("division by 0")
        except (TypeError, ValueError):
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            result_list.append(result)
    return result_list
