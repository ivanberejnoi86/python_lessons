def input_string () -> str:
    input_string = input('Input string:')

    return  input_string

def output_date_in_file (file_name: str, input_string: str) -> None:
    with open(file_name, 'a+') as f:
        f.write(input_string + '\n')
    return

if __name__ == '__main__':
     file_name = 'date_file.txt'
     input_string = input_string()
     output_date_in_file(file_name, input_string)