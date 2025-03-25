class Address:

    def __init__(self, postcode, city, street, house, flat):
        self.postcode = postcode
        self.city = city
        self.street = street
        self.house = house
        self.flat = flat

    def __str__(self):
        return(f"{self.postcode} {self.city}, ул. {self.street} дом {self.house} кв. {self.flat}" )