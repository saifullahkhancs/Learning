def solve(capacity, operations):
    # Implement LRU Cache and process operations
    # Return list of get results only (ignore puts)
    cache = {}
    cache_len = 0
  
    def get(key , cache):
      data = cache.get(key, None)
      if data:
        return data
      else:
        return -1
        
    def put(key ,value , cache,cache_len):

      if cache_len < capacity:
          cache[key] = value

          cache_len += 1

      else:
          removal_keys = list(cache.keys())
          print(removal_keys)
          removal_key = removal_keys[0]
          del cache[removal_key]
          

          cache[key] = value
          cache_len += 1
        

      
    output = []  
    for operation in operations:
       func = operation[0]
       key = operation[1]
       
       print(cache_len)
       if func=="get":
         output_value = get(key , cache)
         output.append(output_value)

       else:
         value = operation[2]
         put(key, value, cache , cache_len )
         cache_len += 1

    return output

result = solve(2,[["put", 1,10],["put", 2,20],["put", 3,30], ["get", 1]])
print(result)
  