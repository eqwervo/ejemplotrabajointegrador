from pathlib import Path
import csv

path_file = Path(__file__).parent.parent / 'files' / 'usu_individual_T324.txt'

print(f'Ruta: {path_file.resolve()}')


gender_index = 11         # 1 = Varon, 2 = Mujer
pondera_index = 9
age_index = 13
education_index = 19
edu_complete_index = 20



def gender_counter(path_file):
    count_m = 0
    count_f = 0 
    with open(path_file, encoding='UTF-8') as archivo_csv:
        reader = csv.reader(archivo_csv, delimiter=';')
        header = next(reader)
        for row in reader:
            if row[gender_index] == '1':
                count_m += int(row[pondera_index])
            else:
                count_f += int(row[pondera_index])
        print(f'Cantidad Femenimo: {count_f} || Cantidad Masculino: {count_m}')

