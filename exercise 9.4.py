class Restaurant:
    """Information about restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Return attributes"""
        print(f'Name of Restaurant: {self.name.title()}\n'
              f'Type of cuisine: {self.cuisine.title()}')

    def open_restaurant(self):
        print(f'Restaurant is open!')

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_reserved(self, increment):
        """Add number to number of reserved"""
        self.number_served += increment


restaurant = Restaurant('astoria', 'ukrainian')
print('number of served clients: ' + str(restaurant.number_served))
restaurant.number_served = 15
print('NEW number of served clients: ' + str(restaurant.number_served))
restaurant.set_number_served(9)
print('by Method number of served clients: ' + str(restaurant.number_served))
restaurant.increment_number_reserved(2)
print('Was reserved new 2 clients.\nNEW number of served clients: ' + str(restaurant.number_served))
