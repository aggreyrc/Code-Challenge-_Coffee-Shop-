class Customer:
    def __init__(self,name):
        if not isinstance(name,str):
            raise ValueError("Name must be a string")
        if not 1 <= len(name) <= 15:
            raise ValueError("Name must be between 1 and 15 characters long")
        self.name = name