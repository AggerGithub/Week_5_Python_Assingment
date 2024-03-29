import os

def create_file():
    try:
        with open('my_file.txt', 'w') as file:
            file.write("Hello, Python!\n")
            file.write("Python version: 3.12.1\n")
            file.write("The speed of light is approximately 3.00 x 10^8 meters per second.\n")
            print("File created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Operation completed.")

def read_file():
    try:
        with open('my_file.txt', 'r') as file:
            lines = file.readlines()
            print("File contents:")
            for line in lines:
                print(line.strip())
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Operation completed.")

def append_file():
    try:
        with open('my_file.txt', 'a') as file:
            file.write('The quick brown fox jumps over the lazy dog.\n')
            file.write('12345 is a numeric sequence.\n')
            file.write(' Pi (π) is approximately 3.14159.\n')
            print("File appended successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Operation completed.")

def main():
    create_file()
    read_file()
    append_file()
    read_file()

if __name__ == "__main__":
    main()