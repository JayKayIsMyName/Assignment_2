# Part c

from dataclasses import dataclass

@dataclass
class InventoryItem:
    name: str
    unit_price: float
    quantity_on_hand: int = 0

apple = InventoryItem('apples', 2.00, 75)
banana = InventoryItem('bananas', 0.75, 50)
cucumber = InventoryItem('cucumbers', 1.50, 60)

print(apple, banana, cucumber)