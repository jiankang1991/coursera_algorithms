
import numpy as np



#########################################
# matrix objects for strassen matrix multiplication
#########################################

class mtx:

    def __init__(self, mtx_list):

        self.mtx = mtx_list
        self.n = len(mtx_list)
    
    def __add__(self, other):

        tmp = [[self.mtx[i][j]+other.mtx[i][j] for j in range(self.n)] for i in range(self.n)]

        return mtx(tmp)

    def __sub__(self, other):

        tmp = [[self.mtx[i][j]-other.mtx[i][j] for j in range(self.n)] for i in range(self.n)]

        return mtx(tmp)
        

    def __mul__(self, other):

        C = [[0 for j in range(self.n)] for i in range(self.n)]

        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    C[i][j] += self.mtx[i][k] * other.mtx[k][j]

        return mtx(C)

    def strassen_multi(self, Y):

        if self.n > 2:

            mid_n = self.n//2

            XY = mtx([[0 for j in range(self.n)] for i in range(self.n)])

            A = mtx([[self.mtx[i][j] for j in range(mid_n)] for i in range(mid_n)])
            B = mtx([[self.mtx[i][j] for j in range(-mid_n, 0)] for i in range(mid_n)])
            C = mtx([[self.mtx[i][j] for j in range(mid_n)] for i in range(-mid_n, 0)])
            D = mtx([[self.mtx[i][j] for j in range(-mid_n, 0)] for i in range(-mid_n, 0)])

            E = mtx([[Y.mtx[i][j] for j in range(mid_n)] for i in range(mid_n)])
            F = mtx([[Y.mtx[i][j] for j in range(-mid_n, 0)] for i in range(mid_n)])
            G = mtx([[Y.mtx[i][j] for j in range(mid_n)] for i in range(-mid_n, 0)])
            H = mtx([[Y.mtx[i][j] for j in range(-mid_n, 0)] for i in range(-mid_n, 0)])

            F_H = F - H
            P_1 = A.strassen_multi(F_H)

            A_B = A + B
            P_2 = A_B.strassen_multi(H)
            
            C_D = C + D
            P_3 = C_D.strassen_multi(E)

            G_E = G - E
            P_4 = D.strassen_multi(G_E)

            A_D = A + D
            E_H = E + H
            P_5 = A_D.strassen_multi(E_H)

            B_D = B - D
            G_H = G + H
            P_6 = B_D.strassen_multi(G_H)

            A_C = A - C
            E_F = E + F
            P_7 = A_C.strassen_multi(E_F)

            P5_P4_P2_P6 = P_5 + P_4 - P_2 + P_6

            P1_P2 = P_1 + P_2

            P3_P4 = P_3 + P_4

            P1_P5_P3_P7 = P_1 + P_5 - P_3 - P_7


            for i in range(mid_n):
                for j in range(mid_n):

                    XY.mtx[i][j] = P5_P4_P2_P6.mtx[i][j]
                    XY.mtx[i][j+mid_n] = P1_P2.mtx[i][j]
                    XY.mtx[i+mid_n][j] = P3_P4.mtx[i][j]
                    XY.mtx[i+mid_n][j+mid_n] = P1_P5_P3_P7.mtx[i][j]
            
            return XY
        else:
            return self * Y


def strassen_multi_mtx(X, Y):

    # print()
    # print(X.mtx)
    # print(Y.mtx)

    if X.n>2:
        
        mid_n = X.n//2

        XY = [[0 for j in range(X.n)] for i in range(X.n)]

        B = mtx([[X.mtx[i][j] for j in range(-mid_n, 0)] for i in range(mid_n)])
        A = mtx([[X.mtx[i][j] for j in range(mid_n)] for i in range(mid_n)])
        C = mtx([[X.mtx[i][j] for j in range(mid_n)] for i in range(-mid_n, 0)])
        D = mtx([[X.mtx[i][j] for j in range(-mid_n, 0)] for i in range(-mid_n, 0)])

        E = mtx([[Y.mtx[i][j] for j in range(mid_n)] for i in range(mid_n)])
        F = mtx([[Y.mtx[i][j] for j in range(-mid_n, 0)] for i in range(mid_n)])
        G = mtx([[Y.mtx[i][j] for j in range(mid_n)] for i in range(-mid_n, 0)])
        H = mtx([[Y.mtx[i][j] for j in range(-mid_n, 0)] for i in range(-mid_n, 0)])

        F_H = F - H
        P_1 = strassen_multi_mtx(A, F_H)

        A_B = A + B
        P_2 = strassen_multi_mtx(A_B, H)
        
        C_D = C + D
        P_3 = strassen_multi_mtx(C_D, E)

        G_E = G - E
        P_4 = strassen_multi_mtx(D, G_E)

        A_D = A + D
        E_H = E + H
        P_5 = strassen_multi_mtx(A_D, E_H)

        B_D = B - D
        G_H = G + H
        P_6 = strassen_multi_mtx(B_D, G_H)

        A_C = A - C
        E_F = E + F
        P_7 = strassen_multi_mtx(A_C, E_F)

        P5_P4_P2_P6 = P_5 + P_4 - P_2 + P_6

        P1_P2 = P_1 + P_2

        P3_P4 = P_3 + P_4

        P1_P5_P3_P7 = P_1 + P_5 - P_3 - P_7

        

        for i in range(mid_n):
            for j in range(mid_n):

                XY[i][j] = P5_P4_P2_P6.mtx[i][j]
                XY[i][j+mid_n] = P1_P2.mtx[i][j]
                XY[i+mid_n][j] = P3_P4.mtx[i][j]
                XY[i+mid_n][j+mid_n] = P1_P5_P3_P7.mtx[i][j]
        

        return mtx(XY)
                
    else:
        return X * Y


#######################################
# function model for strassen matrix multiplication
#######################################
def base_multi(A, B):
    
    n = len(A)


    C = [[0 for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C

def mtx_add(A, B):

    n = len(A)

    C = [[A[i][j]+B[i][j] for j in range(n)] for i in range(n)]

    return C

def mtx_sub(A, B):

    n = len(A)

    C = [[A[i][j]-B[i][j] for j in range(n)] for i in range(n)]

    return C

def strassen_multi(X, Y):

    n = len(X)

    # print()
    # print(X)
    # print(Y)

    if n>2:
        
        mid_n = n//2

        XY = [[0 for j in range(n)] for i in range(n)]

        A = [[X[i][j] for j in range(mid_n)] for i in range(mid_n)]
        B = [[X[i][j] for j in range(-mid_n, 0)] for i in range(mid_n)]
        C = [[X[i][j] for j in range(mid_n)] for i in range(-mid_n, 0)]
        D = [[X[i][j] for j in range(-mid_n, 0)] for i in range(-mid_n, 0)]

        E = [[Y[i][j] for j in range(mid_n)] for i in range(mid_n)]
        F = [[Y[i][j] for j in range(-mid_n, 0)] for i in range(mid_n)]
        G = [[Y[i][j] for j in range(mid_n)] for i in range(-mid_n, 0)]
        H = [[Y[i][j] for j in range(-mid_n, 0)] for i in range(-mid_n, 0)]

        F_H = mtx_sub(F, H)
        P_1 = strassen_multi(A, F_H)

        A_B = mtx_add(A, B)
        P_2 = strassen_multi(A_B, H)
        
        C_D = mtx_add(C, D)
        P_3 = strassen_multi(C_D, E)

        G_E = mtx_sub(G, E)
        P_4 = strassen_multi(D, G_E)

        A_D = mtx_add(A, D)
        E_H = mtx_add(E, H)
        P_5 = strassen_multi(A_D, E_H)

        B_D = mtx_sub(B, D)
        G_H = mtx_add(G, H)
        P_6 = strassen_multi(B_D, G_H)

        A_C = mtx_sub(A, C)
        E_F = mtx_add(E, F)
        P_7 = strassen_multi(A_C, E_F)

        P5_P4 = mtx_add(P_5, P_4)
        P5_P4_P2 = mtx_sub(P5_P4, P_2)
        P5_P4_P2_P6 = mtx_add(P5_P4_P2, P_6)

        P1_P2 = mtx_add(P_1, P_2)

        P3_P4 = mtx_add(P_3, P_4)

        P1_P5 = mtx_add(P_1, P_5)
        P1_P5_P3 = mtx_sub(P1_P5, P_3)
        P1_P5_P3_P7 = mtx_sub(P1_P5_P3, P_7)

        # print(P1_P5_P3_P7)

        for i in range(mid_n):
            for j in range(mid_n):
                XY[i][j] = P5_P4_P2_P6[i][j]
        
        for i in range(mid_n):
            for j in range(mid_n, n):
                XY[i][j] = P1_P2[i][j-mid_n]
        
        for i in range(mid_n, n):
            for j in range(mid_n):
                XY[i][j] = P3_P4[i-mid_n][j]
        
        for i in range(mid_n, n):
            for j in range(mid_n, n):
                XY[i][j] = P1_P5_P3_P7[i-mid_n][j-mid_n]
        

        return XY
                
    else:
        return base_multi(X, Y)



if __name__ == "__main__":
    
    A = [[1,2,3,4],
         [1,2,3,4],
         [1,2,3,4],
         [1,2,3,4]]

    B = [[5,6,7,8],
         [5,6,7,8],
         [5,6,7,8],
         [5,6,7,8]]
    
    C = strassen_multi(A, B)

    # print(C)


    np_A = np.array(A)
    np_B = np.array(B)
    np_C = np.matmul(np_A, np_B)

    # print(np_C)


    np_A1 = np.random.rand(8,8)
    np_B1 = np.random.rand(8,8)
    np_C1 = np.matmul(np_A1, np_B1)

    # print(np_C1)


    # C1 = strassen_multi(np_A1.tolist(), np_B1.tolist())

    # print(C1)

    # print(np.linalg.norm(np.array(C1) - np_C1))


    mtx_A = mtx(A)
    mtx_B = mtx(B)
    
    mtx_C = mtx_A.strassen_multi(mtx_B)

    # print(mtx_A.mtx)
    # print(mtx_B.mtx)
    # print(mtx_C.mtx)


    mtx_A1 = mtx(np_A1.tolist())
    mtx_B1 = mtx(np_B1.tolist())

    mtx_C1 = mtx_A1.strassen_multi(mtx_B1)

    # print(mtx_A.mtx)
    # print(mtx_B.mtx)
    # print(mtx_C1.mtx)

    print(np.linalg.norm(np.array(mtx_C1.mtx) - np_C1))





















