import shutil
import os

def copy_file(source, destination):
    try:
        shutil.copy(source, destination)
        print("File copied successfully.")
    except FileNotFoundError:
        print("Source file not found.")
    except Exception as e:
        print("An error occurred:", e)

def move_file(source, destination):
    try:
        shutil.move(source, destination)
        print("File moved successfully.")
    except FileNotFoundError:
        print("Source file not found.")
    except Exception as e:
        print("An error occurred:", e)

def delete_file(file_path):
    try:
        os.remove(file_path)
        print("File deleted successfully.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == '__main__':
    print("File Operations Tool")
    print("1. Copy file")
    print("2. Move file")
    print("3. Delete file")

    choice = int(input("Enter your choice(1/2/3): "))

    if choice == 1:
        source = input("Enter source file path: ")
        destination = input("Enter destination file path: ")
        copy_file(source, destination)
    elif choice == 2:
        source = input("Enter source file path: ")
        destination = input("Enter destination file path: ")
        move_file(source, destination)
    elif choice == 3:
        file_path = input("Enter file path to delete: ")
        delete_file(file_path)
    else:
        print("Invalid choice. Please select a valid option (1/2/3).")

