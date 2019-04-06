# using tkinter Programming
import tkinter as tk 
from tkinter import ttk
from csv import DictWriter
import os
win=tk.Tk()
win.title('GUI')
name_label=ttk.Label(win, text='Enter your name:')
name_label.grid(row=0, column=0, sticky=tk.W)
age_label=ttk.Label(win, text='Enter your age:')
age_label.grid(row=1, column=0, sticky=tk.W)
email_label=ttk.Label(win, text='Enter your email:')
email_label.grid(row=2, column=0, sticky=tk.W)
gender_label=ttk.Label(win, text='Enter your gender:')
gender_label.grid(row=3, column=0, sticky=tk.W)

name_var=tk.StringVar()
name_eb=ttk.Entry(win, width=18, textvariable=name_var)
name_eb.grid(row=0, column=1)
name_eb.focus()
age_var=tk.StringVar()
age_eb=ttk.Entry(win,width=18, textvariable=age_var)
age_eb.grid(row=1, column=1)

email_var=tk.StringVar()
email_eb=ttk.Entry(win, width=18, textvariable=email_var)
email_eb.grid(row=2, column=1)


gender_var=tk.StringVar()
gender_cb=ttk.Combobox(win, width=15, textvariable=gender_var, state='readonly')
gender_cb['values']=('Male', 'Female', 'other')
gender_cb.current(0)
gender_cb.grid(row=3, column=1)

usertype=tk.StringVar()
radiobtn1=ttk.Radiobutton(win, text='Student', value='Student', variable=usertype)
radiobtn1.grid(row=4, column=0)

radiobtn2=ttk.Radiobutton(win, text='Teacher', value='Teacher', variable=usertype)
radiobtn2.grid(row=4, column=1)

checkbtn_var=tk.IntVar()
checkbtn=ttk.Checkbutton(win, text='check the login', variable=checkbtn_var)
checkbtn.grid(row=5, column=0)

#def action():
#    username=name_var.get()
#    userage=age_var.get()
#    useremail=email_var.get()
#    print(f'{username} is  {userage} years old , {useremail}')
#    user_gender=gender_var.get()
#    user_type=usertype.get()
#    if checkbtn_var.get() == 0:
#        login = 'NO'
#    else:
#        login = 'YES'
#    print(user_gender, user_type, login)
#
#    with open('gamepy.txt', 'a') as f:
#        f.write(f'{username},{userage},{useremail},{user_gender},{usertype},{login}\n')
#    
#    name_eb.delete(0, tk.END)
#    age_eb.delete(0, tk.END)
#    email_eb.delete(0, tk.END)
#    name_label.configure(foreground='red')

def action():
    username=name_var.get()
    userage=age_var.get()
    useremail=email_var.get()
    user_gender=gender_var.get()
    user_type=usertype.get()
    if checkbtn_var.get() == 0:
        login = 'NO'
    else:
        login = 'YES'

    with open('gamepy.csv', 'a', newline='') as f:
        dict_writer=DictWriter(f, fieldnames=['User Name', 'User Email Address', 'User Age', 'User Gender', 'User Type', 'login'])
        if os.stat('gamepy.csv').st_size==0:
            dict_writer.writeheader()
        dict_writer.writeheader()
        dict_writer.writerow({
            'User Name' : username,
            'User Email Address' : useremail,
            'User Age' : userage,
            'User Gender': user_gender,
            'User Type' : usertype,
            'login': login

        })







submit_button=ttk.Button(win, text='Submit', command=action)
submit_button.grid(row=6, column=1)

win.mainloop()


