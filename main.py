from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]

    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = web_entry.get()
    password = password_entry.get()
    username = username_entry.get()
    data_dict = {
        website: {
            "password": password,
            "username": username,
        }
    }

    if website == "" or password == "" or username == "":
        messagebox.showinfo(title="Error", message="Don't leave any fields Empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(data_dict, data_file, indent=4)
        else:
            data.update(data_dict)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)


def find_password():
    website = web_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="NoData", message="File does not exist create one! Enter details and click add!")
    else:
        if website in data:
            messagebox.showinfo(title=website, message=f"Email: {data[website]['username']}\n"
                                                       f"Password: {data[website]['password']}")
        else:
            messagebox.showinfo(title="Error", message=f"There are no details for {website} website.")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager🔑")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

web_entry = Entry(width=36)
web_entry.grid(row=1, column=1)
web_entry.focus()

username_entry = Entry(width=36)
username_entry.grid(row=2, column=1)
username_entry.insert(0, "gunaraj721@gmail.com")

password_entry = Entry(width=36)
password_entry.grid(row=3, column=1)

search_btn = Button(text="SEARCH", width=8, command=find_password)
search_btn.grid(row=1, column=2)

add_btn = Button(text="ADD", width=40)
add_btn.config(command=save)
add_btn.grid(row=4, column=1, columnspan=2)

generate_btn = Button(text="GENERATE", command=generate_password)
generate_btn.grid(row=3, column=2)

window.mainloop()
