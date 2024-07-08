'''Write a python program to print the contents of a directory using the os module.
Search online for the function which does that.'''
import os

def list_directory_contents(directory):
    try:
        # Get the list of all files and directories
        with os.scandir(directory) as entries:
            for entry in entries:
                print(entry.name)
    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory '{directory}'.")

# Example usage
directory = "."  # You can change this to any directory you want to list
list_directory_contents(directory)
