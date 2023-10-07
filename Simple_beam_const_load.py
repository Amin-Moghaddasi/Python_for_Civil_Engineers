def simple_const_beam(l,a,P):
    b = l - a
    Ay = (P * b)/l
    By = (P * a)/l
    return Ay, By

print(simple_const_beam(l=13,a=4.5,P=55))
