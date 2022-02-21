import  os

def get_puples_from_files (file_path: str) -> list:
    with open(file_path, 'r') as file_obj:
        date = file_obj.readlines()
    puples = []
    for student in date:
        item = {
            'name': student.replace('/n', '').split()[0],
            'surname': student.replace('/n', '').split()[1],
            'points': [int(x) for x in student.replace('/n', '').split()[2::]]
        }

        puples.append(item)

    return puples

def average_rating_puples (input_list: list) -> list:
    update_puples_list = []
    for student in input_list:
        item = {
            'surname': student['surname'],
            'name': student['name'][0]+'.',
            'average': round(sum(i for i in student['points']) / len(student['points']), 2)
        }
        update_puples_list.append(item)
    return update_puples_list

def print_lagging_student(input_list: list) -> list:
    lagging_student = []
    for student in input_list:
        if int(student['average']) < 5:
            lagging_student.append(student)

    return print('{0}\n{1}'.format(lagging_student[0], lagging_student[1]))

def print_avarage_in_class (input_list: list) -> list:
    avarage_in_class = float()
    for student in input_list:
        avarage_in_class += float(student['average'])
    return print(f'Средний балл по классу {round(avarage_in_class / len(input_list), 2)}.')

def create_file_with_puples (puples: list, file_name: str) -> None :
    with open(os.path.join(file_name), 'w') as f:
        for student in puples:
            f.write('\n')
            for key in student.keys():
                if key == 'surname':
                    f.write(str(student[key]) + ' ')
                elif key == 'name':
                    f.write(str(student[key]) + '   ')
                else:
                    f.write(str(student[key]).rjust(20 - len(student["surname"]),' '))
    return

if __name__ == '__main__':
    file_path = 'puples_list.txt'
    file_name = 'new_puples_list.txt'
    puples = get_puples_from_files(file_path)
    # print(get_puples_from_files(file_path))
    update_student_list = average_rating_puples(puples)
    print_lagging_student(update_student_list)
    print_avarage_in_class(update_student_list)
    create_file_with_puples(update_student_list, file_name)
