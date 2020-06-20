from datetime import date, timedelta
import pytest

from model import ...

today = date.today()
tomorrow = today + timedelta(days=1)
later = tomorrow + timedelta(days=10)


@pytest.fixture
def batch_of_10():
    return Batch(quantitiy=10)


def test_allocating_to_a_batch_reduces_the_available_quantity(batch_of_10):
    batch_quantitiy=batch_of_10.quantitiy
    ordered_quantitity=5
    batch_of_10.allocate(ordered_quantitity)
    assert batch_of_10.quantity < batch_quantitiy


def test_can_allocate_if_available_greater_than_required():
    batch_quantitiy=batch_of_10.quantitiy
    ordered_quantitity=5
    assert batch_of_10.allocate(ordered_quantitity) 

def test_cannot_allocate_if_available_smaller_than_required():
    batch_quantitiy=batch_of_10.quantitiy
    ordered_quantitity=20
    assert not batch_of_10.allocate(ordered_quantitity) 

def test_can_allocate_if_available_equal_to_required():
    batch_quantitiy=batch_of_10.quantitiy
    ordered_quantitity=batch_quantitiy
    assert batch_of_10.allocate(ordered_quantitity) 

def test_prefers_warehouse_batches_to_shipments():
    pytest.fail('todo')

def test_prefers_earlier_batches():
    pytest.fail('todo')

