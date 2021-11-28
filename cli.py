
def input_info():
    line_insert_into = str(input(" ingrese el texto de posterior al insert into, ejemplo: cliente(rut, nombre, apellido_materno, apellido_paterno) "))
    return line_insert_into

def write_value_repeat(list_row):
    value_str = ''
    counter = 0
    while (counter < len(list_row)):
        if (counter < len(list_row) - 1):
            value_str += f' "{list_row[counter]}",'
        if (counter == len(list_row) - 1):
            value_str += f' "{list_row[counter]}"'
        counter += 1
    return value_str

def write_text(line_insert_into, value_str, text):
    text.write(f'''
insert into {line_insert_into}
value({value_str}); \n
    ''')