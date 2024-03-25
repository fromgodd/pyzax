import os
import argparse
from enum import Enum

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

def list_files_and_folders(directory=".", show_hidden=False):
    contents = os.listdir(directory)
    total_items = 0
    total_hidden_items = 0
    print(color_text(f'Contents of {directory}:', TerminalColor.BOLD))
    print(color_text('-------------', TerminalColor.GREEN))
    for item in contents:
        if not show_hidden and item.startswith('.'):
            total_hidden_items += 1
            continue
        if os.path.isdir(os.path.join(directory, item)):
            print(color_text(item, TerminalColor.YELLOW))  # Folders are printed in yellow
        else:
            print(color_text(item, TerminalColor.WHITE))  # Files are printed in white
        total_items += 1
    if not show_hidden:
        print(color_text(f'Total {total_items} items', TerminalColor.BOLD))
    else:
        print(color_text(f'Total {total_items} items. Hidden files - {total_hidden_items}.', TerminalColor.BOLD))

def check_rights(directory=".", show_hidden=False):
    contents = os.listdir(directory)
    total_items = 0
    total_hidden_items = 0
    max_name_length = max(len(item) for item in contents)  # Max length for proper alignment
    print(color_text(f'Contents of {directory}:', TerminalColor.BOLD))
    print(color_text('-------------', TerminalColor.GREEN))
    for item in contents:
        if not show_hidden and item.startswith('.'):
            total_hidden_items += 1
            continue
        
        if os.path.isdir(os.path.join(directory, item)):
            item_color = TerminalColor.YELLOW  # Folders are displayed in yellow
        else:
            item_color = TerminalColor.WHITE  # Files are displayed in white
        
        # Constructing the file access rights string
        rights_string = ""
        if os.access(os.path.join(directory, item), os.R_OK):
            rights_string += 'r'
        else:
            rights_string += '-'
        if os.access(os.path.join(directory, item), os.W_OK):
            rights_string += 'w'
        else:
            rights_string += '-'
        if os.access(os.path.join(directory, item), os.X_OK):
            rights_string += 'x'
        else:
            rights_string += '-'

        # Printing the item with its rights
        print(color_text(f'{rights_string.ljust(10)} {item.rjust(max_name_length)}', item_color))
        total_items += 1
    if not show_hidden:
        print(color_text(f'Total {total_items} items', TerminalColor.BOLD))
    else:
        print(color_text(f'Total {total_items} items.', TerminalColor.BOLD))

def list_folders(directory=".", show_hidden=False):
    contents = os.listdir(directory)
    total_folders = 0
    total_hidden_folders = 0
    print(color_text(f'Folders in {directory}:', TerminalColor.BOLD))
    print(color_text('-------------', TerminalColor.GREEN))
    for item in contents:
        if not show_hidden and item.startswith('.'):
            total_hidden_folders += 1
            continue
        
        if os.path.isdir(os.path.join(directory, item)):
            print(color_text(item, TerminalColor.YELLOW))  # Folders are printed in yellow
            total_folders += 1
    if not show_hidden:
        print(color_text(f'Total {total_folders} folders', TerminalColor.BOLD))
    else:
        print(color_text(f'Total {total_folders} folders. Hidden folders - {total_hidden_folders}.', TerminalColor.BOLD))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List files in a directory")
    parser.add_argument("directory", nargs="?", default=".", help="Directory to list files from (default: current directory)")
    parser.add_argument("-v", "--version", action="version", version=f"pyzax {VERSION}", help="Show program version")
    parser.add_argument("-d", "--description", action="store_true", help="Print program description")
    parser.add_argument("-f", "--folders", action="store_true", help="Print folders only")
    parser.add_argument("-r", "--rights", action="store_true", help="Print file access rights")
    parser.add_argument("-a", "--all", action="store_true", help="Show hidden elements")
    args = parser.parse_args()

    if args.description:
        print(DESCRIPTION_PROMPT)
    elif args.folders:
        list_folders(directory=args.directory, show_hidden=args.all)
    elif args.rights:
        check_rights(directory=args.directory, show_hidden=args.all)
    else:
        list_files_and_folders(directory=args.directory, show_hidden=args.all)
