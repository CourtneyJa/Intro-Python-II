class Item:
    def __init__(self, item, description):
        self.item = item
        self.description = description

    def __str__(self):
        return f'Item: {self.item} - \nDescription: {self.description}\n'
    
    def __repr__(self):
        return f'Item: {self.item} - Description: {self.description}'
    
        