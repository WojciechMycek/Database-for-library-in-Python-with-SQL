from tkinter import *
from PIL import ImageTk, Image
import sqlite3

class lists_books():
    def __init__(self, tittle, author, published_house, is_it_borrow, who_get_it):
        return 0

class users_library(lists_books):
    def __init__(self,name, vorname, address, borrowed_books, user_id):
        return 0

class borrow_and_give_back(users_library,lists_books):
    def __init__(self):
        return 0