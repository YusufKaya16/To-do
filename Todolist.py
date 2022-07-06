from tkinter import *
from tkinter import messagebox
import sys


def dosya_ac(veri):

    dosya = open("C:\\Users\\Yusuf KAYA\\PycharmProjects\\pythonProject1\\To-Doo.txt", "a",
                 encoding="utf-8")
    dosya.write("-" + veri + "\n")
    dosya.close()


def etkinlik_ekle(event=None):

    task = my_entry.get()
    if task != "":
        liste_box.insert(END, task)
        my_entry.delete(0, "end")
        dosya_ac(task)
        messagebox.showinfo("Bilgilendirme", "Etkinlik eklenmiştir :)")
    else:
        messagebox.showwarning("Uyarı", "Hiçbir etkinlik girilmedi!")


def etkinlik_sil(event=None):
    liste_box.delete(ANCHOR)


def exit(event=None):
    sys.exit(master)


# Pencere
master = Tk()
master.geometry("800x500+400+200")
master.title("To-Do List")
master.config(bg="#1e90ff")
master.resizable(height=False, width=False)
master.bind("<Escape>", exit)

# Liste kutusu çerçevesi
frame = Frame(master)
frame.place(x=480, y=60, width=280, height=350)

label = Label(master, text="Yapılacaklar Listesi", fg="dark red", bg="#1e90ff", font="Times 18")
label.place(x=525, y=20)

# Liste kutusu
liste_box = Listbox(frame,
                    width=22,
                    font="Times 18",
                    bg="Light Gray",
                    bd=0,
                    fg="Forest Green",
                    highlightthickness=0,
                    selectbackground="#a6a6a6",
                    activestyle="none")

liste_box.bind("<Delete>", etkinlik_sil)
liste_box.pack(side=LEFT, fill=BOTH)

# Kaydırma çubuğu
scroll_bar = Scrollbar(frame)
scroll_bar.pack(side=RIGHT, fill=BOTH)

liste_box.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=liste_box.yview)

# veri girişi
karsilama_metni ="Etkinlik giriniz.."
my_entry = Entry(master, font="Times 24")
my_entry.config(fg="black", bd=3, highlightthickness=2)
my_entry.bind("<Return>", etkinlik_ekle)
my_entry.place(x=80, y=90)
my_entry.insert(END, karsilama_metni)

# Buton alanı
buton_frame = Frame(master)
buton_frame.place(x=150, y=190)


# Yeni etkinlik ekleme
ekle_buton = Button(buton_frame,
                       text="Ekle",
                       font="times 14",
                       bg="blue",
                       pady=10,
                       padx=20,
                       command=etkinlik_ekle)

ekle_buton.bind("<Return>", etkinlik_ekle)
ekle_buton.pack(side=LEFT, expand=YES, fill=BOTH)

# Etkinlik silme
sil_buton = Button(buton_frame,
                       text="Sil",
                       font="times 14",
                       bg="Blue",
                       padx=30,
                       pady=10,
                       command=etkinlik_sil)

sil_buton.bind("<Delete>", etkinlik_sil)
sil_buton.pack(side=LEFT, expand=YES, fill=BOTH)

master.mainloop()