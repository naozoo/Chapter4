def fib(n):
    """フィボナッチ数を表示"""
    a, b = 0, 1
    while b < n:
        print("b = ", b)
        a, b = b, a + b
    print()
    
def fib2(n):
    """"フィボナッチ数のリストを返す"""
    ans = []
    a, b = 0, 1
    while b < n:
        ans.append(b)
        a, b = b, a + b
    return ans
