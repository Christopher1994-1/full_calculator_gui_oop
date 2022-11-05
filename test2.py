import math


value = "8"

value_sqrt = str(math.sqrt(int(value)))

if len(value_sqrt) > 4:
    value_length = len(value_sqrt) - 3
    value_cut = value_sqrt[:-value_length]
    print(value_cut)
    
    