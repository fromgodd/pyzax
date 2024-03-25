import os
import argparse
from enum import Enum

'''
    TODO:
    -- ADD BUFFER MODE SUPPORT (-b) argument where contents will be recorded to pre-allocated buf and print
    -- IMPLEMENT CONFIG FILE SUPPORT where we can specify static arguments, color scheme support and etc
    -- Read Write check
    -- Date Time check
    -- Detailed atributes and separate modular structure for project
'''

VERSION = "v0.1"
DESCRIPTION_PROMPT = '''
pyzax - minimalistic replacement for ls written in Python
'''

class TerminalColor(Enum):
    RESET = "\033[0m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    REVERSED = "\033[7m"

def color_text(text, color):
    return f"{color.value}{text}{TerminalColor.RESET.value}"

def list_files_and_folders(directory="."):
    contents = os.listdir(directory)
    total_items = 0
    print(color_text(f'Contents of {directory}:', TerminalColor.BOLD))
    print(color_text('-------------', TerminalColor.GREEN))
    for item in contents:
        print(color_text(item, TerminalColor.YELLOW))
        total_items += 1
    print(color_text(f'Total {total_items} items', TerminalColor.BOLD))

def list_folders(directory="."):
    contents = os.listdir(directory)
    total_folders = 0
    print(color_text(f'Folders in {directory}:', TerminalColor.BOLD))
    print(color_text('-------------', TerminalColor.GREEN))
    for item in contents:
        if os.path.isdir(os.path.join(directory, item)):
            print(color_text(item, TerminalColor.YELLOW))
            total_folders += 1
    print(color_text(f'Total {total_folders} folders', TerminalColor.BOLD))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List files in a directory")
    parser.add_argument("directory", nargs="?", default=".", help="Directory to list files from (default: current directory)")
    parser.add_argument("-v", "--version", action="version", version=f"pyzax {VERSION}", help="Show program version")
    parser.add_argument("-d", "--description", action="store_true", help="Print program description")
    parser.add_argument("-f", "--folders", action="store_true", help="Print folders only")
    args = parser.parse_args()

    if args.description:
        print(DESCRIPTION_PROMPT)
    elif args.folders:
        list_folders(directory=args.directory)
    else:
        list_files_and_folders(directory=args.directory)
