def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
          d[c] += 1
    return d
  
>>> h = histogram('brontosaurus')
>>> h
{'a':1, 'b':1, 'o': 2, 'n':1, 's':2, 'r':2, 'u':2, 't':1}

          
