from sympy import symbols, integrate


class Simple_Beam:
    def simple_beam_dist_load(P_x, l):
        x = symbols('x')
        expr_1 = x * P_x
        Ay = integrate(P_x, (x, 0, l)) - (integrate(expr_1, (x, 0, l))) / l
        By = integrate(expr_1, (x, 0, l)) / l
        return Ay, By

    def simple_const_beam(l, a, P):
        b = l - a
        Ay = (P * b) / l
        By = (P * a) / l
        return Ay, By
