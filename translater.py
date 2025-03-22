from tkinter import *
from tkinter import ttk, messagebox
import googletrans
from googletrans import Translator
import asyncio
import time
import sys ,os
root=Tk()
root.title("Google Translator 2.0")
root.geometry("1080x400")
root.resizable(False, False)
root.configure(background="white")

def resource_path(relative_path):
    """ Get the absolute path for bundled resources when using PyInstaller """
    if getattr(sys, 'frozen', False):  # Check if running as EXE
        base_path = sys._MEIPASS  # PyInstaller temp folder
    else:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def label_change():
    c=combo1.get()
    c1=combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1) 
    root.after(1000, label_change)


def translate_now():
    
    text_ = text1.get(1.0, END).strip()
    t1 = Translator()
    source=combo1.get()
    source=source.capitalize()
    desti=combo2.get()
    desti=desti.capitalize()
    if   not text_:
        messagebox.showwarning("Warning", "Please enter text to translate.")
        return
    if source not in languageV or desti not in languageV:
        messagebox.showwarning("Warning", "Please select  a valid language to translate.")
        return
    if source == desti:
        messagebox.showwarning("Warning", "Source and Destination languages are same. Please select different languages ")
        return
    
    
    async def do_translation():
        trans_text = await t1.translate(text_, src=source, dest=desti)
        text2.delete(1.0, END)
        text2.insert(END, trans_text.text)
    
    asyncio.run(do_translation())
 #icon

def clear_combobox(event, combo):
    """Clear the Combobox text when clicked and reset values."""
    combo.set("")  # Clears the text
    combo["values"] = languageV  # Reset list

# Timer dictionary to track last key press time
typing_timers = {}

def filter_combobox(event, combo, values):
    """Filter dropdown based on typing delay (500ms) and only show if 2+ letters are typed."""
    global typing_timers
    typed = combo.get().lower()

    def update_dropdown():
        if time.time() - typing_timers[combo] >= 0.5:  # 500ms delay
            if len(typed) > 1:  # Only show dropdown if user typed 2+ characters
                filtered_values = [v for v in values if typed in v.lower()]
                combo["values"] = filtered_values

                # Open dropdown without losing focus
                combo.update_idletasks()
                combo.event_generate("<Down>")
            else:
                combo["values"] = values  # Reset to full list

    # Track last keypress time
    typing_timers[combo] = time.time()
    root.after(800, update_dropdown)




image_icon=PhotoImage(file=resource_path("google_translate_icon-icons.com_72021.png"))
root.iconphoto(False,image_icon)

#arrow
arrow_image=PhotoImage(file=resource_path("arrow.png"))
image_label=Label(root,image=arrow_image,width=150)
image_label.place(x=460,y=50)


language=googletrans.LANGUAGES

languageV=list(language.values())
for i in range(len(languageV)):
    languageV[i]=languageV[i].capitalize()
    
lang1=language.keys()
# First Combobox
combo1 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="normal")
combo1.place(x=110, y=20)
combo1.set("English")
combo1.bind("<Button-1>", lambda event: clear_combobox(event, combo1))
combo1.bind("<KeyRelease>", lambda event: filter_combobox(event, combo1, languageV))
label1=Label(root, text="English", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10,y=50)

#first frame
f=Frame(root, bg="Black", bd=5)
f.place(x=10,y=118, width=440,height=210)
text1=Text(f, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0,y=0,width=430,height=200)
scrollbar1=Scrollbar(f)
scrollbar1.pack(side="right", fill='y')
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# Second Combobox
combo2 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="normal")
combo2.place(x=720, y=20)
combo2.set("Select Lanquage")
combo2.bind("<Button-1>", lambda event: clear_combobox(event, combo2))
combo2.bind("<KeyRelease>", lambda event: filter_combobox(event, combo2, languageV))
label2=Label(root, text="English", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=620,y=50)

#second frame
f1=Frame(root, bg="Black", bd=5)
f1.place(x=620, y=118, width=440, height=210)
text2=Text(f1, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0,y=0,width=430, height=200)
scrollbar2=Scrollbar(f1)
scrollbar2.pack(side="right", fill='y')
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)



#translate button
translate=Button(root, text="Translate", font=("Roboto", 15), activebackground="white", cursor="hand2",
    bd=1,width=10, height=2, bg="black", fg="white", command=translate_now)
translate.place(x=476,y=250)


label_change()
root.mainloop() 
