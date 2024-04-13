# Python: How to ignore #comment lines in a File 

with open('example.txt', 'r', encoding='utf-8') as file_obj:
    for line in file_obj:
        line = line.strip()
        if not line.startswith('#'):
            print(line)
