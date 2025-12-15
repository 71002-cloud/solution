import tkinter as tk
from tkinter import ttk
from plusbus_data import Kunder, Rejser, Bookinger, engine
from sqlalchemy.orm import Session
from sqlalchemy import select

# ------------------ Data ------------------

def fetch_(class_):
    with Session(engine) as session:
        result = session.execute(select(class_)).scalars().all()
        return result

def add_kunder(efternavn, kontakt, tree):
    with Session(engine) as session:
        new_kunder = Kunder(efternavn=efternavn, kontakt=kontakt)
        session.add(new_kunder)
        session.commit()
    refresh_tree(tree, Kunder)

def add_rejser(rute, dato, pladser, tree):
    with Session(engine) as session:
        new_rejser = Rejser(rute=rute, dato=dato, pladser=pladser)
        session.add(new_rejser)
        session.commit()
    refresh_tree(tree, Rejser)

def add_bookinger(kunde, rejse, pladser, tree):
    with Session(engine) as session:
        new_booking = Bookinger(kunde=kunde, rejse=rejse, pladser=pladser)
        session.add(new_booking)
        session.commit()
    refresh_tree(tree, Bookinger)


def refresh_tree(tree, class_):
    data = fetch_(class_)
    populate_tree(tree, data)
    entry_refresh()

def clear_tree(tree):
    for item in tree.get_children():
        tree.delete(item)

def populate_tree(tree, data):
    clear_tree(tree)
    for obj in data:
        tree.insert("", "end", values=obj.convert_to_tuple())

# ------------------ Buttons funtiocns ------------------

def kunder_opret():
    efternavn = entry_1_1.get()
    kontakt = entry_1_2.get()
    tree = tree_1
    add_kunder(efternavn, kontakt, tree)
    button_clear_entry_boxes()

def button_clear_entry_boxes():
    entry_1_1.delete(0, "end")
    entry_1_2.delete(0, "end")

def opdate_kunde():
    selceted_item = tree_1.selection()
    if not selceted_item:
        return
    item_id = selceted_item[0]
    efternavn = entry_1_1.get()
    kontakt = entry_1_2.get()

    with Session(engine) as session:
        kunde = session.get(Kunder, int(tree_1.item(item_id)['values'][0]))
        if kunde:
            kunde.efternavn = efternavn
            kunde.kontakt = kontakt
            session.commit()

    refresh_tree(tree_1, Kunder)
    button_clear_entry_boxes()

def slet_kunde():
    selceted_item = tree_1.selection()
    if not selceted_item:
        return
    item_id = selceted_item[0]

    with Session(engine) as session:
        kunde_id = int(tree_1.item(item_id)['values'][0])
        kunde = session.get(Kunder, kunde_id)
        if kunde:
            session.delete(kunde)
            session.commit()

    refresh_tree(tree_1, Kunder)

def rejser_clear_entry_boxes():
    entry_2_1.delete(0, "end")
    entry_2_2.delete(0, "end")
    entry_2_3.delete(0, "end")

def rejser_opret():
    rute = entry_2_1.get()
    dato = entry_2_2.get()
    pladser = entry_2_3.get()
    tree = tree_2

    try:
        pladser = int(pladser)
    except ValueError:
        print("pladser error")
        return

    add_rejser(rute, dato, pladser, tree)
    rejser_clear_entry_boxes()

def opdate_rejser():
    selceted_item = tree_2.selection()
    if not selceted_item:
        return
    item_id = selceted_item[0]
    rute = entry_2_1.get()
    dato = entry_2_2.get()
    pladser = entry_2_3.get()

    try:
        pladser = int(pladser)
    except ValueError:
        print("pladser error")
        return

    with Session(engine) as session:
        rejse = session.get(Rejser, int(tree_2.item(item_id)['values'][0]))
        if rejse:
            rejse.rute = rute
            rejse.dato = dato
            rejse.pladser = pladser
            session.commit()

    refresh_tree(tree_2, Rejser)
    rejser_clear_entry_boxes()

def slet_rejser():
    selceted_item = tree_2.selection()
    if not selceted_item:
        return
    item_id = selceted_item[0]

    with Session(engine) as session:
        rejse_id = int(tree_2.item(item_id)['values'][0])
        rejse = session.get(Rejser, rejse_id)
        if rejse:
            session.delete(rejse)
            session.commit()

    refresh_tree(tree_1, Rejser)
    rejser_clear_entry_boxes()

def slet_booking():
    selceted_item = tree_3.selection()
    if not selceted_item:
        return
    item_id = selceted_item[0]

    with Session(engine) as session:
        booking_id = int(tree_3.item(item_id)['values'][0])
        booking = session.get(Bookinger, booking_id)
        if booking:
            rejse = session.execute(select(Rejser).where(Rejser.rute == booking.rejse)).scalar_one_or_none()
            if rejse:
                rejse_plads = int(rejse.pladser)
                rejse_plads += int(booking.pladser)
                rejse.pladser = rejse_plads

            session.delete(booking)
            session.commit()

    refresh_tree(tree_2, Rejser)
    refresh_tree(tree_3, Bookinger)

def opret_booking():
    kunde = entry_3_1.get()
    rejse_rute = entry_3_2.get()
    pladser = entry_3_3.get()
    tree = tree_3

    try:
        pladser = int(pladser)
    except ValueError:
        print("pladser error")
        return

    with Session(engine) as session:
        rejse = session.execute(select(Rejser).where(Rejser.rute == rejse_rute)).scalar_one_or_none()
        rpladser = int(rejse.pladser)

        if rpladser >= pladser:
            add_bookinger(kunde, rejse_rute, pladser, tree)
            rpladser -= pladser
            rejse.pladser = rpladser
            session.commit()
        else:
            print("pladser error")

    refresh_tree(tree_2, Rejser)
    refresh_tree(tree_3, Bookinger)
    entry_3_3.delete(0, "end")

# ------------------ THEME ------------------
COLOR_BG = "#eaf4ff"
COLOR_FRAME = "#ffffff"
COLOR_BORDER = "#c7ddf5"
COLOR_PRIMARY = "#1e88e5"
COLOR_TEXT = "#0d47a1"

PADX = 5
PADY = 3
ENTRY_WIDTH = 15

# ------------------ WINDOW ------------------
main_window = tk.Tk()
main_window.title("PlusBus")
main_window.geometry("500x500")
main_window.configure(bg=COLOR_BG)

# ------------------ SCROLLABLE CANVAS ------------------
canvas = tk.Canvas(main_window, bg=COLOR_BG, highlightthickness=0)
canvas.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(main_window, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)
main_frame = tk.Frame(canvas, bg=COLOR_BG)
canvas.create_window((0, 0), window=main_frame, anchor="nw")
main_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# ------------------ TREEVIEW STYLE ------------------
style = ttk.Style()
style.theme_use("default")
style.configure("Treeview", background="white", foreground=COLOR_TEXT, rowheight=20, fieldbackground="white")
style.configure("Treeview.Heading", background=COLOR_BORDER, foreground=COLOR_TEXT)
style.map("Treeview", background=[("selected", COLOR_PRIMARY)], foreground=[("selected", "white")])

# ================== KUNDER ==================
frame_1 = tk.LabelFrame(main_frame, text="Kunder", bg=COLOR_FRAME, fg=COLOR_TEXT, padx=8, pady=8)
frame_1.grid(row=0, column=0, padx=PADX, pady=PADY, sticky="ew")

tk.Label(frame_1, text="Efternavn:", bg=COLOR_FRAME, fg=COLOR_TEXT).grid(row=0, column=0, sticky="e", padx=PADX, pady=PADY)
entry_1_1 = tk.Entry(frame_1, width=ENTRY_WIDTH)
entry_1_1.grid(row=0, column=1, sticky="w", padx=PADX, pady=PADY)

tk.Label(frame_1, text="Kontakt:", bg=COLOR_FRAME, fg=COLOR_TEXT).grid(row=1, column=0, sticky="e", padx=PADX, pady=PADY)
entry_1_2 = tk.Entry(frame_1, width=ENTRY_WIDTH)
entry_1_2.grid(row=1, column=1, sticky="w", padx=PADX, pady=PADY)

button_1_1 = tk.Button(frame_1, text="Opret", bg=COLOR_PRIMARY, fg="white", width=8, command=lambda :kunder_opret())
button_1_1.grid(row=2, column=0, padx=PADX, pady=PADY)
button_1_2 = tk.Button(frame_1, text="Opdater", bg=COLOR_PRIMARY, fg="white", width=8, command=lambda :opdate_kunde())
button_1_2.grid(row=2, column=1, padx=PADX, pady=PADY)
button_1_3 = tk.Button(frame_1, text="Slet", bg=COLOR_PRIMARY, fg="white", width=8, command=lambda :slet_kunde())
button_1_3.grid(row=3, column=0, padx=PADX, pady=PADY)
button_1_4 = tk.Button(frame_1, text="Tøm felter", bg=COLOR_PRIMARY, fg="white", width=8, command=lambda :button_clear_entry_boxes())
button_1_4.grid(row=3, column=1, padx=PADX, pady=PADY)

tree_1 = ttk.Treeview(frame_1, columns=("id", "navn", "kontakt"), show="headings", height=3)
tree_1.grid(row=4, column=0, columnspan=2, pady=PADY, sticky="ew")
tree_1.heading("id", text="Id")
tree_1.heading("navn", text="Efternavn")
tree_1.heading("kontakt", text="Kontakt")
tree_1.column("id", width=30, anchor="center")
tree_1.column("navn", width=100, anchor="center")
tree_1.column("kontakt", width=100, anchor="center")

# ================== REJSER ==================
frame_2 = tk.LabelFrame(main_frame, text="Rejser", bg=COLOR_FRAME, fg=COLOR_TEXT, padx=8, pady=8)
frame_2.grid(row=1, column=0, padx=PADX, pady=PADY, sticky="ew")

tk.Label(frame_2, text="Rute:", bg=COLOR_FRAME).grid(row=0, column=0, sticky="e", padx=PADX, pady=PADY)
entry_2_1 = tk.Entry(frame_2, width=ENTRY_WIDTH)
entry_2_1.grid(row=0, column=1, sticky="w", padx=PADX, pady=PADY)

tk.Label(frame_2, text="Dato:", bg=COLOR_FRAME).grid(row=1, column=0, sticky="e", padx=PADX, pady=PADY)
entry_2_2 = tk.Entry(frame_2, width=ENTRY_WIDTH)
entry_2_2.grid(row=1, column=1, sticky="w", padx=PADX, pady=PADY)

tk.Label(frame_2, text="Pladser:", bg=COLOR_FRAME).grid(row=2, column=0, sticky="e", padx=PADX, pady=PADY)
entry_2_3 = tk.Entry(frame_2, width=ENTRY_WIDTH)
entry_2_3.grid(row=2, column=1, sticky="w", padx=PADX, pady=PADY)

button_2_1 = tk.Button(frame_2, text="Opret", bg=COLOR_PRIMARY, fg="white", width=8, command=lambda :rejser_opret())
button_2_1.grid(row=3, column=0, padx=PADX, pady=PADY)
button_2_2 = tk.Button(frame_2, text="Opdater", bg=COLOR_PRIMARY, fg="white", width=8, command=lambda :opdate_rejser())
button_2_2.grid(row=3, column=1, padx=PADX, pady=PADY)
button_2_3 = tk.Button(frame_2, text="Slet", bg=COLOR_PRIMARY, fg="white", width=8, command=lambda :slet_rejser())
button_2_3.grid(row=3, column=2, padx=PADX, pady=PADY)

tree_2 = ttk.Treeview(frame_2, columns=("id", "rute", "dato", "pladser"), show="headings", height=3)
tree_2.grid(row=4, column=0, columnspan=3, pady=PADY, sticky="ew")
tree_2.heading("id", text="Id")
tree_2.heading("rute", text="Rute")
tree_2.heading("dato", text="Dato")
tree_2.heading("pladser", text="Pladser")
tree_2.column("id", width=30, anchor="center")
tree_2.column("rute", width=120, anchor="center")
tree_2.column("dato", width=80, anchor="center")
tree_2.column("pladser", width=50, anchor="center")

# ================== BOOKINGER ==================
frame_3 = tk.LabelFrame(main_frame, text="Bookinger", bg=COLOR_FRAME, fg=COLOR_TEXT, padx=8, pady=8)
frame_3.grid(row=2, column=0, padx=PADX, pady=PADY, sticky="ew")

def entry_refresh():
    kunde_values = [f"{k.efternavn}" for k in fetch_(Kunder)]
    rejse_values = [f"{r.rute}" for r in fetch_(Rejser)]

    if entry_3_1:
        entry_3_1['values'] = kunde_values
    if entry_3_2:
        entry_3_2['values'] = rejse_values

tk.Label(frame_3, text="Kunde:", bg=COLOR_FRAME).grid(row=0, column=0, sticky="e", padx=PADX, pady=PADY)
entry_3_1 = ttk.Combobox(frame_3, values=[], width=ENTRY_WIDTH, state="readonly")
entry_3_1.grid(row=0, column=1, sticky="w", padx=PADX, pady=PADY)

tk.Label(frame_3, text="Rejse:", bg=COLOR_FRAME).grid(row=1, column=0, sticky="e", padx=PADX, pady=PADY)
entry_3_2 = ttk.Combobox(frame_3, values=[], width=ENTRY_WIDTH, state="readonly")
entry_3_2.grid(row=1, column=1, sticky="w", padx=PADX, pady=PADY)

tk.Label(frame_3, text="Pladser:", bg=COLOR_FRAME).grid(row=2, column=0, sticky="e", padx=PADX, pady=PADY)
entry_3_3 = tk.Entry(frame_3, width=ENTRY_WIDTH)
entry_3_3.grid(row=2, column=1, sticky="w", padx=PADX, pady=PADY)

button_3_1 = tk.Button(frame_3, text="Opret booking", bg=COLOR_PRIMARY, fg="white", width=12, command=lambda :opret_booking())
button_3_1.grid(row=3, column=0, padx=PADX, pady=PADY)
button_3_2 = tk.Button(frame_3, text="Slet booking", bg=COLOR_PRIMARY, fg="white", width=12, command=lambda :slet_booking())
button_3_2.grid(row=3, column=1, padx=PADX, pady=PADY)

tree_3 = ttk.Treeview(frame_3, columns=("id", "kunde", "rejse", "pladser"), show="headings", height=4)
tree_3.grid(row=4, column=0, columnspan=2, pady=PADY, sticky="ew")
tree_3.heading("id", text="Id")
tree_3.heading("kunde", text="Kunde")
tree_3.heading("rejse", text="Rejse")
tree_3.heading("pladser", text="Pladser")
tree_3.column("id", width=30, anchor="center")
tree_3.column("kunde", width=100, anchor="center")
tree_3.column("rejse", width=120, anchor="center")
tree_3.column("pladser", width=50, anchor="center")

# ------------------ RUN ------------------
entry_refresh()
refresh_tree(tree_1, Kunder)
refresh_tree(tree_2, Rejser)
refresh_tree(tree_3, Bookinger)

main_window.mainloop()