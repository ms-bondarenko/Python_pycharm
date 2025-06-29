from address import Address

class Mailing:

    def __init__(self, to_address: Address, from_address: Address, cost: float, track: str):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def __str__(self):
        return f"Mailing from {self.from_address} to {self.to_address}, cost: {self.cost: .2f}, tracking number: {self.track}"