from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
           'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for item in range(randint(8, 10))]
    password_symbols = [choice(symbols) for item in range(randint(2, 4))]
    password_numbers = [choice(numbers) for item in range(randint(2, 4))]

    password_list = password_letters+ password_symbols+password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    box_password.insert(0, password)
    pyperclip.copy(password) # Copied to the clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = box_website.get()
    email = box_email.get()
    password = box_password.get()

    if len(website)== 0 or len(password)==0:
        messagebox.showinfo(title="Oops", message="Please make sure you fill all the fields")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                               f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                box_website.delete(0, END)
                box_password.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady= 50)

#Canvas
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
label_website = Label(text="Website:")
label_website.grid(row=1, column =0)
label_email= Label(text="Email/Username:")
label_email.grid(row=2, column =0)
label_password = Label(text="Password:")
label_password.grid(row=3, column =0)

# Entries
box_website = Entry(width=35)
box_website.grid(row=1, column =1, columnspan=2)
box_website.focus()
box_email = Entry(width=35)
box_email.grid(row=2, column =1, columnspan=2)
box_email.insert(0, "riyamail@gmail.com")
box_password = Entry(width=21)
box_password.grid(row=3, column=1)

# Buttons
button_generate = Button(text="Generate Password", command=generate_password)
button_generate.grid(row=3, column=2)
button_add = Button(text= "Add", width=36, command=save)
button_add.grid(row=4, column=1,columnspan=2)

window.mainloop()
