from pathlib import Path
file_path = Path("config_sw1.txt")

ignore = ["duplex", "alias", "Current configuration"]

def convert_config_to_dict(config_filename):
    with open(config_filename,'r') as f:
        content=f.readlines()
        dict_config={}
        parent_line=''
        for line in content:           
 #              check wether this ^'!' or ignore_list content in line
            if line.startswith('!') or line.startswith('\n') or ignore_command(line,ignore):
                continue
            if not line.startswith(' '):
                 parent_line=line.strip()
                 dict_config[parent_line]=[]
            else:
                 linestr=line.strip()
                 dict_config[parent_line].append(linestr)
    return dict_config




def ignore_command(command, ignore):
    ignore_status = False
    for word in ignore:
        if word in command:
            ignore_status = True
    return ignore_status
"""
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
"""



if __name__ == '__main__':
    conf_output= convert_config_to_dict(file_path)
    print(conf_output)