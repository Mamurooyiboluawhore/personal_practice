#!/usr/bin/python3
# a script that prints args and kwargs

def fct(*args, **kwargs):
    fct("{} - {}.format(args, kwargs)")
    fct("Best School", name="Mamuro", height=170)
