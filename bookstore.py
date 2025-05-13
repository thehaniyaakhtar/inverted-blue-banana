#function to validate and track books
#title and author: non empty
#price: +ve no
#stock non neg int
#book titles unique 
#for each book, multuply price by the stock to get books total value
#add up all book values to get total value of all stock 

#helper functions
def valid_title(title):
    return len(title) != 0

def valid_author(author):
    return len(author) != 0

def valid_price(price):
    return price > 0

def valid_stock(stock):
    return stock >= 0

#when to use a helper function and why is it better than a normal one

#main function
def inventory(details):
    titles = set()
    total_value = 0

    for title, author, price, stock in details:
        
        if title in titles:
            print(f"Book already available: {title}")
            return False
        
        
        if not (
            valid_title(title)
            and valid_author(author)
            and valid_price(price)
            and valid_stock(stock)
        ):
            print("Invalid details, try again")
            return False

        titles.add(title)
        
        total_value += price * stock
    
    return total_value

books = [
    ("Atomic Habits", "James Clear", 20.0, 5),
    ("Deep Work", "Cal Newport", 18.5, 4),
    ("Clean Code", "Robert C. Martin", 25.0, 3)
]

print("Inventory content: ", inventory(books))