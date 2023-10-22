import csv

average_salary = 0
items = list()

with open('text_4_var_95', newline = '\n', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',')
    for r in reader:
        #print(r)
        item = {
            'number': int(r[0]),
            'name': r[2] + ' ' + r[1],
            'age': int(r[3]),
            'salary': int(r[4][0:-1])
        }

        average_salary += item['salary']
        items.append(item)

#print(items)

average_salary /= len(items)

filter_list = list()
for item in items:
    if (item['salary'] > average_salary) and item['age'] > (25 + (95 % 10)):
        filter_list.append(item)
#print(filter_list)

filter_list = sorted(filter_list, key = lambda i: i['number'])

with open('r_text_4_var_95', 'w', encoding = "utf-8", newline = '') as res:
    writer = csv.writer(res, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)

    for item in filter_list:
        writer.writerow(item.values())