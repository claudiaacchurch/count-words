# Intended output:
#
# > say_hello("kay")
# => "hello kay"
from lib.hello import *
import pytest
def test_hello_returns_hello_empty_input():
    result = say_hello('')
    assert result == 'hello '

def test_hello_returns_hello_name():
    result = say_hello('Claudia')
    assert result == 'hello Claudia'

def test_hello_raises_error_nonstr():
    with pytest.raises(Exception) as err:
        say_hello(1)
    error_message = str(err.value)
    assert error_message == 'you are not a number'

