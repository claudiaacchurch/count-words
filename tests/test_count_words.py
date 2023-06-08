from lib.count_words import *
import pytest 

'''A function called count_words that takes a 
string as an argument and returns the number of words 
in that string.'''

#takes an argument
#checks number of words
#return number of words

#test returns 0 for empty string
def test_count_words_empty_returns_0():
    result = count_words("")
    assert result == 0

#test returns 1 for single word, no spaces
def test_count_words_one_returns_onw():
    result = count_words("one")
    assert result == 1
#test returns num of words for given string > 1
def test_count_words_multi_returns_multi():
    result = count_words("one two three")
    assert result == 3

#raises error when anything not of type string is passed as an argument
def test_count_words_int_raises_error():
    with pytest.raises(Exception) as e:
        count_words(9)
    error_message = str(e.value)
    assert error_message == "Can't pass integer to function."
