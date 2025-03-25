from smartphone import Smartphone
catalog = []
catalog.append(Smartphone("Samsung", "Galaxy11", "+7-900-123-45-67"))
catalog.append(Smartphone("IPhone", "14 ProMax", "+7-921-123-54-76"))
catalog.append(Smartphone("Samsung", "Galaxy S21", "+7-900-40-45-13"))
catalog.append(Smartphone("Apple", "iPhone 12", "+7-921-123-50-96"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 10", "+7-911-123-90-69"))
for phone in catalog:

    print(f'{phone.phone_brand}, {phone.phone_model}, {phone.number}')