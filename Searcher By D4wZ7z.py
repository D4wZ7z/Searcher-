import os
import os
from colorama import init, Fore
from pystyle import Colorate, Colors
import time


def clear_cmd():
    if os.name == 'nt': #windows
        _ = os.system('cls')
    else:
        _ = os.system('clear') #linux ou mac

def print_logo():
     
    print(Colorate.Horizontal(Colors.rainbow," /$$$$$$$  /$$   /$$              /$$$$$$$$     /$$$$$$$$        "))
    print(Colorate.Horizontal(Colors.rainbow,"| $$__  $$| $$  | $$             |_____ $$     |_____ $$/        "))
    print(Colorate.Horizontal(Colors.rainbow,"| $$  \ $$| $$  | $$ /$$  /$$  /$$    /$$/          /$$//$$$$$$$$"))
    print(Colorate.Horizontal(Colors.rainbow,"| $$  | $$| $$$$$$$$| $$ | $$ | $$   /$$/          /$$/|____ /$$/"))
    print(Colorate.Horizontal(Colors.rainbow,"| $$  | $$|_____  $$| $$ | $$ | $$  /$$/          /$$/    /$$$$/ "))
    print(Colorate.Horizontal(Colors.rainbow,"| $$  | $$      | $$| $$ | $$ | $$ /$$/          /$$/    /$$__/  "))
    print(Colorate.Horizontal(Colors.rainbow,"| $$$$$$$/      | $$|  $$$$$/$$$$//$$$$$$$$ /$$ /$$/    /$$$$$$$$"))
    print(Colorate.Horizontal(Colors.rainbow,"|_______/       |__/ \_____/\___/|________/|__/|__/    |________/"))    
    print(Colorate.Horizontal(Colors.rainbow,""))                                                                           
    print(Colorate.Horizontal(Colors.rainbow,"                                                                             "))
    print(Colorate.Horizontal(Colors.rainbow,"+---------------Searcher---------------+"))
    print(Colorate.Horizontal(Colors.rainbow,"|                                      |"))
    print(Colorate.Horizontal(Colors.rainbow,"[+]Server https://discord.gg/ZQKRncDB  [+]"))
    print(Colorate.Horizontal(Colors.rainbow,"[+]Maded by D4wZ7z                     [+]"))  
    print(Colorate.Horizontal(Colors.rainbow,"[+]Support from wh1t3c4tc4d            [+]"))   
    print(Colorate.Horizontal(Colors.rainbow,"[+]TEAM CACA MOU >>>>                  [+]                     "))
    print(Colorate.Horizontal(Colors.rainbow,"|                                      |"))
    print(Colorate.Horizontal(Colors.rainbow,"+---------------Searcher---------------+"))


def search_files(keyword, directory="db"):
    found_entries = []
    start_time = time.time()
    valid_extensions = (".txt", ".sql")  # possible d'ajouter d'autre extension de fichier si vous voulais.
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(valid_extensions):  
                file_path = os.path.join(root, file)
                matching_lines = []  
                try:
                    with open(file_path, 'r', encoding='latin1') as f:
                        for line_number, line in enumerate(f, start=1):
                            if keyword in line:
                                entry = {
                                    "file_path": os.path.relpath(file_path, directory),
                                    "line_number": line_number,
                                    "line_content": line.strip()
                                }
                                found_entries.append(entry)
                                matching_lines.append(line.strip())  
                    if matching_lines:
                        print(Colorate.Horizontal(Colors.green_to_red, (f"Word found in file : {file_path}")))
                        for line in matching_lines:
                            print(Colorate.Horizontal(Colors.green_to_yellow, (f"Ligne {line_number}: {line}")))
                        print()  
                except FileNotFoundError:
                    print(Colorate.Horizontal(Colors.red_to_blue, (f"File not found: {file_path}. Skipping...")))

    end_time = time.time()
    search_duration = end_time - start_time
    return found_entries, search_duration

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    print_logo()
    print()
    print()
    print(Colorate.Horizontal(Colors.rainbow,"Type the word you wish to search for and press Enter ('Q' to exit and 'cls' to clear cmd) : "))
    print()
    while True:
        keyword = input()
        if keyword.lower() == 'q':
            break
        
        root_directory = "db"
        entries, search_duration = search_files(keyword, root_directory)
        if entries:
            print()
            print()
            print("\nResults:")
            print()
            print()
            for entry in entries:
                print()
                print()
                print(f"Word found in file: {entry['file_path']}")
                print()
                print()
                print(f"Line {entry['line_number']}: {entry['line_content']}\n")
                print()
                print()
            print(f"Search time: {search_duration:.2f} seconds")
            print()
            print()
        else:
            print()
            print("\nNo results found.")

if __name__ == "__main__":
    main()
