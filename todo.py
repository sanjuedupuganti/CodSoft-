import os
import tkinter as tk
from tkinter import messagebox

def create_list(list_name):
    if not os.path.exists(list_name + ".txt"):
        with open(list_name + ".txt", "w"):
            pass
        messagebox.showinfo("Success", f"To-Do List '{list_name}' created successfully!")
    else:
        messagebox.showerror("Error", "To-Do List with that name already exists!")

def add_task(list_name, task):
    with open(list_name + ".txt", "a") as f:
        f.write(task + "\n")
    messagebox.showinfo("Success", f"Task '{task}' added to the '{list_name}' list!")

def show_list(list_name):
    if not os.path.exists(list_name + ".txt"):
        messagebox.showerror("Error", f"To-Do List '{list_name}' doesn't exist.")
        return

    with open(list_name + ".txt", "r") as f:
        tasks = f.readlines()
        if tasks:
            task_text = "\n".join([f"{index}. {task.strip()}" for index, task in enumerate(tasks, start=1)])
            messagebox.showinfo(f"To-Do List Contents", task_text)
        else:
            messagebox.showinfo(f"To-Do List Empty", f"To-Do List '{list_name}' is empty.")

def main():
    root = tk.Tk()
    root.title("To-Do List Application")

    def create_list_callback():
        list_name = list_name_entry.get()
        create_list(list_name)

    def add_task_callback():
        list_name = list_name_entry.get()
        task = task_entry.get()
        add_task(list_name, task)

    def show_list_callback():
        list_name = list_name_entry.get()
        show_list(list_name)

    label = tk.Label(root, text="Welcome to the To-Do List Application!", font=("Helvetica", 16))
    label.pack(pady=10)

    list_name_label = tk.Label(root, text="To-Do List Name:")
    list_name_label.pack()
    list_name_entry = tk.Entry(root)
    list_name_entry.pack()

    add_button = tk.Button(root, text="Create To-Do List", command=create_list_callback)
    add_button.pack(pady=5)

    task_label = tk.Label(root, text="Task:")
    task_label.pack()
    task_entry = tk.Entry(root)
    task_entry.pack()

    add_button = tk.Button(root, text="Add Task", command=add_task_callback)
    add_button.pack(pady=5)

    show_button = tk.Button(root, text="Show To-Do List", command=show_list_callback)
    show_button.pack(pady=5)

    exit_button = tk.Button(root, text="Exit", command=root.quit)
    exit_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
