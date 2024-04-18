import customtkinter 

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

root = customtkinter.CTk()
root.title("Password Sorcerer")
root.geometry("500x350")

def generate_password(length, has_lowercase_letters):
    generated_password.set("testpassword")


frame = customtkinter.CTkFrame(master = root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

frame.grid_columnconfigure(0, weight=1)

password_length = customtkinter.IntVar(master=frame, value = 4)
generated_password = customtkinter.StringVar(master=frame, value='')
is_lowercase_letters_checked = customtkinter.BooleanVar(master=frame, value=True)

label = customtkinter.CTkLabel(master=frame, text="Password Sorcerer", font=("Roboto", 24))
label.grid(row=0,column=0, sticky="ew", columnspan=2)

length_label = customtkinter.CTkLabel(master=frame, text="Password Length")
length_label.grid(row=1,column=0, sticky="ew", columnspan=2, pady=(30,0))

length_slider = customtkinter.CTkSlider(master=frame, from_=4, to=36, number_of_steps=32,variable=password_length)
length_slider.grid(row=2,column=0, sticky="ew",padx=20, pady=(0,20))

length_entry = customtkinter.CTkEntry(master=frame, textvariable=password_length, width=50)
length_entry.grid(row=2,column=1, sticky="w", pady=(0,20))

# Checkboxes for upper & lower case letters, numbers, & symbols
lowercase_checkbox = customtkinter.CTkCheckBox(master=frame, text="Lowercase Letters?", variable=is_lowercase_letters_checked)
lowercase_checkbox.grid(row=3,column=1, sticky="ew",columnspan=2, pady=(0,20))

button = customtkinter.CTkButton(master=frame, text="Generate Password", command=lambda : generate_password(password_length, is_lowercase_letters_checked))
button.grid(row=4,column=0, columnspan=2)

# Holdover from tutorial for basic CTKCheckBox code
# checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
# checkbox.pack(pady=12, padx=10)

# Show password with icon to copy the text to clipboard.
generated_password_label = customtkinter.CTkLabel(master=frame, textvariable=generated_password)
generated_password_label.grid(row=5,column=0, sticky="ew", columnspan=2, pady=(30,0))

root.mainloop()