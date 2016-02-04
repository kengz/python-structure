
class Structure(object):
  # constructor
  def __init__(self, name='greeter'):
    self.name = name

  # method
  def greet(self, msg='Hello World'):
    print msg


if __name__ == '__main__':
  h1 = Structure()
  h1.greet()