class Fila():
  def __init__(self):
    self.items = []

  def esta_vazia(self):
    return self.items == []

  def tamanho(self):
    return len(self.items)

  def enfileira(self, item):
    self.items.insert(0, item)

  def desinfileira(self):
    if self.tamanho() == 0:
      return None
    else:
       return self.items.pop()

