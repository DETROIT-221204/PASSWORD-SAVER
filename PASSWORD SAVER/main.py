from tkinter import *
from tkinter import messagebox
import random

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # print("Welcome to the PyPassword Generator!")
    nr_letters= random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)
    no=nr_letters+nr_symbols+nr_numbers
    password=[]
    for i in range(nr_letters):
        password.append(random.choice(letters))
    for i in range(nr_numbers):
        password.append(random.choice(numbers))
    for i in range(nr_symbols):
        password.append(random.choice(symbols))
    random.shuffle(password)
    password = ''.join(password)
    print("Your password is :"+password)
    password_inp.insert(0,password)


def save():
    website = inp.get()
    email = email_inp.get()
    password = password_inp.get()


    if len(website)==0 or len(email)==0 or len(password)==0:
        messagebox.showinfo(title="OOPS",message="Make sure you havent left any field empty")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the detailed entered:\n Email:{email}\nPassword:{password}\n Is it okay to Save")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website}|{email}|{password}\n")  # Added newline at the end

window = Tk()
window.title("My Password Manager")
window.geometry("400x400")

lock_image = PhotoImage(file="logo.png")
canvas = Canvas(window, width=250, height=250)
canvas.create_image(150, 172, image=lock_image)
canvas.grid(row=0, column=0, columnspan=3, padx=10, pady=10)  # Changed columnspan to 3 to match button span

website_label = Label(text="WEBSITE:", font=("Arial", 10, "bold"))
website_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

inp = Entry(window)
inp.grid(row=1, column=1, padx=10, pady=10)

email_username_label = Label(text="Email/Username:", font=("Arial", 10, "bold"))
email_username_label.grid(row=2, column=0, padx=5)

email_inp = Entry(window)
email_inp.grid(row=2, column=1)

password_label = Label(text="Password", font=("Arial", 10, "bold"))
password_label.grid(row=3, column=0, padx=10)

password_inp = Entry(window)
password_inp.grid(row=3, column=1)

generate_button = Button(text="Generate Password",command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="ADD", command=save)
add_button.grid(row=4, column=0, columnspan=3, pady=10)

window.mainloop()
