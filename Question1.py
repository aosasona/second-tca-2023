import datetime

class Customer:
    def __init__(self, name: str, phone: str, email: str) -> None:
        self.__name: str = name
        self.__phone: str = phone
        self.__email: str = email

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val: str):
        self.__name = val

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, val: str):
        self.__phone = val


    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, val: str): 
        self.__email = val



class Stock:
    def __init__(self, book_name: str, author: str, price: float) -> None:
        self.__book_name: str = book_name
        self.__author: str = author
        self.__price: float = price

    @property
    def book_name(self):
        return self.__book_name

    @book_name.setter
    def book_name(self, val: str):
        self.__book_name = val

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, val: str):
        self.__author = val

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, val: float):
        self.__price = val



class Order:
    def __init__(self, customer: Customer, stock: Stock):
        self.__customer: Customer = customer
        self.__stock: Stock = stock

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, val: Customer):
        self.__customer = val

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, value):
        self.__stock = value



class Shipping:
    def __init__(self, order: Order, ship_date: datetime.date) -> None:
        self.__order: Order = order
        self.__ship_date: datetime.date = ship_date
        self.__ship_cost: float = 0.0
        self.__count_urgent: int = 0


    @property
    def ship_date(self):
        return self.__ship_date

    @property
    def ship_cost(self):
        return self.__ship_cost
