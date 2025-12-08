"""
Opgave "GUI step 1":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

--------

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2010.png

--------

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""

import tkinter as tk

padx = 20
pady = 8

main_window = tk.Tk()
main_window.title('My first GUI')
main_window.geometry('500x500')

frame_1 = tk.LabelFrame(main_window, text="Container")
frame_1.grid(row=0, column=0, padx=padx, pady=pady)
label_1 = tk.Label(frame_1, text="Id", justify="center")
label_1.grid(row=1, column=1, padx=padx, pady=pady)
entry_1 = tk.Entry(frame_1, width=4, justify="center")
entry_1.grid(row=2, column=1, padx=padx, pady=pady)
entry_1.insert(0, "")
button_1 = tk.Button(frame_1, text="Create", justify="center")
button_1.grid(row=3, column=1, padx=padx, pady=pady)

if __name__ == "__main__":
    main_window.mainloop()