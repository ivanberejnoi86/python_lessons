#################################################################
my_list = list(range(10, 201, 10))
for number in my_list:
    if number > 100:
        print(number)

##################################################################
my_list = list(range(10, 201, 10))
my_result = []
for number in my_list:
    if number > 100:
        my_result.append(number)
print(my_result)

##################################################################
my_list = [1, 4, 4]
count_idx = len(my_list)
if count_idx < 2:
     my_list.append(0)
elif count_idx >= 2:
     my_list.append(my_list[count_idx-1] + my_list[count_idx-2])
print(my_list)
###################################################################
my_string = '0123456789'
my_list = []
for smb_1 in my_string:
     for smb_2 in my_string:
         my_list.append(int(smb_1 + smb_2))
print(my_list)
####################################################################