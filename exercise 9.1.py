class Restaurant:
    """Information about restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        """Return attributes"""
        print(f'Name of Restaurant: {self.name.title()}\n'
              f'Type of cuisine: {self.cuisine.title()}')

    def open_restaurant(self):
        print(f'Restaurant "{self.name.title()}" is open!')


restaurant = Restaurant('astoria', 'ukrainian')
print(f'{restaurant.name}, {restaurant.cuisine}')
restaurant.describe_restaurant()
print()
restaurant.open_restaurant()
