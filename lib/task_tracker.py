''' As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO'''

#name of function and arguments
def task_tracker(text):
    if type(text) != str:
        raise Exception("Hello there you are not #TODO")
    elif text == "" or "#TODO" not in text:
        return False
    else:
        return True

    #returns boolean