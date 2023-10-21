# Считайте файл согласно вашему варианту и подсчитайте частоту каждого слова в тексте. В результирующем файле выведите полученные данные в порядке убывания: 

filename = 'text_1_var_95'

with open(filename) as f:
    lines = f.readlines() #Возвращает все строки в файле в виде списка

word_state = dict()

for line in lines:
    #print(line.strip())
    row = (line.strip()
            .replace('!', ' ')      #Заменяем один символ на пробел
            .replace('?', ' ')
            .replace(',', ' ')
            .replace('.', ' ')
            .strip())
    #print(row)
    words = row.split()
    #print(words)

    for word in words:
        if word in word_state:          #Если слово уже встречалось в словаре, добавляем единицу, иначе, записываем его в словарь.
            word_state[word] += 1
        else:
            word_state[word] = 1

#print(word_state)

#Необходимо отсортировать слова в словаре в порядке убывания
word_state = (dict(sorted(word_state.items(), reverse = True, key = lambda item: item[1])))

print(word_state)

with open ('r_text_1_var_95', 'w') as res:
    for key, value in word_state.items():
        res.write(key + ':' + str(value) + '\n')
