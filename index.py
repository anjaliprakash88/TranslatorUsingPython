from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

# Initialize the main window
root = Tk()
root.title("Google Translator")
root.geometry("1080x400")
root.resizable(False, False)
root.configure(background="white")

# Function to update the language labels based on combo box selection
def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000, label_change)

# Function to handle translation
def translate_now():
    try:
        text_ = text1.get(1.0, END).strip()  # Get the input text
        c2 = combo1.get()  # Input language
        c3 = combo2.get()  # Output language

        if text_:  # Proceed only if text is entered
            # Initialize the Translator
            translator = Translator()

            # Detect the language of the input text using googletrans
            detected_lang = translator.detect(text_).lang

            # Find target language code based on the selection
            target_lang_code = None
            for lang_code, lang_name in language.items():
                if lang_name == c3:
                    target_lang_code = lang_code
                    break

            if target_lang_code:
                # Translate the text using Google Translate API
                translated_text = translator.translate(text_, src=detected_lang, dest=target_lang_code).text
                text2.delete(1.0, END)  # Clear the output field
                text2.insert(END, translated_text)  # Insert translated text
            else:
                messagebox.showerror("Error", "Target language not found!")
        else:
            messagebox.showerror("Error", "Please enter text to translate!")
    except Exception as e:
        messagebox.showerror("Error", f"Translation error: {str(e)}")

# GUI elements
# Set up images (ensure the images exist in the working directory)
try:
    image_icon = PhotoImage(file="st.png")
    root.iconphoto(False, image_icon)

    arrow_image = PhotoImage(file="arrow.png")
    image_label = Label(root, image=arrow_image, width=200)
    image_label.place(x=420, y=50)
except Exception as e:
    messagebox.showerror("Error", f"Image loading error: {str(e)}")

# Language dictionary
language = LANGUAGES
languageV = list(language.values())

# ComboBox for input language
combo1 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo1.place(x=110, y=20)
combo1.set('ENGLISH')

label1 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="white", width=15, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

# Input text field
f = Frame(root, bg="Black", bd=5)
f.place(x=10, y=118, width=370, height=210)

text1 = Text(f, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=350, height=200)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right", fill="y")
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# ComboBox for output language
combo2 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo2.place(x=730, y=20)
combo2.set('SELECT LANGUAGE')

label2 = Label(root, text="SELECT LANGUAGE", font="segoe 30 bold", bg="white", width=16, bd=5, relief=GROOVE)
label2.place(x=670, y=50)

# Output text field
f1 = Frame(root, bg="Black", bd=5)
f1.place(x=670, y=118, width=370, height=210)

text2 = Text(f1, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=350, height=200)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side="right", fill="y")
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

# Translate button
translate = Button(root, text="Translate", font="Roboto 15 bold italic", activebackground="purple", cursor="hand2", bd=5, bg='red', fg="white", command=translate_now)
translate.place(x=470, y=300)

# Trigger label change function
label_change()

# Start the main loop
root.configure(bg="white")
root.mainloop()
