def library_entry(library):

    book= input('What book would you like to add: ')
    author =input('who authored this title: ')
    new_book = ((book.title(), author.title()))
    if new_book not in library:
            library.append(new_book)

            return library
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
library_entry(library)

