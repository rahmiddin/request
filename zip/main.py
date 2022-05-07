import os

BASE_PATH = os.getcwd()
LOG_GIR = 'файлы'
FULL_LOG_PATH = os.path.join(BASE_PATH, LOG_GIR)
SHARED_FILE = str(input('Введите имч файла в который будет помешен текст: '))

def get_text(shared_file: str):
    list_ = []
    max_sum = 0
    for i in os.walk(FULL_LOG_PATH):
        for item in i[2]:
            file_sum = sum(1 for line in open(f'{FULL_LOG_PATH}//{item}', 'r', encoding='utf-8'))
            if item != shared_file:
                if file_sum > max_sum:
                    with open(f'{FULL_LOG_PATH}//{item}', 'r', encoding='utf-8') as file:
                        info = f'\nИмя файла: {item}\nКоличесво строк: {file_sum}\n\n'
                        list_.insert(0, info + file.read() + '\n')
                    max_sum=file_sum
                else:
                    with open(f'{FULL_LOG_PATH}//{item}', 'r', encoding='utf-8') as file:
                        info = f'\nИмя файла: {item}\nКоличесво строк: {file_sum}\n\n'
                        list_.append(info + file.read() + '\n')
            else:
                pass
    return list_


def add(file_name, text):
    with open(f'{FULL_LOG_PATH}//{file_name}', 'a', encoding='utf-8') as file:
        for i in text:
            file.write(i)

add('full.txt', text=get_text(shared_file=SHARED_FILE))