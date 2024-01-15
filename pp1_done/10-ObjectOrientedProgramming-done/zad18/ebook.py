class Ebook():
    def __init__(self, title, author, page_numbers):
        self.title = title
        self.author = author
        self.page_numbers = page_numbers
        self.current_page_no = 1
        self.open = False
    def open_book(self):
        self.open = True
    def close_book(self):
        self.open = False
    def next(self):
        if self.open and self.current_page_no < self.page_numbers:
            self.current_page_no += 1
        elif not self.open:
            print("The book is closed.")
    def prev(self):
        if self.open and self.current_page_no < self.page_numbers:
            self.current_page_no -= 1
        elif not self.open:
            print("The book is closed.")
    def status(self):
        status = (f"Title:              {self.title}\n"
                  f"Author:             {self.author}\n"
                  f"Number of pages:    {self.page_numbers}\n"
                  f"Current page:       {self.current_page_no}")
        print(status)