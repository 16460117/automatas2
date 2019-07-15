"""
Nombre: main.py
Objetivo: Conectar a una base de datos en MySQL mediante una interfaz grafica
Autor: Carbajal Ramos Juan Jesús
Fecha: 15/07/19
"""

from tkinter import *
from tkinter import ttk
import pymysql
from reportlab.pdfgen import canvas
import time


def insertar(*args):
    cursor = db.cursor()
    cadsqlinsert = "insert into KeyWord values(" + nombre_entry.get() + "," + "'" + clave_entry.get() + "');"
    cursor.execute(cadsqlinsert)
    db.commit()


def eliminar(*args):
    cursor = db.cursor()
    cadsqldel = "delete from KeyWord where clave =" + clave_delete.get() + ";"
    cursor.execute(cadsqldel)
    db.commit()

def mostrar(*args):

    ml = 10
    t = "                          "
    j = 740

    c = canvas.Canvas('Reporte.pdf')

    c.drawString(ml, 830, "Empresa: La Gran Empresa")
    c.drawString(ml, 810, "Reporte generado el: " + time.strftime("%d/%m/%y"))
    c.drawString(ml, 760, "Clave" + t + "Nombre")

    
    cursor = db.cursor()
    cadsqlbuscar = "select * from KeyWord;"
    cursor.execute(cadsqlbuscar)
    result = cursor.fetchall()


    for row in result:
        clave = row[0]
        nombre = row[1]
        c.drawString(ml, j, "    {0}".format(clave,nombre) + t + "   {1}".format(clave,nombre))
        j = j - 15

    c.save()
    

def modificar(*args):
    cursor = db.cursor()
    cadsqlchange = "UPDATE `KeyWord` SET nombre = '" + nombre_mod.get() + "' WHERE clave = " + clave_mod.get() + ";"
    cursor.execute(cadsqlchange)
    db.commit()
    

#---------------------------------------------------------------------

try:
    db = pymysql.connect("localhost", "root", "", "AutomatasII")
except:
    print('mal')

root = Tk()
root.title("Base de datos")

mainframe = ttk.Frame(root, padding="10 10 10 100")
mainframe.grid(column=1, row=0)

#------------------------------------------------------

nombre_entry = ttk.Entry(mainframe, width=7)
nombre_entry.grid(column=1, row=0)

clave_entry = ttk.Entry(mainframe, width=7)
clave_entry.grid(column=1, row=1)

ttk.Button(mainframe, text="Insertar", command=insertar).grid(column=1  , row=2)

ttk.Label(mainframe, text="Clave").grid(column=0, row=0)
ttk.Label(mainframe, text="Nombre").grid(column=0, row=1)

#----------------------------------------------------------------------------------

ttk.Label(mainframe, text="                 ").grid(column=2, row=0)
ttk.Label(mainframe, text="Clave").grid(column=3, row=0)

clave_delete = ttk.Entry(mainframe, width=7)
clave_delete.grid(column=4, row=0)

ttk.Button(mainframe, text="Borrar", command=eliminar).grid(column=4  , row=1)

#------------------------------------------------------------------------------------

ttk.Label(mainframe, text="               ").grid(column=5, row=0)
ttk.Label(mainframe, text="Clave").grid(column=6, row=0)
ttk.Label(mainframe, text="Nombre").grid(column=6, row=1)

clave_mod = ttk.Entry(mainframe, width=7)
clave_mod.grid(column=7, row=0)

nombre_mod = ttk.Entry(mainframe, width=7)
nombre_mod.grid(column=7, row=1)

ttk.Button(mainframe, text="Modificar", command=modificar).grid(column=7  , row=2)

#-------------------------------------------------------------------------------------

ttk.Label(mainframe, text="               ").grid(column=8, row=0)

ttk.Button(mainframe, text="Reporte", command=mostrar).grid(column=9  , row=0)

#-------------------------------------------------------------------------------------

root.mainloop()
