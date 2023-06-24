import random
import string
import streamlit as st

def generate_password(min_length, include_numbers=True, include_special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special_characters = string.punctuation # for psecial_charatcers

    characters = letters
    if include_numbers:
        characters += digits ## adding the digits in cgaracters if we need digits
    if include_special_characters:
        characters += special_characters ## adding the special characters in characters if we need

    password = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(password) < min_length:
        new_char = random.choice(characters)
        password += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special_characters:
            has_special = True

        meets_criteria = True
        if include_numbers:
            meets_criteria = has_number
        if include_special_characters:
            meets_criteria = meets_criteria and has_special

    return password


## Creating Streamlit app  --------->>
def main():
    st.title("Password Generator")

    min_length = st.number_input("Enter the minimum length for the password:", min_value=1, value=10)

    include_numbers = st.checkbox("Include numbers")
    include_special_characters = st.checkbox("Include special characters")

    if st.button("Generate Password"):
        password = generate_password(min_length, include_numbers, include_special_characters)
        st.success("Your generated password is: " + password)

if __name__ == '__main__':
    main()
