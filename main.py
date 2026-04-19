from enum import Enum, auto

class Ruxsatlar(Enum):
    READ = auto()
    WRITE = auto()
    DELETE = auto()

class User:
    def __init__(self, ism, ruxsatlar=None):
        self.ism = ism
        self.ruxsatlar = ruxsatlar if ruxsatlar else set()

    def qo'sh_ruxsat(self, ruxsat):
        self.ruxsatlar.add(ruxsat)

    def olib_tashlash_ruxsat(self, ruxsat):
        self.ruxsatlar.discard(ruxsat)

    def ruxsatlarini_kontroll_qil(self, ruxsat):
        return ruxsat in self.ruxsatlar

class RuxsatlarTizimi:
    def __init__(self):
        self.ruxsatlar = Ruxsatlar

    def boshqar_ruxsat(self, user, ruxsat, qo'shish=True):
        if qo'shish:
            user.qo'sh_ruxsat(ruxsat)
        else:
            user.olib_tashlash_ruxsat(ruxsat)

# Misol:
ruxsatlar_tizimi = RuxsatlarTizimi()
user = User("Ali")

ruxsatlar_tizimi.boshqar_ruxsat(user, Ruxsatlar.READ, qo'shish=True)
print(user.ruxsatlarini_kontroll_qil(Ruxsatlar.READ))  # True

ruxsatlar_tizimi.boshqar_ruxsat(user, Ruxsatlar.DELETE, qo'shish=False)
print(user.ruxsatlarini_kontroll_qil(Ruxsatlar.DELETE))  # False
