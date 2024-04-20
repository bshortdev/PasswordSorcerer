import random
import string

def generate_password(length, has_lowercase_letters, has_uppercase_letters, has_numbers, has_special_characters):
    password_placeholder = []
    character_types_to_include = []
    if(has_lowercase_letters):
        password_placeholder.append(random.choice(string.ascii_lowercase))
        character_types_to_include.append(0)
    if(has_uppercase_letters):
        password_placeholder.append(random.choice(string.ascii_uppercase))
        character_types_to_include.append(1)
    if(has_numbers):
        password_placeholder.append(random.choice(string.digits))
        character_types_to_include.append(2)
    if(has_special_characters):
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

    return "".join(password_placeholder)
