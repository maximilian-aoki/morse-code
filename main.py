from morse import MORSE_CODE_DICT, TEXT_CODE_DICT

# INTRO TO DISPLAY
print(r'''
   __  _______  ___  ________  _________  ___  ____  _________  _  ___   _________ _____________ 
  /  |/  / __ \/ _ \/ __/ __/ / ___/ __ \/ _ \/ __/ / ___/ __ \/ |/ | | / / __/ _ /_  __/ __/ _ \
 / /|_/ / /_/ / , __\ \/ _/  / /__/ /_/ / // / _/  / /__/ /_/ /    /| |/ / _// , _// / / _// , _/
/_/  /_/\____/_/|_/___/___/  \___/\____/____/___/  \___/\____/_/|_/ |___/___/_/|_|/_/ /___/_/|_| 
                                                                                                 ''')
print("Welcome to the Morse Code Converter!\n")
print("Note that the converter accepts all letters and numbers, "
      "and accepts the following characters: , . ? - ( )")
print("The converter will ignore any characters that are not included in the above.")


# TEXT TO MORSE FUNCTION
def text_to_morse():
    text = input("Please input the text to be converted:\n").upper().strip()
    morse_code_list = []
    for char in text:
        if char in MORSE_CODE_DICT:
            morse_char = MORSE_CODE_DICT[char] + "/"
            morse_code_list.append(morse_char)

    morse_code_converted = "".join(morse_code_list)
    print(f"Here is your morse code:\n{morse_code_converted}")


# MORSE TO TEXT FUNCTION
def morse_to_text():
    morse = input("Please input the morse code to be converted in dashes and periods ['-', '.'] "
                  "with each full 'character' separated by a '/' :\n").strip()
    morse_list = morse.split("/")
    text_list = []
    for char in morse_list:
        if char in TEXT_CODE_DICT:
            text_char = TEXT_CODE_DICT[char]
            text_list.append(text_char)

    text_converted = "".join(text_list).lower()
    print(f"Here is your text: \n{text_converted}")


# PROGRAM LOGIC
program_on = True
while program_on:
    action = input("\nWhat would you like to do? "
                   "('t' for text-to-morse, 'm' for morse-to-text, 'e' for exit: ").lower().strip()
    if action == "t":
        text_to_morse()
    elif action == "m":
        morse_to_text()
    elif action == "e":
        program_on = False
    else:
        print("Sorry, that was not a recognized command")
