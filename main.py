from tkinter import *
from tkinter import messagebox
import pyperclip
from random import choice, randint, shuffle
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def random_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    if len(password_input.get()) > 1:
        password_input.delete(0, END)

    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- FIND PASSWORD     ------------------------------- #
def find_password():
    website = website_input.get()
    try:
        with open("data.json") as file_data:
            json_data = json.load(file_data)

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data file found")

    else:
        if website in json_data:
            email = json_data[website]["email"]
            password = json_data[website]["password"]

            messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No detail for {website} exist")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(email) == 0 and len(password) == 0 and len(website) == 0:
        messagebox.showerror(title="Error", message="Make sure no input field is empty")

    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_input.delete(0, END)
            email_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Passworstr(d Manager")
window.config(padx=50, pady=50)

logo_image = PhotoImage(file="logo.png", )
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=1)

website_label = Label(text="Website:")
website_label.grid(column=0, row=2)
website_input = Entry(width=35)
website_input.focus()
website_input.grid(column=1, row=2, columnspan=2)

search_button = Button(text="Search", width=10, command=find_password)
search_button.grid(column=3, row=2, padx=10)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=3)
email_input = Entry(width=35)
email_input.grid(column=1, row=3, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=4)
password_input = Entry(width=20)
password_input.grid(column=1, row=4)

genrate_password = Button(text="Genrate Password", command=random_password)

genrate_password.grid(column=2, row=4)
add_button = Button(text="ADD", width=36, command=save)

add_button.grid(column=1, row=5, columnspan=2)

window.mainloop()
