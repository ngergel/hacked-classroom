file = open('Rawlist.txt', 'r')
text_list = file.read().split('”')
text_list = '"'.join(text_list)
text_list = text_list.split('“')

for i in range(len(text_list)):
    text_list[i] = text_list[i].strip()

text_list = '"'.join(text_list)
print(text_list)