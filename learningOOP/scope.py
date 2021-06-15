""" At any time during execution, there are 3 or 4 nested scopes whose namespaces are directly accessible:

    1. the innermost scope, which is searched first, contains the local names

    2. the scopes of any enclosing functions, which are searched starting with the nearest enclosing scope,
    contains non-local, but also non-global names

    3. the next-to-last scope contains the current module’s global names

    4. the outermost scope (searched last) is the namespace containing built-in names
"""
# Checking the scope of variable assignment


def scope_test():
    # local assignment of a variable
    def do_local():
        spam = "local"

    # non local assignment
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal"

    # global assignment of a variable
    def do_global():
        global spam
        spam = "global"

    spam = "test"

    do_local()
    print("Spam local: " + spam)
    do_nonlocal()
    print("Spam nonlocal: " + spam)
    do_global()
    print("spam global: " + spam)


scope_test()
print("In global scope: " + spam)
