class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name.title()
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        """Write the name of restaurant and type of cuisine"""
        message = f'Name of restaurant: {self.name}\nType of cuisine: {self.cuisine}'
        return message


astoria = Restaurant('astoria', 'ukrainian')
chin_chan = Restaurant('chin chan chon', 'chines')
vodka = Restaurant('vodka', 'russian')
print(astoria.describe_restaurant() + '\n')
print(chin_chan.describe_restaurant() + '\n')
print(vodka.describe_restaurant())
