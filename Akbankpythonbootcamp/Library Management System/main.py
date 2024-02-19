class Library:
    def __int__(self):
        self.file_path = "book.txt"
        self.file = open(self.file_path, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        book_lines = self.file.read().splitlines()
        for line in book_lines:
            book_info = line.split(',')
            print(f"Title: {book_info[0]}, Author: {book_info[1]}")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_year = input("Enter book release year: ")
        number_of_pages = input("Enter book number of pages: ")

        book_line = f"{title},{author},{release_year},{number_of_pages}\n"
        self.file.write(book_line)
        print(f"Book '{title}' added succesfully!")

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")

        self.file.seek(0)
        book_lines = self.file.read().splitlines()
        updated_book_lines = [line for line in book_lines if title_to_remove not in line]

        self.file.seek(0)
        self.file.truncate()
        self.file.writelines("\n".join(updated_book_lines))

        print(f"Book '{title_to_remove}' revomed succesfully!")


lib = Library()


while True:
    print("\n*** Menu ***")
    print("1) List Book")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Quit")

    user_input = input("Enter your choice (1-4): ")


    if user_input == "1" :
        lib.list_books()
    elif user_input == "2" :
        lib.add_book()
    elif user_input == "3" :
        lib.remove_book()
    elif user_input == "4" :
        print("Exiting the program. Goodbye")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4")


