import random
import string
import customtkinter 

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

root = customtkinter.CTk()
root.title("Password Sorcerer")
root.geometry("500x400")

def generate_password(length, has_lowercase_letters, has_uppercase_letters, has_numbers, has_special_characters):
    password_placeholder = []
    character_types_to_include = []
    if(has_lowercase_letters.get()):
        password_placeholder.append(random.choice(string.ascii_lowercase))
        character_types_to_include.append(0)
    if(has_uppercase_letters.get()):
        password_placeholder.append(random.choice(string.ascii_uppercase))
        character_types_to_include.append(1)
    if(has_numbers.get()):
        password_placeholder.append(random.choice(string.digits))
        character_types_to_include.append(2)
    if(has_special_characters.get()):
        password_placeholder.append(random.choice(string.punctuation))
        character_types_to_include.append(3)
    loop_range = range(length.get()-len(password_placeholder))
    for n in loop_range:
        type_of_character = character_types_to_include[random.randint(0, len(character_types_to_include)-1)]
        if type_of_character == 0:
            password_placeholder.append(random.choice(string.ascii_lowercase))
        elif type_of_character == 1:
            password_placeholder.append(random.choice(string.ascii_uppercase))
        elif type_of_character == 2:
            password_placeholder.append(random.choice(string.digits))
        else:
            password_placeholder.append(random.choice(string.punctuation))

    generated_password.set("".join(password_placeholder))


frame = customtkinter.CTkFrame(master = root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

frame.grid_columnconfigure(0, weight=1)

password_length = customtkinter.IntVar(master=frame, value = 4)
generated_password = customtkinter.StringVar(master=frame, value='')
is_lowercase_letters_checked = customtkinter.BooleanVar(master=frame, value=True)
is_uppercase_letters_checked = customtkinter.BooleanVar(master=frame, value=True)
is_numbers_checked = customtkinter.BooleanVar(master=frame, value=True)
is_special_characters_checked = customtkinter.BooleanVar(master=frame, value=True)

label = customtkinter.CTkLabel(master=frame, text="Password Sorcerer", font=("Roboto", 24))
label.grid(row=0,column=0, sticky="ew", columnspan=4, pady=(10,0))

length_label = customtkinter.CTkLabel(master=frame, text="Password Length")
length_label.grid(row=1,column=0, sticky="ew", columnspan=4, pady=(20,0))

max_password_length = 128
length_slider = customtkinter.CTkSlider(master=frame, from_=4, to=max_password_length, number_of_steps=max_password_length-4,variable=password_length)
length_slider.grid(row=2,column=0, sticky="ew",columnspan=4, padx=(20, 80), pady=(0,20))

length_entry = customtkinter.CTkEntry(master=frame, textvariable=password_length, width=50)
length_entry.grid(row=2,column=3, sticky="e", padx=20, pady=(0,20))

lowercase_checkbox = customtkinter.CTkCheckBox(master=frame, text="Lowercase Letters?", variable=is_lowercase_letters_checked)
lowercase_checkbox.grid(row=3,column=0, sticky="ew", columnspan=2, pady=(0,20), padx=20)

uppercase_checkbox = customtkinter.CTkCheckBox(master=frame, text="Uppercase Letters?", variable=is_uppercase_letters_checked)
uppercase_checkbox.grid(row=3,column=2, sticky="ew", columnspan=2, pady=(0,20), padx=20)

numbers_checkbox = customtkinter.CTkCheckBox(master=frame, text="Numbers?", variable=is_numbers_checked)
numbers_checkbox.grid(row=4,column=0, sticky="ew", columnspan=2, pady=(0,20), padx=20)

special_characters_checkbox = customtkinter.CTkCheckBox(master=frame, text="Special Characters?", variable=is_special_characters_checked)
special_characters_checkbox.grid(row=4,column=2, sticky="ew", columnspan=2, pady=(0,20), padx=20)

button = customtkinter.CTkButton(master=frame, text="Generate Password", command=lambda : generate_password(password_length, is_lowercase_letters_checked, is_uppercase_letters_checked, is_numbers_checked, is_special_characters_checked))
button.grid(row=5,column=0, columnspan=4, pady=(20, 0))

# Show password with icon to copy the text to clipboard.
generated_password_label = customtkinter.CTkLabel(master=frame, textvariable=generated_password)
generated_password_label.grid(row=6,column=0, sticky="ew", columnspan=4, pady=(30,0))

root.mainloop()