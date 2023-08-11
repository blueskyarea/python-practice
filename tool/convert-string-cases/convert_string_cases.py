import sys

def convert_to_uppercase(text):
    return text.upper()

def convert_to_lowercase(text):
    return text.lower()

def convert_to_titlecase(text):
    return text.title()

if __name__ == '__main__':
    print("Text Conversion Tool")
    print("1. Convert to Uppercase")
    print("2. Convert to Lowercase")
    print("3. Convert to Title Case")

    choice = int(input("Enter your choice (1/2/3): "))
    input_text = input("Enter the text: ")
    if choice == 1:
        converted_text = convert_to_uppercase(input_text)
    elif choice == 2:
        converted_text = convert_to_lowercase(input_text)
    elif choice == 3:
        converted_text = convert_to_titlecase(input_text)
    else:
        print("Invalid choice. Please select a valid option (1/2/3).")
        sys.exit(0)

    print("Converted text:", converted_text)
