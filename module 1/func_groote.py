def groote(nr1, nr2):
  if nr1 > nr2:
    return f"nr 1: ({nr1}) is grooter dan nr 2: ({nr2})"
  elif nr2 > nr1:
    return f"nr 2: ({nr2}) is grooter dan nr 1: ({nr1})"
  else:
    return f"nr 1: ({nr1}) is net zo groot als nr 2: ({nr2})"
  
print(groote(4, 5))
print(groote(5, 4))
print(groote(4, 4))