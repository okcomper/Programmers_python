def solution(n, k):
    q = k - (n // 10)
    answer = (12000 * n) + (2000 * q)
    return answer