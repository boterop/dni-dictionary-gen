import os
from datetime import datetime

MAX_SAVE_LIST = 10000

def save_pass(file_name, password):
    os.system(f'echo {password} >> {file_name}.txt')

def printProgressBar (iteration, total):
    prefix = 'Progress:'
    suffix = 'Complete'
    length = 50
    fill = '█'
    decimals = 1
    printEnd = "\r"
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)

    if iteration == total: 
        print()

def create_passwords_list(min_num, max_num, file_name):
    start_time = datetime.now()
    words = max_num-min_num
    printProgressBar(0, words)
    buffer = ""
    buffer_len = 0
    for i in range(min_num, max_num):
        buffer += f'{str(i)}\n'
        buffer_len += 1
        if buffer_len == MAX_SAVE_LIST:
            save_pass(file_name, f'"{buffer}"')
            buffer = ""
            buffer_len = 0
            printProgressBar(i-min_num, words)
    end_time = datetime.now()
    difference = end_time - start_time
    print(f'{words} passwords registered in {difference.seconds} seconds')

print("Generate an entire identification number list")
dni = input("DNI: ")
dni_len = len(dni)-1
dni_num = int(dni) // 10**dni_len
start_in_dni = input(f'Start in {dni}? (yes/no): ').lower()[0] == 'y'
first_num = int(dni_num) * 10**dni_len if not start_in_dni else int(dni)
last_num = (int(dni_num)+1) * 10**dni_len
file_name = input("File name: ")
create_passwords_list(first_num, last_num, file_name)
