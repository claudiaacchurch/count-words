'''As a user
So that I can improve my grammar
I want to verify that a text starts with
 a capital letter and ends with a suitable 
 sentence-ending punctuation mark.
'''

#func name
#parameters

def check_grammar(text):
    if type(text) != str:
        return False
    is_lower = text[0].isupper()
    is_punctuation = text[-1] in "!?."
    return is_lower and is_punctuation

    #returns True/ False