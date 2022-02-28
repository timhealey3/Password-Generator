import secrets
import string
from tkinter import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = Tk()
    # Name of program
    root.title("Password Generator")
    # size of window
    root.geometry('450x250')
    lbl = Label(root, text="Website Name")
    lbl.grid(column=0, row=0)
    lbl = Label(root, text="Password Length")
    lbl.grid(column=0, row=2)
    # Input text
    pass_limit = Entry(root, width=10, bd=0)
    pass_limit.grid(column=2, row=2)
    company = Entry(root, width=10, bd=0)
    # input company name
    company.grid(column=2, row=0)
    pass_show = Label(root, text="")
    pass_show.grid()
    pass_ret = Label(root, text="")
    pass_ret.grid(column=0, row=4)

    def clicked_gen():
        try:
            int_limit = int(pass_limit.get())
            str_company = str(company.get())
            all_letters = string.ascii_letters
            all_ints = string.digits
            generated_pass = ''.join(secrets.choice(all_ints + all_letters) for i in range(int_limit))
            pass_show.configure(text=generated_pass)
            with open("pass.txt", "a") as f:
                f.write(str_company + "\t" + generated_pass + "\n")
                f.close()
        except ValueError:
            pass_show.configure(text="Enter a Integer")
    # Retrieve function
    def clicked_ret():
        pass_ret.configure(text="")
        str_company = str(company.get())
        infile = open("pass.txt", "r")
        website_list = []
        for line in infile:
            stripped_line = line.strip()
            line_list = stripped_line.split()
            website_list.append(line_list)
        j = 0
        try:
            while j < 10:
                if str_company == (website_list[j][0]):
                    pass_ret.configure(text=website_list[j][1], relief="flat")
                j = j + 1
        except IndexError:
            pass
        infile.close()


    # button widget with red color text inside
    gen_btn = Button(root, text="Generate", fg="red", command=clicked_gen)
    # Set Button Grid
    gen_btn.grid(column=2, row=3)
    # button widget with red color text inside
    ret_btn = Button(root, text="Retrieve", fg="green", command=clicked_ret)
    # Set Button Grid
    ret_btn.grid(column=2, row=4)
    root.mainloop()
