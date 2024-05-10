import sys
import time
import shutil


### eksperimen
### bisa dicoba2 juga buat yang lain

def login_interface():
    logo = '''
 ██████╗ ██╗    ██╗ ██████╗ █████╗ 
██╔═══██╗██║    ██║██╔════╝██╔══██╗
██║   ██║██║ █╗ ██║██║     ███████║
██║   ██║██║███╗██║██║     ██╔══██║
╚██████╔╝╚███╔███╔╝╚██████╗██║  ██║
 ╚═════╝  ╚══╝╚══╝  ╚═════╝╚═╝  ╚═╝ 
 
[ Login ]   [ Help ]   [ Register ]   [ Menu ]   [ Logout ]

                              [Exit]                                
'''
    return logo

def print_centered(text):
    """Prints text centered in the terminal."""
    cols = shutil.get_terminal_size().columns
    lines = text.split('\n')
    for line in lines:
        padding = " " * ((cols - len(line)) // 2)
        print(padding + line)


if __name__ =='__main__':
    print_centered(login_interface())