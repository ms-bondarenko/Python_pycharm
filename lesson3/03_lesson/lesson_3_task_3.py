from address import  Address
from mailing import Mailing

if __name__ == "__main__":
    to_addr = Address("352900","Armavir", "main street", "25", "35")
    from_addr = Address("350000", "Krasnodar","Severnaya","54","79")
    mailing = Mailing( to_address = to_addr,from_address = from_addr, cost = 250.45, track = "ADB123456")

print(mailing)

