from src.table import Table 

def test_valid_position():
    table = Table()
    assert table.is_valid_position(0,4)
    assert table.is_valid_position(1,4)
    assert table.is_valid_position(2,4)
    assert table.is_valid_position(4,4)
    assert table.is_valid_position(4,4)
    
def test_invalid_position():
    table = Table()
    assert not table.is_valid_position(0,5)
    assert not table.is_valid_position(1,-4)
    assert not table.is_valid_position(-2,8)
    assert not table.is_valid_position(40,4)
    assert not table.is_valid_position(6,1)