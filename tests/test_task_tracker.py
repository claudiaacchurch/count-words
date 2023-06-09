from lib.task_tracker import *
import pytest

#if text is empty string return false
def test_task_tracker_empty_returns_false():
    result = task_tracker("")
    assert result == False

#if text doesn't contain string return False
def test_task_tracker_doesnt_contain_string_return_false():
    result = task_tracker("Hello there!")
    assert result == False
#if text contains string return True
def test_task_tracker_contains_string_return_true():
    result = task_tracker("hello #TODO")
    assert result == True

#if text isn't a str return Exception
def test_task_tracker_isnt_str_return_exception():
    with pytest.raises(Exception) as e:
        task_tracker(90)
    error_message = str(e.value)
    assert error_message == "Hello there you are not #TODO"