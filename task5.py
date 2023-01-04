# Даны два файла, в каждом из Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

path = 'file.txt'
data = open (path, 'r') # считывает файл
for line in data:   # считывает каждую строку в файле
    print(line)
data.close()

path1 = 'file1.txt'
data1 = open (path1, 'r') # считывает файл
for line1 in data1:   # считывает каждую строку в файле
    print(line1)
data1.close()
    
print(f"{line[:-2]}+{line1[:-2]} = 0")