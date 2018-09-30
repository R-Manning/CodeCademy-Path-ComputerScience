from linked_list import Node, LinkedList
from blossom_lib import flower_definitions

class HashMap:
  
  def __init__(self, size):
    self.array_size = size
    
    self.array = [LinkedList() for i in range(self.array_size)]
    
  def hash(self, key):
    return sum(key.encode())
  
  def compress(self, hash_code):
    return hash_code % self.array_size
  
  def assign(self, key, value):
    array_index = self.compress(self.hash(key))
    payload = Node([key, value])
    list_at_array = self.array[array_index]
    for item in list_at_array:
      if item[0] == key:
        item[1] = value
        return
    list_at_array.insert(payload)
    #not sure if this is the correct way to do this
    
  def retrieve(self, key):
    array_index = self.compress(self.hash(key))
    list_at_index = self.array[array_index]
    for item in list_at_index:
      if item[0] == key:
        return item[1]
      else:
        return None
    
    if payload != None:
      if payload[0] == key:
        return payload[1]
      else:
        return None
    else:
      return None
    
    
blossom = HashMap(len(flower_definitions))
for flower in flower_definitions:
  blossom.assign(flower[0], flower[1])
  
