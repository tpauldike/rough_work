from programmer import Programmer

prog1 = Programmer("Ebube Anyanwu", "Frontend developer")

prog1.info()
#print(prog1.lastname)
prog2 = Programmer("Josh Japhet Klein Adams", "DevOps")
print('''
prog2 has other names such as '{}' but here are his full details:
'''.format(prog2.othernames))
prog2.info()
