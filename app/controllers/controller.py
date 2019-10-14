class Controller:

  def toLIST(self, items):
    __new_list = []
    for item in items:
      __new_list.append(item.toDICT())
    return __new_list
