class Restaurant:
    def __init__(self, name, work_time, menu):
        self.name = name
        self.work_time = work_time
        self.menu = menu

    def restaurant_name(self):
        """Write a name of restaurant"""
        message = f'Name of restaurant: {self.name.title()}'
        print(message)

    def cuisine_type(self, cuisine='international'):
        """Write type of cuisine in restaurant"""
        message = f'Type of cuisine: {cuisine}.'
        print(message)

    def menu_message(self):
        """Write dishes in restaurant"""
        menu_list = ''
        for dish in self.menu:
            if dish == self.menu[-1]:
                menu_list += f' {dish}.'
            else:
                menu_list += f' {dish},'
        message = f'Menu:{menu_list}'
        print(message)

    def visit_time(self):
        """Write when restaurant is open"""
        if self.work_time == 'day':
            print(f'{self.name.title()} is a {self.work_time} restaurant (08:00 - 22:00).')
        elif self.work_time == 'night':
            print(f'{self.name.title()} is a {self.work_time} restaurant (21:00 - 09:00).')
        elif self.work_time == 'day&night':
            print(f'{self.name.title()} is a {self.work_time} restaurant (24/7).')
        else:
            print('ERROR! Work time isn\'t founded.')


class IceCreamStand(Restaurant):

    def __init__(self, name, work_time, menu, flavors):
        super().__init__(name, work_time, menu)
        self.flavors = flavors

    def cuisine_type(self, cuisine='international'):
        print('We make ice cream.')

    def menu_message(self):
        print('We make ice cream.')

    def flavors_list(self):
        """Write list of types of ice cream"""
        list_msg = ''
        for ice_cream in self.flavors:
            if ice_cream == self.flavors[-1]:
                list_msg += f' {ice_cream}.'
            else:
                list_msg += f' {ice_cream},'
        message = f'List of ice cream:{list_msg}'
        print(message)


ice_list = ['chocolate', 'banana', 'mix']
ashot = IceCreamStand('ashot', 'day', '', ice_list)
ashot.flavors_list()
