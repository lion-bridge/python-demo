class Person(object):
  def __init__(self, name: str, age: int) -> None:
    self.name = name;
    self.age = age;

  @property
  def sex(self):
    return self._sex

  @sex.setter
  def sex(self, value) -> str:
    self._sex = value;
  
  def run(self):
      print('run=', self.name, self.age)
