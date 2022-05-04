from typing import List, Tuple, Union

def extended_euclid(a: int, b: int) -> Tuple[int, List[int]]:
    # Розширений алгоритм Евкліда
    if a > b:
        r_prev, r_cur = a, b
    else: r_prev, r_cur = b, a
    q = []
    while r_cur != 0:
        q_cur = r_prev // r_cur
        q.append(q_cur)
        r_next = r_prev % r_cur
        r_prev, r_cur = r_cur, r_next
    return r_prev, q

def inversed_element(a: int, n: int) -> Union[int, bool]:
    # Пошук оберненого a за модулем n
    u_prev, u_cur = 1, 0
    gcd, q = extended_euclid(a % n, n)
    if gcd == 1:
        for el in reversed(q):
            u_next = u_prev - el * u_cur
            u_prev, u_cur = u_cur, u_next
        return u_next
    return False

def solve_congruence(eq: Tuple[int, int, int]) -> Union[List[Tuple[int, int]], bool]:
    # Розв'язання лінійної конґруенції ax = b (mod n)
    n = eq[2]
    a, b = eq[0] % n, eq[1] % n
    if 0 < a < n and 0 < b < n:
        d1_1 = extended_euclid(a, n)[0]
        d1_2 = extended_euclid(b, n)[0]
        if d1_1 == d1_2 and d1_1 != 1:
            a //= d1_1
            b //= d1_1
            n //= d1_1
        elif d1_1 != 1 and d1_2 == 1: 
            return False

        d2 = extended_euclid(a, b)[0]
        if d2 != 1:
            a //= d2
            b //= d2

        x = [b * inversed_element(a, n) % n + i * eq[2] // d1_1 for i in range(d1_1)]
        return x
    return False