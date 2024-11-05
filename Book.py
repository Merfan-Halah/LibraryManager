class Book:

    def __init__(self, title, author, year,status):
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __str__(self):
        return f"{self.title} by {self.author} {self.year} - {self.status}"



