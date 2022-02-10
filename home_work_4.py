##################################################################################
digit = 10203250
my_text = str(digit)
count_1 = 0
for number in my_text:
    if number == '0':
        count_1 += 1
print(count_1)

####################################################################################
digit = 1230000
my_text = str(digit)
count = 0
for number in my_text[::-1]:
    if number == '0':
        count += 1
    else:
        break
print(count)

######################################################################################
my_list_1 = [1,3,5,7,9]
my_list_2 = [2,4,6,8,10]
my_result = []
for i in range(len(my_list_2)):
    if i % 2 == 0:
        my_result.append(my_list_1[i])
    elif i % 2 != 0:
        my_result.append(my_list_2[i])
print(my_result)

########################################################################################
my_list = [1, 2, 3, 4]
new_list = my_list[1:] + my_list[:1]
print(new_list)
print(id(my_list), id(new_list))

#########################################################################################
my_list = [1, 2, 3, 4]
my_list.append(my_list.pop(0))
print(my_list)

###########################################################################################
my_str = '43 больше чем 34 но меньше чем 56'
new_str = my_str.split()
sum = 0
for word in new_str:
    if word.isdigit():
        sum += int(word)
print(sum)

##############################################################################################
my_str = 'My long string'
l_limit = 'o'
r_limit = 'g'
l_limit_indx = my_str.find(l_limit)
r_limit_indx = my_str.rfind(r_limit)
sub_str = my_str[l_limit_indx + 1:r_limit_indx]
print(sub_str)

################################################################################################
my_str = 'abcde'
my_list = []
for i in range(len(my_str)):
    if i % 2 == 0:
        my_list.append(my_str[i:i+2])
for word_indx in  range(len(my_list)):
    if len(my_list[word_indx]) < 2:
        my_list[word_indx] += '_'
print(my_list)

#################################################################################################
my_list = [1, 5, 7, 8, 0, 6, 5, 4]
count = 0
for num_idx in range(1, len(my_list) - 1):
    if my_list[num_idx] > my_list[num_idx -1] + my_list[num_idx +1]:
        count += 1
print(count)

##################################################################################################








