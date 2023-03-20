from tkinter import *


# add task to list box
def add_task():
    task = task_input.get()
    if task != "":
        tasks.insert(END, task)
        task_input.delete(0, END)


# delete selected task from list box
def delete_task():
    tasks.delete(ANCHOR)


# mark selected task as complete
def mark_complete():
    tasks.itemconfig(tasks.curselection(), fg="Green")


# create window
root = Tk()
root.geometry("450x640")

# create a title
root.title("To-Do List")

# heading
Label(root, text="Python TO-DO", font=("Aerial", 18), bg="Blue").pack(pady=10)
# create a label
Label(root, text="Enter Task", font=("Helvetica", 14), bg="sky blue").pack(pady=10)

# create an entry field
task_input = Entry(root, font=("Helvetica", 14), bg="white")
task_input.pack(pady=10)

# create a list box to display tasks
tasks = Listbox(root, font=("Helvetica", 14), bg="light grey", height=10)
tasks.pack(pady=20)

# create buttons to add, delete, and mark tasks as complete
Button(root, text="Add Task", font=("Helvetica", 14), bg = "sky blue" , command=add_task).pack(pady=5)
Button(root, text="Delete Task", font=("Helvetica", 14), bg = "sky blue" , command=delete_task).pack(pady=5)
Button(root, text="Mark as Complete", font=("Helvetica", 14) , bg = "sky blue" , command=mark_complete).pack(pady=5)

# run the application
root.mainloop()
