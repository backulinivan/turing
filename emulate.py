#Задача словаря инструкций из файла
def emulate_instructions(inp_instructions):
    inst_dict = {}
    inst_file = open(inp_instructions, 'r')
    single_inst = inst_file.readline().rstrip()
    while single_inst:
        off_st, off_val, dst_st, dst_val, dir = single_inst.split()
        if off_st in inst_dict:
            inst_dict[off_st].update({off_val:(dst_st, dst_val, dir)})
        else:
            inst_dict.update({off_st:{off_val:(dst_st, dst_val, dir)}})
        single_inst = inst_file.readline().rstrip()
    inst_file.close()
    return inst_dict

#Задача изначальной строки
def emulate_initial_string(inp_str):
    inp_file = open(inp_str, 'r')
    init_str = inp_file.readline()
    inp_file.close()
    return init_str

#Исполнительная функция
def executor(string, init_state, inst):
    state = init_state
    pos = 1
    charlist = list(string)
    while state != 'Q':
        cur_ch = inst[state][charlist[pos]]
        state = cur_ch[0]
        charlist[pos] = cur_ch[1]
        direction = cur_ch[2]
        if direction == 'R':
            pos += 1
        else:
            pos -= 1
    return ''.join(charlist)

#Умножение бинарного числа на два
instructions1 = emulate_instructions('instructions1.txt')
initial_string1 = emulate_initial_string('input_string1.txt')
result1 = executor(initial_string1, 'q0', instructions1)
print('№1')
print('Initial', initial_string1)
print('Result ', result1,'\n')

#Перенос начального символа в конец
instructions2 = emulate_instructions('instructions2.txt')
initial_string2 = emulate_initial_string('input_string2.txt')
result2 = executor(initial_string2, 'q0', instructions2)
print('№2')
print('Initial', initial_string2)
print('Result ', result2,'\n')

#Стирание слова, если первый ипоследний символы совпадают
instructions3 = emulate_instructions('instructions3.txt')
initial_string3 = emulate_initial_string('input_string3.txt')
result3 = executor(initial_string3, 'q0', instructions3)
print('№3')
print('Initial', initial_string3)
print('Result ', result3,'\n')

#Удаление второго символа
instructions4 = emulate_instructions('instructions4.txt')
initial_string4 = emulate_initial_string('input_string4.txt')
result4 = executor(initial_string4, 'q0', instructions4)
print('№4')
print('Initial', initial_string4)
print('Result ', result4,'\n')

#Удаление первого вхождения а в слове
instructions5 = emulate_instructions('instructions5.txt')
initial_string5 = emulate_initial_string('input_string5.txt')
result5 = executor(initial_string5, 'q0', instructions5)
print('№5')
print('Initial', initial_string5)
print('Result ', result5,'\n')