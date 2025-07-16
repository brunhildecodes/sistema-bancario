class Pilha:
  def __init__(self):
    self.items = []

  def push(self, item):
    self.items.append(item)

  def tamanho(self):
    return len(self.items)

  def pop(self):
    if self.tamanho() == 0:
      return None
    else:
      return self.items.pop()

  def topo(self):
    return self.items[-1]

  def esta_vazia(self):
    return self.items == []