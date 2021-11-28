from cli import write_value_repeat, write_text

def data_read():
    data_list = []
    data = open("data.csv", "r")
    for str_row in data:
        list_row = str_row.strip().split(",")
        data_list.append(list_row)
    data.close()
    return data_list


def info_order(data_list, line_insert_into):
    text = open("data_to_insert.txt", "w")
    for list_row in data_list:
        value_str = write_value_repeat(list_row)
        write_text(line_insert_into, value_str, text)
    text.close()

