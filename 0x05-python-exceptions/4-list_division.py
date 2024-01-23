#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []

   try:
       for i in range(list_length):
           if i >= len(my_list_1) or i >= len(my_list_2):
               raise IndexError("out of range")
           
           try:
               result = my_list_1[i] / my_list_2[i]
               result_list.append(result)
            except ZeroDivisionError:
                print("division by 0")
                result_list.append(0)
            except (TypeError, ValueError):
                print("wrong type")
                result_list.append(0)

        except IndexError as e:
            print(e)
        finally:
            return result_list
