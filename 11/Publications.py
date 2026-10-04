class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Book: {self.name} (Author: {self.author}, {self.page_count} pages)")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Magazine: {self.name} (Chief Editor: {self.chief_editor})")

# Main program
donald_duck = Magazine("Donald Duck", "Aki Hyyppä")
compartment_no_6 = Book("Compartment No. 6", "Rosa Liksom", 192)

donald_duck.print_information()
compartment_no_6.print_information()