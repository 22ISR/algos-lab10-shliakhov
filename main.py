from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Мой TODO-лист")

listbox = Listbox(root, width=30, height=5)
listbox.pack(pady=10)
listbox.insert(END, "Элемент 1")
listbox.insert(END, "Элемент 2")
listbox.insert(END, "Элемент 3")

def add():
    new_language = language_entry.get()
    listbox.insert(END, new_language)

language_entry = ttk.Entry()
language_entry.pack()
ttk.Button(text="Добавить", command=add).pack()



# def get_selected():
#     selected = listbox.curselection()
#     if selected:
#         print("Выбрано:", listbox.get(selected[0]))

# select_button = Button(root, text="Выбрать", command=get_selected)
# select_button.pack()

def delete_selected():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected[0])
        new_language = listbox.delete(selected[0])

delete_button = Button(root, text="Удалить", command=delete_selected)
delete_button.pack()

def clear_listbox():
    listbox.delete(0, END)

clear_botton = Button(root, text="Очистить всё", command=clear_listbox) 
clear_botton.pack()

root.mainloop() 

