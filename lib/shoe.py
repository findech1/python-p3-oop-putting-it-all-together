#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size, color, price):
        self.brand = brand
        self.size = size
        self.color = color
        self.price = price

    def change_color(self, new_color):
        self.color = new_color
        print(f"The color of the {self.brand} shoe has been changed to {self.color}.")

    def display_details(self):
        print(f"Brand: {self.brand}")
        print(f"Size: {self.size}")
        print(f"Color: {self.color}")
        print(f"Price: {self.price}")
