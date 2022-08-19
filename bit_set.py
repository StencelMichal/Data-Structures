class BitSet:
    def __init__(self):
        self.bits = 0

    def add(self, bit: int) -> None:
        self.bits = self.bits | (1 << bit)

    def remove(self, bit: int) -> None:
        self.bits = self.bits & ~(1 << bit)

    def contains(self, bit: int) -> bool:
        return (self.bits & 1 << bit) > 0

    def clear(self) -> None:
        self.bits = 0
