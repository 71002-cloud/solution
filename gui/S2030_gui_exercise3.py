"""Opgave "GUI step 3":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

--------

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2030.png

Genbrug din kode fra "GUI step 2".

GUI-strukturen bør være som følger:
    main window
        labelframe
            frame
                treeview and scrollbar
            frame
                labels and entries
            frame
                buttons

Funktionalitet:
    Klik på knappen "clear entry boxes" sletter teksten i alle indtastningsfelter (entries).

--------

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""

import tkinter as tk
from tkinter import ttk

def button_clear_entry_boxes():
    entry_1.delete(0, "end")
    entry_2.delete(0, "end")
    entry_3.delete(0, "end")
    entry_4.delete(0, "end")

padx = 4
pady = 4
rowheight = 24
treeview_background = "#eeeeee"
treeview_foreground = "black"
treeview_selected = "#d4d4d4"

main_window = tk.Tk()
main_window.title('My first GUI')
main_window.geometry('500x500')

style = ttk.Style()
style.theme_use('default')
style.configure("Treeview", background=treeview_background, foreground=treeview_foreground, rowheight=rowheight, fieldbackground=treeview_background)
style.map('Treeview', background=[('selected', treeview_selected)])

frame_1 = tk.LabelFrame(main_window, text="Container")
frame_1.grid(row=0, column=0, padx=padx, pady=pady)

frame_4 = tk.Frame(frame_1)
frame_4.grid(row=0, column=0, padx=padx, pady=pady)

tree_1_scrollbar = tk.Scrollbar(frame_4)
tree_1_scrollbar.grid(row=0, column=1, sticky='ns')
tree_1 = ttk.Treeview(frame_4, yscrollcommand=tree_1_scrollbar.set, selectmode="browse")
tree_1.grid(row=0, column=0, sticky='ns')

tree_1['columns'] = ("col1", "col2", "col3")
tree_1.column("#0", width=0, stretch=tk.NO)
tree_1.column("col1", anchor=tk.E, width=40)
tree_1.column("col2", anchor=tk.W, width=70)
tree_1.column("col3", anchor=tk.W, width=170)

tree_1.heading("col1", text="Id", anchor=tk.CENTER)
tree_1.heading("col2", text="Weight", anchor=tk.CENTER)
tree_1.heading("col3", text="Destination", anchor=tk.CENTER)

frame_2 = tk.Frame(frame_1)
frame_2.grid(row=1, column=0, padx=padx, pady=pady)
label_1 = tk.Label(frame_2, text="Id")
label_1.grid(row=1, column=1, padx=padx, pady=pady)
label_2 = tk.Label(frame_2, text="Weight")
label_2.grid(row=1, column=2, padx=padx, pady=pady)
label_3 = tk.Label(frame_2, text="Destination")
label_3.grid(row=1, column=3, padx=padx, pady=pady)
label_4 = tk.Label(frame_2, text="Weather")
label_4.grid(row=1, column=4, padx=padx, pady=pady)

entry_1 = tk.Entry(frame_2, width=5)
entry_1.grid(row=2, column=1, padx=padx, pady=pady)
entry_2 = tk.Entry(frame_2, width=12)
entry_2.grid(row=2, column=2, padx=padx, pady=pady)
entry_3 = tk.Entry(frame_2, width=22)
entry_3.grid(row=2, column=3, padx=padx, pady=pady)
entry_4 = tk.Entry(frame_2, width=15)
entry_4.grid(row=2, column=4, padx=padx, pady=pady)

frame_3 = tk.Frame(frame_1)
frame_3.grid(row=3, column=0, padx=padx, pady=pady)

button_1 = tk.Button(frame_3, text="Create")
button_1.grid(row=1, column=1, padx=padx, pady=pady)
button_2 = tk.Button(frame_3, text="Update")
button_2.grid(row=1, column=2, padx=padx, pady=pady)
button_3 = tk.Button(frame_3, text="Delete")
button_3.grid(row=1, column=3, padx=padx, pady=pady)
button_4 = tk.Button(frame_3, text="Clear Entry Boxes", command=lambda: button_clear_entry_boxes())
button_4.grid(row=1, column=4, padx=padx, pady=pady)

if __name__ == "__main__":
    main_window.mainloop()