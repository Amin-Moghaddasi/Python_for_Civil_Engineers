from sympy import symbols, integrate


class Simple_Beam:
    @staticmethod
    def simple_beam_dist_load_Ay(P_x, l, x_0, x_1):
        x = symbols('x')
        expr_1 = x * P_x
        Ay = integrate(P_x, (x, x_0, x_1)) - (integrate(expr_1, (x, x_0, x_1))) / l

        return Ay

    @staticmethod
    def simple_beam_dist_load_By(P_x, l, x_0, x_1):
        x = symbols('x')
        expr_1 = x * P_x
        By = integrate(expr_1, (x, x_0, x_1)) / l
        return  By

    @staticmethod
    def simple_const_beam_Ay(l, a, P):
        b = l - a
        Ay = (P * b) / l
        return Ay
    @staticmethod
    def simple_const_beam_By(l, a, P):
        b = l - a
        By = (P * a) / l
        return By


    @staticmethod
    def combo(loads):
        dist_list =[]
        const_list =[]
        print(len(loads))
        for i in range (len(loads)):
                if loads[i][0] == 'Dist':
                    dist_list.append(loads[i])
                elif loads[i][0] == 'Const':
                    const_list.append(loads[i])
                else:
                    print("Error!")
        Ay = 0
        By = 0
        print(f"Const list : {const_list}")
        print(f"Dist list : {dist_list}")
        for k in range(len(dist_list)):
            Ay += Simple_Beam.simple_beam_dist_load_Ay(P_x =dist_list[k][1],l= dist_list[k][2],x_0=dist_list[k][3],x_1=dist_list[k][4])
            By += Simple_Beam.simple_beam_dist_load_By(P_x=dist_list[k][1], l=dist_list[k][2], x_0=dist_list[k][3],
                                                x_1=dist_list[k][4])
        for g in range(len(const_list)):
            Ay += Simple_Beam.simple_const_beam_Ay(l=const_list[g][1],a=const_list[g][2],P=const_list[g][3])
            By += Simple_Beam.simple_const_beam_By(l=const_list[g][1],a=const_list[g][2],P=const_list[g][3])
        return Ay, By
