import tkinter as tk
from tkinter import *
from tkinter import messagebox
screen = Tk()
screen.geometry("400x250")
#tạo hàm câu lệnh cho submit button
def clickSubmitButton():
    messagebox.showinfo("Đăng nhập", "Bạn đã đăng nhập thành công")
#tạo cancel button
cancelButton = Button(screen, text="Cancel").grid(row=5, column= 0)
#tạo submit button
submitButton = Button(screen, text="Submit", fg="red", activebackground="red", activeforeground="white", command=clickSubmitButton)
submitButton.grid(row=5, column=1)
#tạo label để hiển thị nội dung
#tạo entry để nhập nội dung
name = Label(screen, text= "Name").grid(row=0, column=0)
nameFill = Entry(screen).grid(row=0, column=1)
passWord = Label(screen, text="Password").grid(row=1, column=0)
passWordFill = Entry(screen).grid(row=1, column=1)

screen.mainloop()