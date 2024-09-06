from src.math_ops import add , sub

def test_add():
    assert add(2,3)==5
    assert add(3,7)==10
    assert add(-1,1)==0
    assert add(3,5)==8

def test_sub():
    assert sub(3,6)==-3
    assert sub(24,2)==22
    assert sub(5,2)==3
        