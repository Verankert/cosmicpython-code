from typing import List,Set
from dataclasses import dataclass
class Sku():
    def __init__(self):
        self.reference_id=None
@dataclass(frozen=True)
class OrderLine():
    # def __init__(self,sku:Sku,quantity:int):
        order_id: str
        sku: Sku
        quantity:int
class Order():
    def __init__(self,order_lines: List[OrderLine]):
        self.order_id = None

class Batch():
    def __init__(self,quantity,sku: Sku):
        self.quantity = quantity 
        self.sku = sku
        self.reference_id = 1
        self.order_lines: Set[OrderLine]= set()

    def allocate(self, order_line: OrderLine):
        if self.can_allocate(order_line):
           self.quantity -= order_line.quantity
           self.order_lines.add(order_line)
           return True

    def deallocate(self,order_line):
        if can_deallocate(order_line):
            self.order_lines.remove(order_line)
            self.quantity -= order_line.quantity

    def can_deallocate(self,order_line):
        return order_line in self.order_lines

    def can_allocate(self,order_line):
        return self.quantity >= order_line.quantity and self.sku == order_line.sku
class Warehouse():
    def __init__(self):
        pass
    pass