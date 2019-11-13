class A:
    def__str__(self):
        return"A"
class B(A):
    def__str__(self):
        return"B"
class C(B):
    def__str__(self):
        return"C"
def main():
    b=B()
    a=A()
    c=C()
    print(a,b,c)
main()