import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry1.get()
    if task:
        listbox1.insert(tk.END, task)
        entry1.delete(0, tk.END)
    else:
        messagebox.showwarning("Uyarı", "Lütfen bir görev girin.")

def complete_task():
    try:
        completed_task = []
        selected_task_index = listbox1.curselection()[0]
        task_text = listbox1.get(selected_task_index)
        completed_task.append(task_text)
        listbox2.insert(tk.END,completed_task)
        listbox1.delete(selected_task_index)

    except IndexError:
        messagebox.showwarning("Uyarı", "Lütfen tamamlanmış olarak işaretlenecek bir görev seçin.")

def delete_task():
    try:
        selected_task_index = listbox1.curselection()[0]
        listbox1.delete(selected_task_index)

    except IndexError:
        messagebox.showwarning("Uyarı", "Lütfen silinecek bir görev seçin.")

def clear_tasks():
    listbox1.delete(0, tk.END)
    listbox2.delete(0,tk.END)

def save_and_exit():
    tasks = listbox1.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    root.destroy()

# Ana pencere oluştur
root = tk.Tk()
root.title("To-Do List Uygulaması")
root.geometry("400x400")
root.configure(bg="#48CAE4")

# Görev ekleme alanı
label1 = tk.Label(root, text="Eklemek İstediğiniz Görevi Giriniz: ", bg="#48CAE4", fg="Black")
label1.place(x=110, y=10)
entry1 = tk.Entry(root, width=40)
entry1.place(x=80, y=35)
label2 = tk.Label(root, text=" Eklenen Görevler ", bg="#023E8A", fg="White")
label2.place(x=60,y=125)
label3 = tk.Label(root,text=" Tamamlanan Görevler ", bg="#023E8A", fg="White")
label3.place(x=230,y=125)

# Ekleme, Silme, Tamamlama ve Temizleme düğmeleri
button_color = "#0077B6"
text_color = "White"
add_button = tk.Button(root, text=" Ekle ", command=add_task, bg=button_color, fg=text_color)
add_button.place(x=50,y=70)
complete_button = tk.Button(root, text=" Tamamlandı ", command=complete_task, bg=button_color, fg=text_color)
complete_button.place(x=120,y=70)
delete_button = tk.Button(root, text="   Sil   ", command=delete_task, bg=button_color, fg=text_color)
delete_button.place(x=230,y=70)
clear_button = tk.Button(root, text=" Temizle ", command=clear_tasks, bg=button_color, fg=text_color)
clear_button.place(x=300,y=70)

# Veriyi kaydet ve çık düğmesi
save_exit_button = tk.Button(root, text="Kaydet ve Çık", command=save_and_exit, bg=button_color, fg=text_color)
save_exit_button.place(x=160,y=360)

# Görev listesi
listbox1 = tk.Listbox(root, selectmode=tk.SINGLE, height=12, width=30, bg="#90E0EF")  # Görev listesinin listbox'ı
listbox1.place(x=20, y=150)
listbox2 = tk.Listbox(root , selectmode=tk.SINGLE, height=12, width=30, bg="#90E0EF") # Tamamlanan listenin listbox'ı
listbox2.place(x=200 , y=150)


# Kayıtlı görevleri yükle
try:
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
        for task in tasks:
            listbox1.insert(tk.END, task.strip())
except FileNotFoundError:
    pass

# Ana döngüyü başlat
root.mainloop()
