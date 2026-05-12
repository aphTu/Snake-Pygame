class Node():
  def __init__(self,  val, prev, next ):
    self.next = next
    self.val = val
    self.prev = prev

  def updateNext(self,address):
    self.next = address
  def updateVal(self, val):
    self.val = val
  def updatePrev(self, prev):
    self.prev = prev
  def __eq__(self, other):
    if not isinstance(other, Node):
      return NotImplemented
    return self.val == other.val and self.next == other.next and self.prev == other.prev
  def __lt__(self,other):
    if not isinstance(other, Node):
      return NotImplemented
    return self.val < other.val
  
  def __gt__(self, other):
    if not isinstance(other, Node):
      return NotImplemented
    return self.val > other.val
  def __ge__(self,other):
    if not isinstance(other, Node):
      return NotImplemented
    return self.val >= other.val
  def __le__(self,other):
    if not isinstance(other, Node):
      return NotImplemented
    return self.val<=other.val

class linkedList():
  def __init__(self):
    self.headNode = None
    self.tailNode = None


  def insertHead(self, val):
    if self.headNode is None:
      newNode = Node(val, None, None)
      self.tailNode = newNode
      self.headNode = newNode
    else:
      newNode = Node(val,None, self.headNode)
      self.headNode = newNode
  
  def insertTail(self, val):
    # if self.tailNode is None, it mean that there are no node within the linked list
    if self.tailNode is None:
      newNode = Node(val, None, None)
      self.tailNode = newNode
      self.headNode = newNode
    else:
      newNode = Node(val, self.tailNode, None)
      self.tailNode = newNode
  
  def insertAtIndex(self, val, index):
    if self.headNode is None:
      self.insertHead(val)
    else:
      curr_ptr = self.headNode
      i = 0
      while(curr_ptr.next is not None or i != index):
        i+=1
        curr_ptr = curr_ptr.next
      # now we are the correct index or at tail
      if curr_ptr is None:
        self.insertTail(val)
      else:
        newNode = Node(val )
      
    