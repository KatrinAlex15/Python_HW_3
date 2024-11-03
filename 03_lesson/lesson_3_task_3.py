from address import Address
from mailing import Mailing

to_address = Address(index="12345", city="Новосибирск", street="Толстого", house="10", apartment="20")
from_address = Address(index="65412", city="Тольятти", street="Лермонтова", house="5", apartment="30")
mailing = Mailing(to_address, from_address, cost=1500, track="123456")

print(mailing)