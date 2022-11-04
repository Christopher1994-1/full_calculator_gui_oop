import re


value_to_calculate = "2 + "
toBeCal = value_to_calculate.split(" ")
measured = len(toBeCal)
last_digit = re.search(r'\d+$', value_to_calculate)



        # ------------ Checks Addition Operator ------------ #
        
if toBeCal.count("+") and measured == 3 and last_digit != None:
    first_num = toBeCal[0]
    second_num = toBeCal[2]
    result = int(first_num) + int(second_num)
    # self.advanced_zero_base_input.set(value=str(result))
    print(result)
else:
    print("None")