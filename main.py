def fib_recursive(n, counts):
    """
    Return the nth Fibonacci number. 
    counts is a list of n+1 elements, where counts[i] is incremented
    each time fib_recursive(i, counts) is called.
    """    
    counts[n] += 1
    ###TODO
    pass
    
def test_fib_recursive():
    n = 10
    counts = [0] * (n+1)
    assert fib_recursive(n, counts) == 55
    print(counts)
    print(sum(counts))
    
def fib_top_down(n, fibs):
    ###TODO
    pass

def test_fib_top_down():
    n = 10
    fibs = [-1] * (n+1)
    assert fib_top_down(n, fibs) == 55
    print(fibs)

def fib_bottom_up(n):
    ###TODO
    pass

def test_fib_bottom_up():
    n = 10
    assert fib_bottom_up(n) == 55


def fib_bottom_up_better(n):
    ###TODO
    pass

def test_fib_bottom_up_better():
    n = 10
    assert fib_bottom_up_better(n) == 55