from smartphone import Smartphone

catalog = []
phone1 = Smartphone("Samsung", "A5", "+79211111111")
phone2 = Smartphone("Apple", "Iphone 11", "+79212222222")
phone3 = Smartphone("Apple", "Iphone 12", "+79213333333")
phone4 = Smartphone("Xiaomi", "Redmi Note 10", "+79214444444")
phone5 = Smartphone("Google", "Pixel 5", "+79215555555")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} {phone.model} {phone.phone_number}")