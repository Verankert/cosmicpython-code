from datetime import date, timedelta
import pytest

from model import Batch,Sku,OrderLine,Order

today = date.today()
tomorrow = today + timedelta(days=1)
later = tomorrow + timedelta(days=10)

@pytest.fixture
def table():
    return Sku()

@pytest.fixture
def order_line_of_2(table):
    return OrderLine(sku=table,quantity=2,order_id="first_order")

@pytest.fixture
def order_line_of_10(table):
    return OrderLine(sku=table,quantity=10,order_id="second_order")

@pytest.fixture
def batch_of_10(table):
    return Batch(quantity=10,sku=table)
@pytest.fixture
def batch_of_5(table):
    return Batch(quantity=5,sku=table)

def test_allocating_to_a_batch_reduces_the_available_quantity(batch_of_10,order_line_of_2):
    batch_quantity=batch_of_10.quantity
    batch_of_10.allocate(order_line_of_2)
    assert batch_of_10.quantity < batch_quantity


def test_can_allocate_if_available_greater_than_required(batch_of_10,order_line_of_2):
    assert batch_of_10.quantity > order_line_of_2.quantity
    assert batch_of_10.can_allocate(order_line_of_2) 

def test_cannot_allocate_if_available_smaller_than_required(batch_of_5,order_line_of_10):
    assert not batch_of_5.allocate(order_line_of_10) 

def test_can_allocate_if_available_equal_to_required(batch_of_10,order_line_of_10):
    assert batch_of_10.quantity == order_line_of_10.quantity
    assert batch_of_10.can_allocate(order_line_of_10) 

def test_can_not_deallocate_unallocated(batch_of_10,order_line_of_2):
    assert not batch_of_10.can_deallocate(order_line_of_2)

def test_can_deallocate_unallocated(batch_of_10,order_line_of_2):
    batch_of_10.allocate(order_line_of_2)
    assert batch_of_10.can_deallocate(order_line_of_2)
def test_prefers_warehouse_batches_to_shipments():
    pytest.fail('todo')

def test_prefers_earlier_batches():
    pytest.fail('todo')

