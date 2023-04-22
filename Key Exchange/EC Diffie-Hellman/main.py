# Written by Hunter Richardson 2023
# Uses NIST P-256 curve


import random

from utils import P_256

def point_operation(P, Q, a, p):
    if P != Q:
        S = ((Q[1] - P[1]) * (pow(Q[0] - P[0], p-2, p))) % p
    else:
        S = ((3 * P[0] ** 2 + a) * pow(2*P[1], p-2, p)) % p


    x = (pow(S, 2) - P[0] - Q[0]) % p
    y = (S*(P[0] - x)- P[1]) % p

    return [x, y]


def doubleAndAdd(c, P, a, p):
    T = P
    for i in c:
         T = point_operation(T, T, a, p)
         if i == "1":
             T = point_operation(T, P, a, p)
    return T



def main():
    E = P_256()
    P = [E.gx, E.gy]

    a = format(random.randint(2, E.n - 1), 'b')
    keyA = doubleAndAdd(a, P, E.a, E.p)

    b = format(random.randint(2, E.n - 1), 'b')
    keyB = doubleAndAdd(b, P, E.a, E.p)

    keyAB = doubleAndAdd(a, keyB, E.a, E.p)
    keyBA = doubleAndAdd(b, keyA, E.a, E.p)

    if keyAB == keyBA:
        print("The lists are identical")

    print(keyAB)
    print(keyBA)


if __name__ == '__main__':
    main()
