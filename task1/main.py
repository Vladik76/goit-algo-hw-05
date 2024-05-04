def caching_fibonacci():
    """
    This outer function creates inner function fibonacci and cache
    """
    cache={}

    def fibonacci(n:int):
        """
         This inner function calculates Fibonacci numbers
         """
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return  cache.get(n,1) #if current  value already in the cache we return it
        
        cache[n] = fibonacci(n-1) + fibonacci(n-2) # otherwise, we calculate value and save it to the cache

        return cache[n]
    
    return fibonacci

        