"""Opgave "Calculator with GUI"

Løs opgave 0700_calculator_exercise.py med en GUI

Kopier denne fil til din egen løsningsmappe. Skriv din løsning i kopien.

Hvis du går i stå, spørg Google, andre elever, en AI eller læreren.

Når dit program er færdigt, skub det til dit GitHub-repository.
"""
import tkinter as tk

number = []
ops = []
count = 0
string = ""

def numbers(num):
    global string
    if string == "" and num == 0:
        return
    elif string == "" and num == ",":
        string = "0,"
        label_1.config(text=string)
    else:
        num = str(num)
        string += num
        label_1.config(text=string)

def plus_minus():
    global string
    if string == "":
        return
    if string[0] == "-":
        string = string[1:]
        label_1.config(text=string)
    else:
        string = "-" + string
        label_1.config(text=string)


def op(symbol):
    global number, ops, string, count
    if string == "":
        return
    number.append(string)
    string = ""
    ops.append(symbol)
    count += 1

def resault():
    global number, ops, string, count

    if not string == "":
        number.append(string)

    line = f""
    print(number)
    print(ops)
    print(count)

    for i in range(len(number)):
        line += number[i]
        if i < len(ops):
            line += ops[i]

    print(line)

    try:
        line = line.replace(",", ".")
        result = eval(line)
        label_1.config(text=str(result))
    except Exception as e:
        label_1.config(text="Error")

    string = ""
    ops = []
    number = []
    count = 0

def delete_last():
    global string
    string = string[:-1]
    if string == "":
        label_1.config(text="0")
    else:
        label_1.config(text=string)

def ce():
    global string
    string = ""
    label_1.config(text="0")

def c():
    global string, number, ops, count
    string = ""
    number = []
    ops = []
    count = 0
    label_1.config(text="0")

main_window = tk.Tk()
main_window.title('Das lommeregner')
main_window.geometry('500x500')

fg = '#000000'
bg = '#F3F3F3'
activebackground = '#D0D0D0'
activeforeground = '#000000'

fg2 = '#000000'
bg2 = '#E0E0E0'
activebackground2 = '#C0C0C0'
activeforeground2 = '#000000'

font = ('Arial', 12)
witdh = 8
padx = 2
pady = 2

label_1 = tk.Label(main_window, text='0', width=witdh*4, font=font, fg=fg, bg=bg, relief="solid", bd=2)
label_1.grid(row=0, column=1, sticky='nsew', pady=pady, padx=padx)

frame_1 = tk.Frame(main_window)
frame_1.grid(row=2, column=1)

button_1 = tk.Button(frame_1, text='1', bd=0, bg=bg, activeforeground=activeforeground, activebackground=activebackground, font=font, fg=fg, width=witdh, command=lambda :numbers(1))
button_1.grid(row=1, column=1, sticky='nsew', pady=pady, padx=padx)
button_2 = tk.Button(frame_1, text='2', bd=0, bg=bg, activeforeground=activeforeground, activebackground=activebackground, font=font, fg=fg, width=witdh, command=lambda :numbers(2))
button_2.grid(row=1, column=2, sticky='nsew', pady=pady, padx=padx)
button_3 = tk.Button(frame_1, text='3', bd=0, bg=bg, activeforeground=activeforeground, activebackground=activebackground, font=font, fg=fg, width=witdh, command=lambda :numbers(3))
button_3.grid(row=1, column=3, sticky='nsew', pady=pady, padx=padx)
button_4 = tk.Button(frame_1, text='4', bd=0, bg=bg, activeforeground=activeforeground, activebackground=activebackground, font=font, fg=fg, width=witdh, command=lambda :numbers(4))
button_4.grid(row=2, column=1, sticky='nsew', pady=pady, padx=padx)
button_5 = tk.Button(frame_1, text='5', bd=0, bg=bg, activeforeground=activeforeground, activebackground=activebackground, font=font, fg=fg, width=witdh, command=lambda :numbers(5))
button_5.grid(row=2, column=2, sticky='nsew', pady=pady, padx=padx)
button_6 = tk.Button(frame_1, text='6', bd=0, bg=bg, activeforeground=activeforeground, activebackground=activebackground, font=font, fg=fg, width=witdh, command=lambda :numbers(6))
button_6.grid(row=2, column=3, sticky='nsew', pady=pady, padx=padx)
button_7 = tk.Button(frame_1, text='7', bd=0, bg=bg, activeforeground=activeforeground, activebackground=activebackground, font=font, fg=fg, width=witdh, command=lambda :numbers(7))
button_7.grid(row=3, column=1, sticky='nsew', pady=pady, padx=padx)
button_8 = tk.Button(frame_1, text='8', bd=0, bg=bg, activeforeground=activeforeground, activebackground=activebackground, font=font, fg=fg, width=witdh, command=lambda :numbers(8))
button_8.grid(row=3, column=2, sticky='nsew', pady=pady, padx=padx)
button_9 = tk.Button(frame_1, text='9', bd=0, bg=bg, activeforeground=activeforeground, activebackground=activebackground, font=font, fg=fg, width=witdh, command=lambda :numbers(9))
button_9.grid(row=3, column=3, sticky='nsew', pady=pady, padx=padx)
button_11 = tk.Button(frame_1, text='0', bd=0, bg=bg, activeforeground=activeforeground, activebackground=activebackground, font=font, fg=fg, width=witdh, command=lambda :numbers(0))
button_11.grid(row=4, column=2, sticky='nsew', pady=pady, padx=padx)

button_10 = tk.Button(frame_1, text='+/-', bd=0, bg=bg, activeforeground=activeforeground, activebackground=activebackground, font=font, fg=fg, width=witdh, command=lambda :plus_minus())
button_10.grid(row=4, column=1, sticky='nsew', pady=pady, padx=padx)
button_12 = tk.Button(frame_1, text=',', bd=0, bg=bg, activeforeground=activeforeground, activebackground=activebackground, font=font, fg=fg, width=witdh, command=lambda :numbers(','))
button_12.grid(row=4, column=3, sticky='nsew', pady=pady, padx=padx)

button_13 = tk.Button(frame_1, text='/', bd=0, bg=bg2, activeforeground=activeforeground2, activebackground=activebackground2, font=font, fg=fg2, width=witdh, command=lambda :op('/'))
button_13.grid(row=1, column=4, sticky='nsew', pady=pady, padx=padx)
button_14 = tk.Button(frame_1, text='*', bd=0, bg=bg2, activeforeground=activeforeground2, activebackground=activebackground2, font=font, fg=fg2, width=witdh, command=lambda :op('*'))
button_14.grid(row=2, column=4, sticky='nsew', pady=pady, padx=padx)
button_15 = tk.Button(frame_1, text='-', bd=0, bg=bg2, activeforeground=activeforeground2, activebackground=activebackground2, font=font, fg=fg2, width=witdh, command=lambda :op('-'))
button_15.grid(row=3, column=4, sticky='nsew', pady=pady, padx=padx)
button_16 = tk.Button(frame_1, text='+', bd=0, bg=bg2, activeforeground=activeforeground2, activebackground=activebackground2, font=font, fg=fg2, width=witdh, command=lambda :op('+'))
button_16.grid(row=4, column=4, sticky='nsew', pady=pady, padx=padx)

frame2 = tk.Frame(main_window)
frame2.grid(row=1, column=1)

button_17 = tk.Button(frame2, text='=', bd=0, bg='blue', activeforeground='blue', activebackground='white', font=font, fg='white', width=witdh, command=lambda :resault())
button_17.grid(row=1, column=1, sticky='nsew', pady=pady, padx=padx)
button_18 = tk.Button(frame2, text='CE', bd=0, bg=bg2, activeforeground=activeforeground2, activebackground=activebackground2, font=font, fg=fg2, width=witdh, command=lambda :ce())
button_18.grid(row=1, column=2, sticky='nsew', pady=pady, padx=padx)
button_19 = tk.Button(frame2, text='C', bd=0, bg=bg2, activeforeground=activeforeground2, activebackground=activebackground2, font=font, fg=fg2, width=witdh, command=lambda :c())
button_19.grid(row=1, column=3, sticky='nsew', pady=pady, padx=padx)
button_20 = tk.Button(frame2, text='Delete', bd=0, bg=bg2, activeforeground=activeforeground2, activebackground=activebackground2, font=font, fg=fg2, width=witdh, command=lambda :delete_last())
button_20.grid(row=1, column=4, sticky='nsew', pady=pady, padx=padx)

if __name__ == "__main__":
    main_window.mainloop()