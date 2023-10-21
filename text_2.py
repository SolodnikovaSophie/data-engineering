# Считайте файл согласно вашему варианту и подсчитайте сумму чисел, по каждой строке. В результирующем файле выведите полученные данные

filename = 'text_2_var_95'
with open(filename) as file:
    lines = file.readlines()   #Считываем строки в исходном файле

summ_lines = list()

for line in lines:
    print()
    nums = line.split('|')
    summ_line = 0
    for num in nums:
        summ_line += int(num)
    average = summ_line / len(nums)

    summ_lines.append(average)

print(summ_lines)

with open('r_text_2_var_95', 'w') as result:
    for value in summ_lines:
        result.write(str(value) + '\n')
