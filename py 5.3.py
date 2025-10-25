from tkinter import *


root = Tk()

root.title("Student Mark List")
root.geometry("500x400")

f1 = Frame(root, bg="red")
f1.pack(fill=BOTH, expand=True)

l1 = Label(f1, text="ARITHMETIC OPERATIONS", bg="red", fg="purple", font=("Arial", 25))
l1.pack(pady=20)


f2 = Frame(root, bg="black")
f2.pack(fill=BOTH, expand=True)

l2 = Label(f2, text="Student Mark List", bg="blue", fg="white", font=("Arial", 18))
l2.pack(pady=20)


root.mainloop()
