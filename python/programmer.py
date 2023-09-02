class Programmer:
    def __init__(self, fullname, role):
        names = fullname.split()

        self.firstname = names[0]
        self.lastname = names[-1]
        if len(names) > 2:
            othernames = ""
            for i in names[1:-1]:
                othernames += i+' '
            self.othernames = othernames[:-1]
        self.fullname = fullname
        self.role = role
        self.email = f'{self.firstname.lower()}.{self.lastname.lower()}@tma.org'

    def info(self):
        print(f'Name:\t{self.fullname}\nRole:\t{self.role}\nEmail:\t{self.email}')
