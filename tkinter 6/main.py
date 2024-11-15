from tkinter import *

def vlevo():
    selected_items = tovar_listbox.curselection()
    for i in selected_items[::-1]:
        item = tovar_listbox.get(i)
        pocypka_listbox.insert(END, item)
        tovar_listbox.delete(i)

def vpravo():
    selected_items = pocypka_listbox.curselection()
    for i in selected_items[::-1]:
        item = pocypka_listbox.get(i)
        tovar_listbox.insert(END, item)
        pocypka_listbox.delete(i)


root = Tk()
root.title("Покупки")


tovar_listbox = Listbox(root, selectmode=EXTENDED, width=15, height=8)
pocypka_listbox = Listbox(root, selectmode=EXTENDED, width=15, height=8)

# товары
for item in ['apple', 'tomato', 'milk', 'bananas', 'carrot', 'bread', 'butter', 'meat', 'potato', 'pineapple']:
    tovar_listbox.insert(END, item)


tovar_listbox.grid(row=0, column=0, padx=10, pady=10)
pocypka_listbox.grid(row=0, column=2, padx=10, pady=10)

#рамка
frame = Frame(root)
frame.grid(row=0, column=1, padx=10)

# Кнопки для перемещения
dobavlen_button = Button(frame, text=">>>", command=vlevo)
ydalen_button = Button(frame, text="<<<", command=vpravo)

# Расположение кнопок
dobavlen_button.pack(pady=1)
ydalen_button.pack(pady=1)


root.mainloop()
