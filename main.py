from cli import input_info
from controller import data_read, info_order
from tkinter import *
from tkinter import messagebox as message_box


data_list = data_read() #--------------en esta funcion busca el archivo entregado en cli.py, asegurese de que se llame "data.csv" y que la consola este asignada a la carpeta actual con cd .\insertor de datos SQL---------------------
line_insert_into = input_info() #---------aca se debe ingresar el input una vez se lo pide por consola, idealmente use el formato dispuesto en el ejemplo del input---------
info_order(data_list, line_insert_into)#----------aca ordena los datos y asigna las demas funciones para que escriban donde se debe la informacion esperada-------------

'''
window = Tk()
window.title("Insertor de datos SQL")
window.geometry("1080x960")

input_insert_into = StringVar()
input_insert_into_graphic = Label(window, text="ingrese el texto de posterior al insert into, ejemplo: cliente(rut, nombre, apellido_materno, apellido_paterno) ").pack()
input_insert_into_entry = Entry(window, textvariable=input_insert_into).pack()
message_box.showinfo("su data para insertar fue creada")

window.mainloop()
'''