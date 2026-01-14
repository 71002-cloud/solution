import tkinter as tk
from PIL import Image, ImageTk
from morris import Miner

morris = Miner()
def game_step():
    if not morris.dead() and morris.turn < 1000:
        morris.turn += 1

        if morris.sleepiness > 90:
            morris.sleep()
            action = "Morris sleeps"
        elif morris.thirst > 90 and morris.whisky > 0:
            morris.drink()
            action = "Morris drinks"
        elif morris.hunger > 90 and morris.gold >= 2:
            morris.eat()
            action = "Morris eats"
        elif morris.whisky < 5 and morris.gold >= 1 and morris.turn < 976:
            morris.buy_whisky()
            action = "Buys whisky"
        else:
            morris.mine()
            action = "Morris mines"

        update_visuel()

        print(action)
        print("--------------------------------------------------------------------------------")
        main_window.after(100, game_step)

def update_visuel():
    show_sleep = str(morris.sleepiness) + '/100'
    show_thirst = str(morris.thirst) + '/100'
    show_hunger = str(morris.hunger) + '/100'
    show_turn = 'Turn: ' + str(morris.turn)

    label_2_2.config(text=morris.gold)
    label_2.config(text=show_turn)
    label_img_2.config(text=morris.whisky)
    label_5_1.config(text=show_sleep)
    label_5_2. config(text=show_thirst)
    label_5_3.config(text=show_hunger)


    if morris.whisky == 0:
        label_img_2.config(text="", image=img_morris_tk)
    elif morris.whisky > 0:
        label_img_2.config(text=morris.whisky, image=img_morris_whisky_tk)

"""
List of sizes
Window:        1000 x 600
Panels:        480 x 500
Character:     250 x 300
Icons:         40 x 40
Bottle:        40 x 80
Fonts:         20–28 px
Padding:       20 px
"""

fg = '#000000'
wfg= '#ffffff'
bg = '#F3F3F3'
activebackground = '#D0D0D0'
activeforeground = '#000000'

font = ('Arial', 20)
mfont = ('Arial', 28)
witdh = 8
pwitdh = 480
pheight = 500
padx = 2
pady = 2

main_window = tk.Tk()
main_window.title('Morris D Miner')
main_window.geometry('1000x600')

#Img
def load_image(path, size):
    try:
        img = Image.open(path).resize(size)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Failed to load {path}: {e}")
        return None

img_money_tk = load_image("penge_img.png", (80,80))
img_sleep_tk = load_image("sleep_img.png", (80,80))
img_thirst_tk = load_image("water.png", (80,80))
img_hunger_tk = load_image("burger.png", (80,80))

#Morris img
img_morris_tk = load_image("morris.png", (250, 300))
img_morris_whisky_tk = load_image("morris_whisky.png", (250, 300))

#Main window
label_1 = tk.Label(main_window, text="Morris", width=witdh, font=mfont, fg=fg)
label_1.grid(row=0, column=0, sticky='nsew', pady=pady, padx=padx)
frame_1 = tk.Frame(main_window)
frame_1.grid(row=1, column=0, sticky='nsew', pady=pady, padx=padx)
frame_2 = tk.Frame(main_window)
frame_2.grid(row=2, column=0, sticky='nsew', pady=pady, padx=padx)

#Frame_2
label_img_1 = tk.Label(frame_2, image=img_money_tk)
label_img_1.grid(row=0, column=0, sticky='nsew', pady=pady, padx=padx)
label_2_2 = tk.Label(frame_2, text="", width=witdh+10, font=font, fg=fg)
label_2_2.grid(row=0, column=1, sticky='nsew', pady=pady, padx=padx)

#Frame_1
frame_3 = tk.Frame(frame_1, width=pwitdh, height=pheight)
frame_3.grid(row=0, column=0, sticky='nsew', pady=pady, padx=padx)
frame_4 = tk.Frame(frame_1, width=pwitdh, height=pheight)
frame_4.grid(row=0, column=1, sticky='nsew', pady=pady, padx=padx)

#frame_3
label_2 = tk.Label(frame_3, text="", width=witdh, font=font, fg=fg)
label_2.grid(row=0, column=0, sticky='nsew', pady=pady, padx=padx)
frame_5 = tk.Frame(frame_3)
frame_5.grid(row=1, column=0, sticky='nsew', pady=pady, padx=padx)

#frame_5
label_img_5_1 = tk.Label(frame_5, image=img_sleep_tk)
label_img_5_1.grid(row=0, column=0, sticky='nsew', pady=pady, padx=padx)
label_5_1 = tk.Label(frame_5, text="", width=witdh, font=font, fg=fg)
label_5_1.grid(row=0, column=1, sticky='nsew', pady=pady, padx=padx)

label_img_5_2 = tk.Label(frame_5, image=img_thirst_tk)
label_img_5_2.grid(row=1, column=0, sticky='nsew', pady=pady, padx=padx)
label_5_2 = tk.Label(frame_5, text="", width=witdh, font=font, fg=fg)
label_5_2.grid(row=1, column=1, sticky='nsew', pady=pady, padx=padx)

label_img_5_3 = tk.Label(frame_5, image=img_hunger_tk)
label_img_5_3.grid(row=2, column=0, sticky='nsew', pady=pady, padx=padx)
label_5_3 = tk.Label(frame_5, text="", width=witdh, font=font, fg=fg)
label_5_3.grid(row=2, column=1, sticky='nsew', pady=pady, padx=padx)

#frmae_4
label_img_2 = tk.Label(frame_4, image=img_morris_tk, text="5", font=font, fg=wfg, compound="center", anchor="nw")
label_img_2.grid(row=0, column=0, sticky='nsew', pady=pady, padx=padx)

if __name__ == "__main__":
    main_window.after(100, game_step)
    main_window.mainloop()