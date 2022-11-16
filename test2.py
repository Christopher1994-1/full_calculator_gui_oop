value = "-9"
VALUE = int(value)

K_VALUE = int(value)
K = (K_VALUE - 273.15) * 1.8 + 32
final_value = str(K).split(".")[0]

print(final_value)
