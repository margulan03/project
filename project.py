from tkinter import *
import csv
day = []
hour = []
price =[]
airline = []
var = []

with open('airplanes.csv', 'r') as file:
    read = csv.reader(file, delimiter=';')
    f = list(read)
    del (f[0])
    for x in f:
        day.append(x[0])
        hour.append(x[1])
        price.append(x[2])
        airline.append(x[3])


def start():
    ent_name.grid(row=1, column=0, padx=180, pady=20)
    ent_surname.grid(row=3, column=0)
    batton1.grid(row=4, column=0, pady=20)
    label1.grid(row=0, column=0, pady=10)
    label2.grid(row=2)



def tickets1():
    ent_name.grid_forget()https://zoom.us/j/97174852996?pwd=cy9sN3kxVWFRNmlKM0JQSnRIZWNaZz09
    batton1.grid_forget()
    label1.grid_forget()
    label2.grid_forget()
    label5.grid_forget()
    ent_surname.grid_forget()
    label4.grid_forget()
    label6.grid_forget()
    batton3.grid_forget()
    batton4.grid_forget()
    listb1.grid(row=1, column=0, padx=160, pady=10)
    label3.grid(row=0, pady=20)
    batton2.grid(row=2, column=0)
    for x in range(len(day)):
        var.append(day[x] + ' ' + hour[x] + ' ' + airline[x])
        a = StringVar(value=var)
        listb1.config(listvariable=a)


def tickets2():
    listb1.grid_forget()
    label3.grid_forget()
    batton2.grid_forget()
    i = listb1.curselection()[0]
    label5.grid(row=0, column=0, padx=200, pady=20)
    label4.grid(row=1, column=0, padx=200)
    label4.config(text=price[i]+'теңге')
    label6.grid(row=2, column=0)
    batton3.grid(row=3, column=0)
    batton4.grid(row=4, column=0)


def order():
    label5.grid_forget()
    label4.grid_forget()
    label6.grid_forget()
    batton3.grid_forget()
    batton4.grid_forget()
    i = listb1.curselection()[0]
    label7.grid(row=0, column=0, padx=200, pady=50)
    with open('order.txt', 'w+') as f_txt:
        f_txt.writelines('Name: '+ent_name.get()+'\n')
        f_txt.writelines('Surname: '+ent_surname.get()+'\n')
        f_txt.writelines('Date: '+day[i]+' '+hour[i]+'\n')
        f_txt.writelines('Airline: '+airline[i]+'\n')
        f_txt.writelines('Price: '+price[i]+' тенге')


root = Tk()
root.geometry('500x300')
root.title('AIRPLANES')

label1 = Label(root, text='Enter yor name:')
label2 = Label(root, text='Enter yor surname:')
label3 = Label(root, text='Choose time and airline:')
label4 = Label(root, text='')
label5 = Label(root, text='Price of ticket:')
label6 = Label(root, text='Place an order?')
label7 = Label(root, text='Order is processed')

listb1 = Listbox(root, listvariable='', width=30)
listb2 = Listbox(root, listvariable='', width=30)

batton1 = Button(root, text='Next', width=10, command=tickets1)
batton2 = Button(root, text='Next', width=10, command=tickets2)
batton3 = Button(root, text='Yes', width=10, command=order)
batton4 = Button(root, text='No', width=10, command=tickets1)


ent_name = Entry(root, width=25)
ent_surname = Entry(root, width=25)

start()

root.mainloop()