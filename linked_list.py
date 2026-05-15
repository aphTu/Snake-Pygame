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
    
  def removeAtHead(self):
    if self.len == 0 or self.headNode is None:
        raise IndexError("Cannot delete item from an empty linked list")

    removed_node = self.headNode
    val = removed_node.val

    self.headNode = removed_node.next

    if self.headNode is None:
        self.tailNode = None
    else:
        self.headNode.prev = None

    self.len -= 1

    return val


  def removeAtTail(self):
    if self.len==0 or self.tailNode is None:
      raise IndexError("Cannot delete items from an empty linked list")
    
    remove_node = self.tailNode
    val = remove_node.val
    self.tailNode = remove_node.prev

    if self.tailNode is None:
      self.headNode = None
    else:
      self.tailNode.next = None
    self.len -=1
    return val
  
  def removeAtIndex(self, index):
    if self.len == 0 or self.headNode is None or self.tailNode is None:
      return IndexError("Cannot delete items from an empty linked list")
    if self.len <= index or index < 0:
      return IndexError("Cannot delete an out of bound item")
    if index == 0:
      return self.removeAtHead()
    else :
      i = 0
      curr_ptr = self.headNode
      while(curr_ptr is not None and i!= index):
        curr_ptr= curr_ptr.next
        i+=1
      # currently at that index or at tail
      if curr_ptr is None or i+1 == self.len:
        return self.removeAtTail()
      else:
        remove_node = curr_ptr
        next_node = remove_node.next
        prev_node = remove_node.prev
        next_node.prev = prev_node
        prev_node.next = next_node
        val = remove_node.val
        self.len-=1
        return val

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
  def getLen(self):
    return self.len