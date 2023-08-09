def count_characters(input_string):
    return len(input_string)

def reverse_string(input_string):
    return input_string[::-1]

if __name__ == '__main__':
    print("String Manipulation Tool")
    print("1. Count characters")
    print("2. Reverse string")

    choice = int(input("Enter your choice (1/2) "))

    if choice == 1:
        input_str = input("Enter a string: ")
        char_count = count_characters(input_str)
        print("Number of characters:", char_count)
    elif choice == 2:
        input_str = input("Enter a string: ")
        reversed_str = reverse_string(input_str)
        print("Reversed string:", reversed_str)
    else:
        print("Invalid choice. Please select a valid option (1/2).")

