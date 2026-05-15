from linked_list import LinkedList
class Queue():
  def __init__(self):
    self.queue = LinkedList()

  def enqueue(self, val):
    self.queue.insertTail(val)
  
  def dequeue(self):
    if self.isEmpty():
      return None
    return self.queue.removeAtHead()
  
  def peek(self):
    if self.queue.headNode is not None:
      return self.queue.headNode.val
    return None
  
  def isEmpty(self):
    return self.queue.isEmpty()
  
  def __repr__(self):
    return self.__str__
  
  def __str__ (self):
    return self.queue.returnLinkedList()