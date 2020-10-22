def fib_recursive(n, counts):
    """
    Return the nth Fibonacci number. 
    counts is a list of n+1 elements, where counts[i] is incremented
    each time fib_recursive(i, counts) is called.
    """    
    counts[n] += 1
    if n == 0:
      return 0
    elif n ==1:
      return 1
    else:
      return fib_recursive(n-1,counts) + fib_recursive(n-2,counts)

    
def test_fib_recursive():
    n = 10
    counts = [0] * (n+1)
    assert fib_recursive(n, counts) == 55
    print(counts)
    print(sum(counts))
    
def fib_top_down(n, fibs):
    if n == 0:
      fibs[0] = 0
      return 0
    elif n == 1:
      fibs[1] = 1
      return 1
    elif fibs[n] != -1:
      return fibs[n]
    else:
      fibs[n] = fib_top_down(n-1, fibs) + fib_top_down(n-2, fibs)
      return fibs[n]

def test_fib_top_down():
    n = 10
    fibs = [-1] * (n+1)
    assert fib_top_down(n, fibs) == 55
    print(fibs)

def fib_bottom_up(n):
    val_list = []

    for i in range(n + 1):
      if i == 0:
        val_list.append(0)
      elif i == 1:
        val_list.append(1)
      else:
        val_list.append(val_list[i-1] + val_list[i-2])
    
    return val_list[n]

def test_fib_bottom_up():
    n = 10
    assert fib_bottom_up(n) == 55
