#######################################

print("Удвоенный результат целого числа.")
get_value = input("Введите число:")
transform_value = int(get_value)
new_value = transform_value * 2
print(f"Вы ввели {get_value}, результат- {new_value}.")

########################################

print("Удвоенный результат не целого числа.")
get_value = input("Введите число:")
transform_value = float(get_value)
new_value = transform_value * 2
print("Вы ввели {}, результат- {}.".format(get_value, new_value))

##########################################

print("Удвоеная строка.")
get_str = input("Введите строку:")
new_str = get_str +" "+ get_str

print("Вы ввели: " + get_str + " результат " + new_str)








