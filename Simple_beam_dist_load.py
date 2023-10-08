from sympy import *
def simple_beam_dist_load(P_x, l):
    x = symbols('x')
    expr_1 = x * P_x
    Ay = integrate(P_x,(x,0,l)) - (integrate(expr_1,(x,0,l))) / l
    By = integrate(expr_1, (x,0,l)) / l
    return Ay , By
x = symbols('x')
expr = 2*x
print(simple_beam_dist_load(P_x=expr,l=6))
