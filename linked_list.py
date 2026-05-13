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
  def __str__(self):
    _str = ""
    if self.prev is None: 
      _str+="None, "
    else:
      _str+=f"{self.prev.val}, "
    if self.val is not None:
      _str +=f"{self.val}"
    if self.next is None:
      _str+=", None"
    else:
      _str+=f", {self.next.val}"
    return _str

class linkedList():
  def __init__(self):
    self.headNode = None
    self.tailNode = None
    self.len = 0
    


  def insertHead(self, val):
    if self.headNode is None:
      newNode = Node(val, None, None)
      self.tailNode = newNode
      self.headNode = newNode
    else:
      newNode = Node(val,None, self.headNode)
      self.headNode.prev = newNode
      self.headNode = newNode
    self.len+=1
  
  def insertTail(self, val):
    # if self.tailNode is None, it mean that there are no node within the linked list
    if self.tailNode is None:
      newNode = Node(val, None, None)
      self.tailNode = newNode
      self.headNode = newNode
    else:
      newNode = Node(val, self.tailNode, None)
      self.tailNode.next = newNode
      self.tailNode = newNode
      
    self.len+=1

  
  def insertAtIndex(self, val, index):
    if self.headNode is None:
      self.insertHead(val)
    else:
      curr_ptr = self.headNode
      i = 0
      while curr_ptr is not None and i != index:
        i+=1
        curr_ptr = curr_ptr.next
      # now we are the correct index or at tail
      if curr_ptr is None or index+1 == self.len:
        self.insertTail(val)
      else:
        nextNode = curr_ptr.next

        newNode = Node(val, prev =curr_ptr, next= nextNode)
        
        if nextNode is not None:
          nextNode.prev = newNode
        curr_ptr.next = newNode
        # print(newNode)
        self.len+=1
    
  def printLinkedList(self):
    curr_ptr = self.headNode
    while curr_ptr is not None:
      print(curr_ptr.val, sep=" ")
      curr_ptr = curr_ptr.next
    print("")
  def returnLinkedList(self):
    _str= ""
    curr_ptr = self.headNode
    while curr_ptr is not None:
      _str+= f"{curr_ptr.val} "
      curr_ptr = curr_ptr.next
    return _str
  def returnLinkedListReverse(self):
    _str = ""
    curr_ptr = self.tailNode
    while curr_ptr is not None:
      _str+= f"{curr_ptr.val} "
      curr_ptr = curr_ptr.prev
    return _str
  