l1 = [1, 2, 3, 4]
l1_iter = iter(l1)

print(next(l1_iter))
print(next(l1_iter))
print(next(l1_iter))
print(next(l1_iter))

l1_iter = iter(l1)
for _ in l1_iter:
    print(_, end=" ")
print()


class MyNumbers:
  def __iter__(self):
    self.a = 10
    return self
 
  def __next__(self):
      if self.a<=30:
          x = self.a
          self.a += 10
          return x
      else:
          raise StopIteration
 
myclass = MyNumbers()
myiter = iter(myclass)
 
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))