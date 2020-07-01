class Estate():

    def __init__(self, title, type_, address, rooms, price, area):
        self.title = title
        self.type = type_
        self.address = address
        self.rooms = rooms
        self.price = price
        self.area = area

    def get_title(self):
        return self.title

    def get_type(self):
        return self.type

    def get_address(self):
        return self.address

    def get_rooms(self):
        return self.rooms

    def get_price(self):
        return self.price

    def get_area(self):
        return self.area

    def set_title(self, title):
        self.title = title

    def set_type(self, type_):
        self.type = type_

    def set_address(self, address):
        self.address = address

    def set_rooms(self, rooms):
        self.rooms = rooms

    def set_price(self, price):
        self.price = price

    def set_area(self, area):
        self.area = area
