from tkinter import *
from tkinter import ttk
import tkinter as tk
import mysql.connector
from tkinter import messagebox


def connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        port="3306",
        password="Quest@123",
        database="loginpage"

    )
def execute(a,b=()):
    conn=connection()
    courser=conn.cursor()
    courser.execute(a,b)
    conn.commit()
    conn.close()

def add():
    name=en1.get()
    id=en2.get()
    phone_NO=en3.get()
    if name and id and phone_NO:
        execute("insert into logintabl(name,id,phone_NO)values(%s,%s,%s)",(name,id,phone_NO))
        messagebox.showinfo("added","saved succecs fully")
    else:
        messagebox.showerror("error","fill full data")
def fetch_data():
    conn=connection()
    cursor=conn.cursor()
    cursor.execute('select * from logintabl')
    rows=cursor.fetchall()
    conn.close()
    return rows




def clear():
    en7.delete(1.0,END)


def clear_all():
    en1.delete(0,END)
    en2.delete(0,END)
    en3.delete(0,END)
    en4.delete(0,END)
    en5.delete(0,END)
    en6.delete(0,END)

def update():
  name=en4.get()
  id=en5.get()
  phone=en6.get()
  if name and id and phone:
      execute('update logintabl set name=%s,phone_NO=%s where id=%s',(name,phone,id))
      messagebox.showinfo('updated','data is updated')
  else:
      messagebox.showwarning("not found",'please enter full data')
def fetch_one(id):
    conn=connection()
    crsr=conn.cursor()
    crsr.execute('select * from logintabl where id=%s',(id,))
    s=crsr.fetchone()
    conn.close()
    return s
def display():
    id=en5.get()
    en7.delete(1.0,END)
    if id:
        row=fetch_one(id)
        if row:
            en7.insert(END,f"id:{row[1]},name:{row[0]},phone:{row[2]}")
            en4.delete(0,END)
            en6.delete(0,END)
            en4.insert(END,f"{row[0]}")
            en6.insert(END,f"{row[2]}")


        else:
            messagebox.showwarning('error','not found data')


    else:
        rows = fetch_data()
        for r in rows:
            en7.insert(END,f"id: {r[1]}, name: {r[0]},  phone_NO: {r[2]}\n")   
    
        


app=Tk()
app.title("login")
app.geometry('500x600')
lb1=Label(app,text='name')
lb1.place(x=60,y=50)
en1=Entry(app)
en1.place(x=160,y=50)
lb2=Label(app,text="id")
lb2.place(x=60,y=80)
en2=Entry(app)
en2.place(x=160,y=80)
lb3=Label(app,text='phone number')
lb3.place(x=60,y=110)
en3=Entry(app)
en3.place(x=160,y=110)
bt1=Button(app,text='Display',background="grey",activebackground="red",command=display)
bt1.place(x=80,y=180)
bt2=Button(app,text='Save',background='purple',
           command=add)
bt2.place(x=180,y=180)
bt5=Button(app,text='clear',activebackground="red",command=clear_all)
bt5.place(x=300,y=180)
lb4=Label(app,text='name')
lb4.place(x=60,y=250)
en4=Entry(app)
en4.place(x=160,y=250)
lb5=Label(app,text="id")
lb5.place(x=60,y=280)
en5=Entry(app)
en5.place(x=160,y=280)
lb6=Label(app,text='phone number')
lb6.place(x=60,y=310)
en6=Entry(app)
en6.place(x=160,y=310)
bt3=Button(app,text='Update',background="blue",command=update)
bt3.place(x=80,y=380)
bt4=Button(app,text='Delete',background='yellow')
bt4.place(x=180,y=380)
en7=tk.Text(app,width=55,height=7)
en7.place(x=20,y=430)
bt5=Button(app,text='clear',background='red',command=clear)
bt5.place(x=300,y=380)



app.mainloop()