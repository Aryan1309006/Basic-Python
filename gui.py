import tkinter as tk
root=tk.Tk()
root.geometry("300x300")

root.title("Tkinter Widgites Example")
label=tk.Label(root,text="Enter your Name:")
label.pack()
enter1=tk.Entry(root,width=20)
enter1.pack()

label2=tk.Label(root,text="Enter your Roll number:")
label2.pack()
enter2=tk.Entry(root,width=20)
enter2.pack()

label3=tk.Label(root,text="Enter your Email ID:")
label3.pack()
enter3=tk.Entry(root,width=20)
enter3.pack()

lable4=tk.Label(root,text="Select your  gender")
lable4.pack()
radio_var=tk.IntVar()
radiobutton1=tk.Radiobutton(root,text="Male",variable=radio_var,value=1)
radiobutton1.pack()
radiobutton2=tk.Radiobutton(root,text="Female",variable=radio_var,value=1)
radiobutton2.pack()

check_var=tk.BooleanVar()
checkbutton=tk.Checkbutton(root,text="Accept all terms and conditions", variable=check_var)
checkbutton.pack()

def on_button_click():
    print(f"Name:{enter1.get()}, Roll no:{enter2.get()}, Email ID:{enter3.get()},selected optioin:{radio_var.get()}, Terms and Conditions:{check_var.get()}")
button=tk.Button(root,text="Submit",command=on_button_click)
button.pack()
root.mainloop()
"""
____________________________________________OUTPUT______________________________________
Name:Aryan, Roll no:1034, Email ID:Aryan@gmail.com,selected optioin:1, Terms and Conditions:True
"""
