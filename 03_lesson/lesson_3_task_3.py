from address import Address
from mailing import Mailing 


to_address = Address('160001', 'Вологда', 'Мира', '24', '2' )
from_address = Address('162200', 'Харовск', 'Ленградская', '39', '12')
cost = 100
track = 'ABC123'

my_mailing = Mailing(from_address, to_address, cost, track)
print(my_mailing)