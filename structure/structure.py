
class greeter(object):
  # constructor
  def __init__(self, name='greeter'):
    self.name = name

  # method
  def greet(self, msg='Hello World'):
    print(msg)

def hi(msg='Say Hi'):
	print(msg)

if __name__ == '__main__':
  h1 = greeter()
  h1.greet()