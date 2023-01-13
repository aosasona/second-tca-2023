from datetime import datetime

# ENUM to define shipping types cost
NORMAL_COST = 3.95
URGENT_COST = 5.45

"""
Every property has been set to private by default unless explicitly needed as this is good security practice (eg. in firewalls)
"""

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
    def __init__(self, order: Order, ship_date: datetime) -> None:
        self.__order: Order = order
        self.__ship_date: datetime = ship_date
        self.__ship_cost: float = 0.0
        self.count_urgent: int = 0

    @property
    def order(self):
        return self.__order

    @property
    def ship_date(self):
        return self.__ship_date
    
    @property
    def ship_cost(self):
        return self.__ship_cost

    def set_ship_cost(self, val: float):
        self.__ship_cost = val

    def calc_ship_cost(self, is_urgent: bool) -> float:
        cost = NORMAL_COST
        if is_urgent:
            cost = URGENT_COST
            self.count_urgent += 1
        self.set_ship_cost(cost)
        return cost



class Invoice:
    def __init__(self, invoice_nbr: str, stock: Stock, ship_order: Shipping) -> None:
        self.__invoice_nbr: str = invoice_nbr
        self.__stock: Stock = stock
        self.__ship_order: Shipping = ship_order
        self.__total_cost: float = 0.0
        
    @property
    def invoice_nbr(self):
        return self.__invoice_nbr

    def invoice(self):
        shipping_cost = self.__ship_order.ship_cost
        book_cost =  self.__stock.price
        total_cost = shipping_cost + book_cost
        self.__total_cost = total_cost
        return self.__total_cost

    def __str__(self) -> str:
        order = self.__ship_order.order
        customer = order.customer
        stock = order.stock
        return f"""
    Customer name: -> {customer.name}
    Phone number: -> {customer.phone}
    E-mail address -> {customer.email}
    --- Book details ---
        - title -> {stock.book_name}
        - price -> {stock.price}
        - author -> {stock.author}
    Date -> {self.__ship_order.ship_date}
    Shipping fee -> {self.__ship_order.ship_cost}
    Total cost -> {self.__total_cost:.2f}"""




class BookStore:
    def __init__(self):
        self.invoices: list[Invoice] = []

    def get_invoices(self):
        return self.invoices

    def search_invoice(self, nbr: str):
        for invoice in self.invoices:
            if invoice.invoice_nbr == nbr:
                print(f"---------------------------\nFound invoice no. {nbr}\n---------------------------")
                print(invoice)
                return

        print("Invoice not found!")


"""
Test function to simulate various operations
"""

class Test:
    def main(self):
        customer1 = Customer("Jack Richer", "07823456747", "j.richer@gmail.com")
        customer2 = Customer("Jack Ryan", "07126556919", "jackryan@protonmail.com")
        customer3 = Customer("James Bond", "07123123784", "double007@outlook.com") 
 
 
        stock1 = Stock("Spy 101", "Tom Cruise", 24.99)
        stock2 = Stock("Spy 102", "John Wick", 14.99)
        stock3 = Stock("Spy 103", "Mary Jane", 34.99)
 
 
        order1 = Order(customer1, stock1)
        order2 = Order(customer2, stock2)
        order3 = Order(customer3, stock3)
 
 
        shipping1 = Shipping(order1, datetime.today())
        shipping2 = Shipping(order2, datetime.today())
        shipping3 = Shipping(order3, datetime.today())
 
 
        shipping1.set_ship_cost(shipping1.calc_ship_cost(True))
        shipping2.set_ship_cost(shipping2.calc_ship_cost(False))
        shipping3.set_ship_cost(shipping3.calc_ship_cost(True))
 
 
        invoice1 = Invoice("INV0001", stock1, shipping1)
        invoice2 = Invoice("INV0002", stock2, shipping2)
        invoice3 = Invoice("INV0003", stock3, shipping3)
 
 
        bookstore = BookStore()
 
        bookstore.invoices.append(invoice1)
        bookstore.invoices.append(invoice2)
        bookstore.invoices.append(invoice3)
 
        print(f"Number of urgent shipments: {shipping1.count_urgent}")
        print(f"Invoice 1 total cost: {invoice1.invoice():.2f}")
        print(f"Invoice 2 total cost: {invoice2.invoice():.2f}")
        print(f"Invoice 3 total cost: {invoice3.invoice():.2f}")
 
        bookstore.search_invoice("INV0004")
 
 
if __name__ == "__main__":
    Test().main()
