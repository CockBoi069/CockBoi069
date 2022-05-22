class A:
    def rn(self,r):
        print()
class B:
    def marks(self,m,e,s,ss):
        print()
class C(A,B):
    def final(self):
        print("MATHS:", m)
        print("SOCIAL SCIENCE:", ss)
        print("SCIENCE:", s)
        print("ENGLISH:", e)
        t = m + e + s + ss
        p = t * 100 / 400
        print("Total", t)
        print("Percentage:", p)

r = int(input("Enter roll number: "))
m = int(input("Enter maths marks: "))
s = int(input("Enter science marks: "))
e = int(input("Enter english marks: "))
ss = int(input("Enter socials science marks: "))

O=C()
O.rn(r)
O.marks(m,e,s,ss)
O.final()
