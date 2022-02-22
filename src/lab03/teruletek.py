import sys
import math

# def terulet(a=None,b=None, r=1)->int:
#  if r is None:
    #     r=1
#     if (a is None and b is None):
#         return r*r*math.pi
#     print(a,b)
#     if b is None:
#         b=a
#     print(a,b)
#     return a*b
#
# def teruletek():
#
#     for line in sys.stdin:
#         ln=line.split()
#         a=int(ln[0])
#         b=int(ln[1])
#         print(terulet(a,b))

def lnko(a,b):
    while b:
        a,b=b,a%b
    return a



if __name__== "__main__":
#     print(terulet(2,5))
#     print(terulet(2,3.14))
#     print(terulet(b=2,a=7))
#     print(terulet(r=2))
#     print(round(terulet(),5))
#     print(terulet())
    print(lnko(12,82))
    print(lnko(64476,123456))
