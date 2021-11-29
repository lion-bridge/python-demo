import flyable
import runnable


class SuperMan(flyable.Flybale, runnable.Runnable):
  def __init__(self) -> None:
      super().__init__()
      print('我是超人')

xMan = SuperMan();
xMan.fly();
xMan.fun();
  