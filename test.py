class Emp:
    def __init__(self, f, l, p):
        self.f = f
        self.l = l
        self.p = p
        self.e = f"{f}{l}@company.com"


emp1 = Emp("Desmond", "Osabutey", 6000)

emp2 = Emp("Kelly", "Prosper", 60000)
print(emp2.e)
