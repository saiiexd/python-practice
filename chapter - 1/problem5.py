#5. Label the program written in problem 4 with comments. 

#importing os
import os

#defining 
def list_directory_contents(path):
    try:
        # Get the list of all files and directories
        dir_contents = os.listdir(path)
        print(f"Contents of the directory '{path}':")
        for item in dir_contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except NotADirectoryError:
        print(f"The path '{path}' is not a directory.")
    except PermissionError:
        print(f"Permission denied for accessing the directory '{path}'.")

# Replace 'your_directory_path' with the path to the directory you want to list
your_directory_path = 'C:/Users/saive/OneDrive/Desktop/python practice'
list_directory_contents(your_directory_path)

#check
