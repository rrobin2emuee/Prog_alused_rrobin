def summa(a, b):
    return a + b
def lahutamine(a, b):
    return a - b
def korrutamine(a, b):
    return a * b
def jagamine(a, b):
    return a / b
def taisarvuline_jagamine(a, b):
    return a // b

operaatorid = {
    "+": summa,
    "-": lahutamine,
    "*": korrutamine,
    "/": jagamine,
    "//": taisarvuline_jagamine
}
