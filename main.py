import os

file_list = []
for filename in os.listdir('sorted'):
    with open(os.path.join('sorted', filename), 'r', encoding='utf-8') as f:
        text = f.readlines()        
        len_ = len(text)
        file_list.append(f'{len_}: {filename}')
file_list.sort()
with open('result.txt','w', encoding='utf-8') as f:
    for name in file_list:
        q = str(name)
        x = q.partition(': ')[2]
        n = x.partition('.')[0]
        i = 0
        with open(os.path.join('sorted',(x)),encoding='utf-8') as f_in:
            for s in f_in:
                i += 1
                out_s = f'Строка номер {i} файла номер {n} {s.strip()}'
                f.write(out_s)
                f.write('\n')