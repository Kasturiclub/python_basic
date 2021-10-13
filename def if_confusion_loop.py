def if_confusion(
      x, y):
 
  if x > y:
    if x - 5 > 0: 
      x=y
      return "A" if y == y + y else "B"
 
    elif x + y > 0:
      while x > y: x -= 1
      while y > x: y -= 1
      if x == y:
        return "E"
 
  else:
    if x - 2 > y - 4:
      x_old = x
      x=y*y
      y = 2 * x_old
      
      if (x - 4) ** 2 > (y - 7) ** 2:
        return "C"
      return "D"
    return "F"
 
 
print(if_confusion(3, 7))