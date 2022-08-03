class Library():
    def __init__(self):
        self.book_store = {}
        
    def add_book(self, book_name, author):
        self.book_store.update({book_name : author})
        return self
        
    def search_book(self, book_name):
        print(self.book_store[book_name])
        return self
        
    def delete_book(self, book_name):
        self.book_store.pop(book_name)
        return self
        
        
if __name__ == '__main__':
    l1 = Library()
    print(l1.add_book("Machine Learning", "sebastian").search_book("Machine Learning").delete_book("Machine Learning"))
    

    