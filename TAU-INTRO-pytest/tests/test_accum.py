import pytest

from stuff.accum import Accumulator



def test_accumlator_init(accum,accum2):
    assert accum.count == 0


def test_accumlator_add_one(accum):
    accum.add()
    assert accum.count == 1

def test_accumlator_add_three(accum):
    accum.add(3)
    assert accum.count == 3

def test_accumlator_add_twice(accum):
    accum.add()
    accum.add()
    assert accum.count == 2

def test_accumulator_cannot_set_count_directly(accum):
  with pytest.raises(AttributeError, match=r"can't set attribute 'count'") as e:
    accum.count = 10