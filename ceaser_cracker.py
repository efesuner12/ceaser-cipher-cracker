from datetime import datetime
import string
import os
import re

def valid_op_input(choice):
    try:
        choice = int(choice)
    except:
        print("Please enter an integer value!\n")
        return False
    
    return True

def valid_path(path):
    splitted = path.split("/")
    length = len(splitted)

    if not os.path.isdir(path) or "." in splitted[length-1]:
        print("Invalid path!\nPath is not a directory!\n")
        return False

    return True

def create_shift_substitution(n):
    decoding = {}

    alphabet_size = len(string.ascii_uppercase)

    for i in range(alphabet_size):
        letter = string.ascii_uppercase[i]
        subst_letter = string.ascii_uppercase[(i+n)%alphabet_size]

        decoding[subst_letter] = letter

    return decoding

def decode(message, subst):
    result = ""

    for letter in message.upper():
        if letter in subst:
            result += subst[letter]
        else:
            result += letter

    return result

def crack(ciphertext):
    cracked_messages = []

    alphabet_size = len(string.ascii_uppercase)

    for i in range(alphabet_size):
        decode_list = create_shift_substitution(i)
        plain = decode(ciphertext, decode_list)
        cracked_messages.append(plain)

    return cracked_messages

def print_results(results):
    print("\n## POSSBILE PLAIN MESSAGES ##")
    for i in range(1, len(results)):
        print(f"{i} - {results[i]}")
    print("## END ##\n")

def write_into_file(ciphertext, results, path):
    path = f"{path}/cracked.txt"

    print(f"\n[+] Writing results into {path}...")
    
    with open(path, "w") as f:
        data = f"CRACKED CIPHERTEXT: {ciphertext}\n"
        data += f"OPERATION CARRIED OUT ON {datetime.now()}\n\n"

        data += "## POSSBILE PLAIN MESSAGES ##\n"
        for i in range(1, len(results)):
            data += f"{i} - {results[i]}\n"
        data += "## END ##"

        f.write(data)
    
    f.close()
    print("[+] Done.\n")


if __name__ == "__main__":
    os.system("cls||clear")

    ciphertext = input("Please enter the cipher text you want to crack:\n--> ")

    print("\n[+] Cracking the ciphertext...")
    cracked_messages = crack(ciphertext)
    print("[+] Done.\n")

    can_stop = False

    while not can_stop:
        op_choice = input("Would you like to\n 1- Print possible messages\n 2- Write them into a file\n--> ")

        while not valid_op_input(op_choice):
            op_choice = input("Would you like to\n 1- Print possible messages\n 2- Write them into a file\n--> ")
        
        if op_choice == "1":
            can_stop = True
            print_results(cracked_messages)

        elif op_choice == "2":
            can_stop = True
            path = input("\nDestination path (without filename and extension): ")

            while not valid_path(path):
                path = input("Destination path (without filename and extension): ")
            
            write_into_file(ciphertext, cracked_messages, path)

        else:
            print("Not a valid choice!\n")
