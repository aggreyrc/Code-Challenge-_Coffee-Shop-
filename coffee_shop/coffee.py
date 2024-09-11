class Coffee:
    def __init__(self, name):
        if not isinstance(name,str):
            raise ValueError("Name must be a string")
        if not len(name) > 3:
            raise ValueError("Name must be at least 3 characters long")
        self.name = name