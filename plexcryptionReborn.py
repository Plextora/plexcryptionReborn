import time
import os
import datetime

def encryptText():
    print("Please enter the text you want to encrypt:")

    text = input(">> ")

    timestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H-%M-%S")

    original = text

    text = text.upper()

    encryption = {
        "A": "¯\_(ツ)_/¯",
        "B": "( ͡° ͜ʖ ͡°)",
        "C": "ʕ•ᴥ•ʔ",
        "D": "▄︻̷̿┻̿═━一",
        "E": "༼ つ ◕_◕ ༽つ",
        "F": "ಠ_ಠ",
        "G": "(◕‿◕✿)",
        "H": "(¬‿¬)",
        "I": "◉_◉",
        "J": "~(˘▾˘~)",
        "K": "ヾ(⌐■_■)ノ♪",
        "L": "ಥ_ಥ",
        "M": "(｡◕‿◕｡)",
        "N": "°Д°",
        "O": "(；一_一)",
        "P": "( ⚆ _ ⚆ )",
        "Q": "(ᵔᴥᵔ)",
        "R": "｡◕‿◕｡",
        "S": "ಠ~ಠ",
        "T": "^̮^",
        "U": "Ƹ̵̡Ӝ̵̨̄Ʒ",
        "V": "(▰˘◡˘▰)",
        "W": "◔̯◔",
        "X": "¬_¬",
        "Y": "._.",
        "Z": ":D"
    }

    for key, value in encryption.items():
        text = text.replace(key, value)
    
    print("Here is your encrypted text:")    
        
    print(text)

    print("In case of the decryption function not working, plexcryption has saved your original text into original" + timestamp + ".txt")

    with open("original" + timestamp + ".txt", "w") as f:
        f.write(original)


    menu()

def decryptText():
    print("Please enter the text you want to decrypt:")

    text = input(">> ")
    text = text.upper()

    decryption = {
        "¯\_(ツ)_/¯": "A",
        "( ͡° ͜ʖ ͡°)": "B",
        "ʕ•ᴥ•ʔ": "C",
        "▄︻̷̿┻̿═━一": "D",
        "༼ つ ◕_◕ ༽つ": "E",
        "ಠ_ಠ": "F",
        "(◕‿◕✿)": "G",
        "(¬‿¬)": "H",
        "◉_◉": "I",
        "~(˘▾˘~)": "J",
        "ヾ(⌐■_■)ノ♪": "K",
        "ಥ_ಥ": "L",
        "(｡◕‿◕｡)": "M",
        "°Д°": "N",
        "(；一_一)": "O",
        "( ⚆ _ ⚆ )": "P",
        "(ᵔᴥᵔ)": "Q",
        "｡◕‿◕｡": "R",
        "ಠ~ಠ": "S",
        "^̮^": "T",
        "Ƹ̵̡Ӝ̵̨̄Ʒ": "U",
        "(▰˘◡˘▰)": "V",
        "◔̯◔": "W",
        "¬_¬": "X",
        "._.": "Y",
        ":D": "Z"
    }

    for key, value in decryption.items():
        text = text.replace(key, value)
    
    print("Here is your decrypted text:")

    print(text) 

    menu()


def startup():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("""
██████╗░██╗░░░░░███████╗██╗░░██╗░█████╗░██████╗░██╗░░░██╗██████╗░████████╗██╗░█████╗░███╗░░██╗
██╔══██╗██║░░░░░██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
██████╔╝██║░░░░░█████╗░░░╚███╔╝░██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░██║██║░░██║██╔██╗██║
██╔═══╝░██║░░░░░██╔══╝░░░██╔██╗░██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░██║██║░░██║██║╚████║
██║░░░░░███████╗███████╗██╔╝╚██╗╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░██║╚█████╔╝██║░╚███║
╚═╝░░░░░╚══════╝╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝

██████╗░███████╗██████╗░░█████╗░██████╗░███╗░░██╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗████╗░██║
██████╔╝█████╗░░██████╦╝██║░░██║██████╔╝██╔██╗██║
██╔══██╗██╔══╝░░██╔══██╗██║░░██║██╔══██╗██║╚████║
██║░░██║███████╗██████╦╝╚█████╔╝██║░░██║██║░╚███║
╚═╝░░╚═╝╚══════╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝

Made by Plextora""")
    
    time.sleep(3)

    os.system('cls' if os.name == 'nt' else 'clear')

startup()

def menu():
    print("What would you like to do?")

    print("[1] Encrypt text")
    print("[2] Decrypt text")
    print("[3] Exit")

    option = input(">> ")

    if option == "1":
        encryptText()
    if option == "2":
        decryptText()
    if option == "3":
        os._exit(os.EX_OK)
    else:
        print("Invalid option.")
        menu()

menu()
