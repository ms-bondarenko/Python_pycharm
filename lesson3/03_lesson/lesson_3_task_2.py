from smartphone import SmartPhone

catalog = [
    SmartPhone("Nokia", "3220","+79024445566"),
    SmartPhone("Siemens", "S45","+79289992415"),
    SmartPhone("iPhone","12", "+79883252525"),
    SmartPhone("Samsung","R210","+79892325255"),
    SmartPhone("Alcatel", "OT535", "+79293653635"),
    SmartPhone("Ericsson","T28", "+79031112233")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model} . {smartphone.number}")
