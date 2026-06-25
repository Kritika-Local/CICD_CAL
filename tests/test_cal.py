from src.cal_operations import add,sub

def test_add():
    assert add(2,2)==4
    assert add(3,5)==8

def test_sub():
    assert sub(3,3)==0