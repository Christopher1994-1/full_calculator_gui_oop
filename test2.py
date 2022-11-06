value = "2 + 2.5"
fli = value.split(" ")
number_one = fli[0]
number_two = fli[2]


if "." in number_one:
    print("Index 1")
elif "." in number_two:
    print("Index 2")
    