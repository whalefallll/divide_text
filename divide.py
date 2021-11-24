f = open('官场巅峰.txt', 'r', encoding='utf-8')
txt = f.read()
txt = txt.replace('###第一章\n', '')
txt_slice = txt.split('\n')
final_txt = ''
numbers = 0
for i in txt_slice:
    final_txt = final_txt + i
    if numbers < 1400:
        numbers += len(i)
    else:
        final_txt += '\n###第一章\n'
        numbers = 0

f2 = open('new.txt', 'w', encoding='utf-8')
f2.write(final_txt)
f.close()
f2.close()
