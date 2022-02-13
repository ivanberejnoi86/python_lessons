###########################################################################
persons  = [
    {'name': 'Jhon', 'age': 15},
    {'name': 'Nick', 'age': 34},
    {'name': 'Sem', 'age': 19},
    {'name': 'Donald', 'age': 39},
    {'name': 'Bill', 'age': 42},
    {'name': 'Ben', 'age': 34},
    {'name': 'Gerald', 'age': 15},
    {'name': 'Robin', 'age': 15},
    ]

def min_age(input_arr):
    name = []
    min_age_persons = min(input_arr, key= lambda item: item['age'])
    for personidx in range(len(input_arr)):
        if min_age_persons['age'] == input_arr[personidx]['age']:
            name.append(input_arr[personidx]['name'])
    return name

print(f'Самый млаший {min_age(persons)} в списке.')

def longest_name(input_arr):
    long_name = []
    names = []
    for nameidx in range(len(input_arr)):
        names.append(input_arr[nameidx]['name'])
    longest = len(max(names, key=len))
    for name in names:
        if len(name) == longest:
            long_name.append(name)

    return long_name
print(f'Самое длинное имя {longest_name(persons)} в списке.')

def averag_age(input_arr):
    age = []
    for personidx in range(len(input_arr)):
        age.append(input_arr[personidx]['age'])
    averag = sum(age) / len(age)

    return int(averag)

print(f'Средний возраст в списке {averag_age(persons)} лет.')
###########################################################################
my_str1 = 'Leopold'
my_str2 = 'Adolf'
def symbols_in (input_str1, input_str2):
    symb_list = []
    for symb in input_str1:
        if symb in input_str2 and symb != ' ':
            symb_list.append(symb)
    return symb_list
print(symbols_in(my_str1, my_str2))
#############################################################################
my_str1 = 'Leonid'
my_str2 = 'Wladimir'

def symbol_in (input_str1, input_str2):
    symb_list = []
    for symb in input_str1:
        if symb in input_str2 and symb != ' ':
            symb_list.append(symb)
    return set(symb_list)
print(symbol_in(my_str1, my_str2))
################################################################################

import  random
import string

names = ['smith', 'williams', 'miller', 'johnson']
domains = ['com', 'net', 'ua', 'io']

def rand_string ():
    letters = string.ascii_lowercase
    rand_str = ''.join(random.choice(letters) for i in range(random.randint(4, 7)))

    return rand_str

def create_email (input_name, input_domains):
    rand_name = random.choice(input_name)
    rand_numb = random.randint(100,999)
    rand_domains = random.choice(input_domains)
    new_email = f'{rand_name}.{rand_numb}@{rand_string()}.{rand_domains}'

    return new_email
print(create_email(names, domains))
####################################################################################