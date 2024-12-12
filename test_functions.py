from functions import salary,hello_who

def test_hello_who_max():
    assert hello_who('Max') =='Hello,Max'
    assert hello_who('Ben') =='Hello,Ben'
    assert hello_who('Sawe') == 'Hello,Sawe'

def test_salary():
    assert salary(2,4) == 16
    assert salary(5,4) == 40

def test_beta():
    assert beta(4) == "четное"
    assert beta(3) == "не четное"