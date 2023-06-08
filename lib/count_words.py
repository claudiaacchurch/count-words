def count_words(string):
    #if not isinstance(string, str):
    if type(string) != str:
        raise Exception("Can't pass integer to function.")
    split_str = string.split()
    return len(split_str)