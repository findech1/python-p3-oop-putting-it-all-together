#!/usr/bin/env python3


# In book.py

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
        self.current_page = 1  # Default current page to 1

    def flip_page(self):
        if self.current_page < self.page_count:
            self.current_page += 1
            print(f"Flipped to page {self.current_page}")
        else:
            print("You've reached the end of the book.")

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Total Pages: {self.page_count}")
        print(f"Current Page: {self.current_page}")
