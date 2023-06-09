def say_hello(name):
    if type(name) != str:
        raise Exception('you are not a number')
    return f"hello {name}"


# Intended output:
#
# > say_hello("kay")
# => "hello kay"
# debug function to return the above text
# parameters name
#  returns 'hello name'
# side effects