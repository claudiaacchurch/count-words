from lib.check_grammar import *
import pytest

#returns False with non-str input 
def test_check_grammar_returns_false_no_input():
    result = check_grammar(90)
    assert result == False
#returns False with a lower case start letter
def test_check_grammar_returns_false_for_lowercase():
    result = check_grammar("hello there!")
    assert result == False
#returns False with non-sentance ending punctuation mark
def test_check_grammar_no_punctuation_returns_false():
    result = check_grammar("Hello there")
    assert result ==  False

#else returns True
def test_check_grammar_returns_true():
    result = check_grammar("Hello there.")
    assert result == True