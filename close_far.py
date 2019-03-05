def close_far(a, b, c):
  if abs(b-a)<=1:
    if abs(c-a)>=2 and abs(c-b)>=2:
      return True
    else:
      return False
  elif abs(c-a)<=1:
    if abs(b-a)>=2 and abs(b-c)>=2:
      return True
    else:
      return False
  else:
    return False
def test_too_close():
    x = close_far(1,2,3)
    assert not x
