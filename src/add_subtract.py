def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a,b):
    return a * b

def divide(a,b):
    return a / b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0

def test_sub():
    assert sub(5,2) == 3
    assert sub(1,-1) == 2

def test_mul(a,b):
    assert mul(5,4) == 20
    assert mul(5,2) == 10

def test_divide(a,b):
    assert divide(10,2) == 5
    assert divide(100,10)== 10
