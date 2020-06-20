class Batch():
    def __init__(self,quantiity,sku: Sku):
        self.quantiity = quantiity 
        self.sku = sku
        self.reference_id = 1
        self.order_lines: List[OrderLine]= []
    def allocate(self, order_line: OrderLine):
        if self.quantiity >= order_line.quantiity:
           self.quantiity -= order_line.quantiity
           self.order_lines.append(order_line)
           return True
        return False

class Order():
    def __init__(self,order_lines: list=[OrderLine]):
        self.reference_id = None

class OrderLine():
    def __init__(self,sku:Sku,quantity:int):
        self.sku = sku

        pass
class Sku():
    def __init__():
        self.reference_id=None
        
        pass

class Warehouse():
    pass