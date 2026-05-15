import unittest

from linked_list import *


class TestLinkedList(unittest.TestCase):
  def test_insert_head(self):
    val  = 5
    expected = f"{val} "
    list = LinkedList()
    list.insertHead(val)
    self.assertEqual(expected, list.returnLinkedList())
    self.assertEqual(1, list.len)
    self.assertEqual(expected, list.returnLinkedListReverse())

  def test_insert_three_item_head(self):
    val  = 5
    val2 = 10
    val3 = 20
    expected = f"{val3} {val2} {val} "
    expected_reverse = f"{val} {val2} {val3} "
    list = LinkedList()
    list.insertHead(val)
    list.insertHead(val2)
    list.insertHead(val3)
    self.assertEqual(expected, list.returnLinkedList())
    self.assertEqual(3, list.len)
    self.assertEqual(expected_reverse, list.returnLinkedListReverse())



  def test_insert_tail(self):
    val  = 5
    expected = f"{val} "
    list = LinkedList()
    list.insertTail(val)
    self.assertEqual(expected, list.returnLinkedList())
    self.assertEqual(1, list.len)
    self.assertEqual(expected, list.returnLinkedListReverse())



  def test_insert_three_item_tail(self):
    val  = 5
    val2 = 10
    val3 = 20
    expected = f"{val} {val2} {val3} "
    expected_reverse = f"{val3} {val2} {val} "

    list = LinkedList()
    list.insertTail(val)
    list.insertTail(val2)
    list.insertTail(val3)
    # print(list.returnLinkedList())
    self.assertEqual(expected, list.returnLinkedList())
    self.assertEqual(3, list.len)
    self.assertEqual(expected_reverse, list.returnLinkedListReverse())

  def test_insert_at_zero_index(self):
    val  = 5
    expected = f"{val} "
    list = LinkedList()
    list.insertAtIndex(val, 0)
    self.assertEqual(expected, list.returnLinkedList())
    self.assertEqual(1, list.len)
    self.assertEqual(expected, list.returnLinkedListReverse())


  def test_insert_in_middle(self):
    val  = 5
    val2 = 10
    val3 = 20
    expected = f"{val} {val3} {val2} "
    expected_reverse = f"{val2} {val3} {val} "

    list = LinkedList()
    list.insertHead(val)
    list.insertTail(val2)
    list.insertAtIndex(val3, 0)
    # print(list.returnLinkedList())
    self.assertEqual(expected, list.returnLinkedList())
    self.assertEqual(3, list.len)
    self.assertEqual(expected_reverse, list.returnLinkedListReverse())

  def test_insert_after_head_single_node(self):
    val = 5
    val2 = 10

    expected = f"{val} {val2} "
    expected_reverse = f"{val2} {val} "

    list = LinkedList()
    list.insertHead(val)
    list.insertAtIndex(val2, 0)

    self.assertEqual(expected, list.returnLinkedList())
    self.assertEqual(2, list.len)
    self.assertEqual(expected_reverse, list.returnLinkedListReverse())


  def test_insert_after_middle_index(self):
    val = 5
    val2 = 10
    val3 = 20
    val4 = 15

    expected = f"{val} {val2} {val4} {val3} "
    expected_reverse = f"{val3} {val4} {val2} {val} "

    list = LinkedList()
    list.insertHead(val)
    list.insertTail(val2)
    list.insertTail(val3)
    list.insertAtIndex(val4, 1)

    self.assertEqual(expected, list.returnLinkedList())
    self.assertEqual(4, list.len)
    self.assertEqual(expected_reverse, list.returnLinkedListReverse())


  def test_insert_at_last_index(self):
    val = 5
    val2 = 10
    val3 = 20

    expected = f"{val} {val2} {val3} "
    expected_reverse = f"{val3} {val2} {val} "

    list = LinkedList()
    list.insertHead(val)
    list.insertTail(val2)
    list.insertAtIndex(val3, 1)

    self.assertEqual(expected, list.returnLinkedList())
    self.assertEqual(3, list.len)
    self.assertEqual(expected_reverse, list.returnLinkedListReverse())


  def test_insert_multiple_times_in_middle(self):
    val = 5
    val2 = 10
    val3 = 20
    val4 = 30

    expected = f"{val} {val3} {val4} {val2} "
    expected_reverse = f"{val2} {val4} {val3} {val} "

    list = LinkedList()
    list.insertHead(val)
    list.insertTail(val2)
    list.insertAtIndex(val3, 0)
    list.insertAtIndex(val4, 1)

    self.assertEqual(expected, list.returnLinkedList())
    self.assertEqual(4, list.len)
    self.assertEqual(expected_reverse, list.returnLinkedListReverse())


  def test_insert_negative_value_in_middle(self):
    val = 5
    val2 = 10
    val3 = -20

    expected = f"{val} {val3} {val2} "
    expected_reverse = f"{val2} {val3} {val} "

    list = LinkedList()
    list.insertHead(val)
    list.insertTail(val2)
    list.insertAtIndex(val3, 0)

    self.assertEqual(expected, list.returnLinkedList())
    self.assertEqual(3, list.len)
    self.assertEqual(expected_reverse, list.returnLinkedListReverse())


  def test_insert_zero_value_in_middle(self):
    val = 5
    val2 = 10
    val3 = 0

    expected = f"{val} {val3} {val2} "
    expected_reverse = f"{val2} {val3} {val} "

    list = LinkedList()
    list.insertHead(val)
    list.insertTail(val2)
    list.insertAtIndex(val3, 0)

    self.assertEqual(expected, list.returnLinkedList())
    self.assertEqual(3, list.len)
    self.assertEqual(expected_reverse, list.returnLinkedListReverse())


  def test_insert_keeps_head_and_tail_correct(self):
    val = 1
    val2 = 2
    val3 = 3
    val4 = 4
    val5 = 99

    expected = f"{val} {val2} {val5} {val3} {val4} "
    expected_reverse = f"{val4} {val3} {val5} {val2} {val} "

    list = LinkedList()
    list.insertHead(val)
    list.insertTail(val2)
    list.insertTail(val3)
    list.insertTail(val4)
    list.insertAtIndex(val5, 1)

    self.assertEqual(expected, list.returnLinkedList())
    self.assertEqual(5, list.len)
    self.assertEqual(expected_reverse, list.returnLinkedListReverse())

  def test_remove_item_at_head(self):
    val = 1
    val2 = 2
    val3 = 3
    val4 = 4
    val5 = 99

    expected = f"{val2} {val5} {val3} {val4} "
    expected_reverse = f"{val4} {val3} {val5} {val2} "
    expected_item = val
    list = LinkedList()
    list.insertHead(val)
    list.insertTail(val2)
    list.insertTail(val3)
    list.insertTail(val4)
    list.insertAtIndex(val5, 1)
    item = list.removeAtHead()
    self.assertEqual(expected, list.returnLinkedList())
    self.assertEqual(4, list.len)
    self.assertEqual(expected_reverse, list.returnLinkedListReverse())
    self.assertEqual(expected_item, item)

  def test_remove_two_item_at_head(self):
      val = 1
      val2 = 2
      val3 = 3
      val4 = 4
      val5 = 99

      expected = f"{val5} {val3} {val4} "
      expected_reverse = f"{val4} {val3} {val5} "
      expected_item = val
      expected_secondItem = val2
      list = LinkedList()
      list.insertHead(val)
      list.insertTail(val2)
      list.insertTail(val3)
      list.insertTail(val4)
      list.insertAtIndex(val5, 1)
      item = list.removeAtHead()
      secondItem = list.removeAtHead()
      self.assertEqual(expected, list.returnLinkedList())
      self.assertEqual(3, list.len)
      self.assertEqual(expected_reverse, list.returnLinkedListReverse())
      self.assertEqual(expected_item, item)
      self.assertEqual(expected_secondItem, secondItem)

  def test_remove_head_single_node(self):
      val = 5

      expected = ""
      expected_reverse = ""
      expected_item = val

      list = LinkedList()
      list.insertHead(val)
      item = list.removeAtHead()

      self.assertEqual(expected, list.returnLinkedList())
      self.assertEqual(0, list.len)
      self.assertEqual(expected_reverse, list.returnLinkedListReverse())
      self.assertEqual(item, expected_item)

  def test_remove_head_until_empty(self):
      val = 5
      val2 = 10
      val3 = 20

      expected = ""
      expected_reverse = ""

      list = LinkedList()
      list.insertHead(val)
      list.insertTail(val2)
      list.insertTail(val3)

      list.removeAtHead()
      list.removeAtHead()
      list.removeAtHead()

      self.assertEqual(expected, list.returnLinkedList())
      self.assertEqual(0, list.len)
      self.assertEqual(expected_reverse, list.returnLinkedListReverse())
    
  def test_remove_at_tail(self):
    val = 1
    val2 = 2
    val3 = 3
    val4 = 4
    val5 = 99

    expected = f"{val} {val2} {val5} {val3} "
    expected_reverse = f"{val3} {val5} {val2} {val} "
    expected_item = val4
    list = LinkedList()
    list.insertHead(val)
    list.insertTail(val2)
    list.insertTail(val3)
    list.insertTail(val4)
    list.insertAtIndex(val5, 1)
    item = list.removeAtTail()
    self.assertEqual(expected, list.returnLinkedList())
    self.assertEqual(4, list.getLen())
    self.assertEqual(expected_reverse, list.returnLinkedListReverse())
    self.assertEqual(expected_item, item)

  def test_remove_two_at_tail(self):
    val = 1
    val2 = 2
    val3 = 3
    val4 = 4
    val5 = 99

    expected = f"{val} {val2} {val5} "
    expected_reverse = f"{val5} {val2} {val} "
    expected_item = val4
    expected_secondItem = val3
    list = LinkedList()
    list.insertHead(val)
    list.insertTail(val2)
    list.insertTail(val3)
    list.insertTail(val4)
    list.insertAtIndex(val5, 1)
    item = list.removeAtTail()
    secondItem = list.removeAtTail()
    self.assertEqual(expected, list.returnLinkedList())
    self.assertEqual(3, list.getLen())
    self.assertEqual(expected_reverse, list.returnLinkedListReverse())
    self.assertEqual(expected_item, item)
    self.assertEqual(expected_secondItem, secondItem)

  def test_remove_single_node_tail(self):
    val = 5
    expected = ""
    expected_reverse = ""
    expected_item = val

    list = LinkedList()
    list.insertHead(val)
    item = list.removeAtTail()

    self.assertEqual(expected, list.returnLinkedList())
    self.assertEqual(0, list.len)
    self.assertEqual(expected_reverse, list.returnLinkedListReverse())
    self.assertEqual(item, expected_item)

  def test_remove_tail_until_empty(self):
    val = 5
    val2 = 10
    val3 = 20

    expected = ""
    expected_reverse = ""

    list = LinkedList()
    list.insertHead(val)
    list.insertTail(val2)
    list.insertTail(val3)

    list.removeAtTail()
    list.removeAtTail()
    list.removeAtTail()

    self.assertEqual(expected, list.returnLinkedList())
    self.assertEqual(0, list.len)
    self.assertEqual(expected_reverse, list.returnLinkedListReverse())    

  def test_remove_at_index_in_middle(self):
    val = 5
    val2 = 10
    val3 = 20

    expected = f"{val} {val3} "
    expected_reverse = f"{val3} {val} "
    expected_item = val2
    list = LinkedList()
    list.insertHead(val)
    list.insertTail(val2)
    list.insertTail(val3)
    item = list.removeAtIndex(1)

    self.assertEqual(expected, list.returnLinkedList())
    self.assertEqual(2, list.getLen())
    self.assertEqual(expected_reverse, list.returnLinkedListReverse())
    self.assertEqual(expected_item, item)

  def test_remove_at_index_head(self):
    val = 5
    val2 = 10
    val3 = 20

    expected = f"{val2} {val3} "
    expected_reverse = f"{val3} {val2} "
    expected_item = val
    list = LinkedList()
    list.insertHead(val)
    list.insertTail(val2)
    list.insertTail(val3)
    item = list.removeAtIndex(0)

    self.assertEqual(expected, list.returnLinkedList())
    self.assertEqual(2, list.getLen())
    self.assertEqual(expected_reverse, list.returnLinkedListReverse())
    self.assertEqual(expected_item, item)

  def test_remove_at_index_tail(self):
    val = 5
    val2 = 10
    val3 = 20

    expected = f"{val} {val2} "
    expected_reverse = f"{val2} {val} "
    expected_item = val3
    list = LinkedList()
    list.insertHead(val)
    list.insertTail(val2)
    list.insertTail(val3)
    item = list.removeAtIndex(2)

    self.assertEqual(expected, list.returnLinkedList())
    self.assertEqual(2, list.getLen())
    self.assertEqual(expected_reverse, list.returnLinkedListReverse())
    self.assertEqual(expected_item, item)
  
  def test_remove_at_index_single_item(self):
    val = 5

    expected = ""
    expected_reverse = ""
    expected_item = val

    list = LinkedList()
    list.insertHead(val)

    removed_item = list.removeAtIndex(0)

    self.assertEqual(expected, list.returnLinkedList())
    self.assertEqual(0, list.getLen())
    self.assertEqual(expected_reverse, list.returnLinkedListReverse())
    self.assertEqual(expected_item, removed_item)

  def test_remove_at_index_two_items_remove_head(self):
    val = 5
    val2 = 10

    expected = f"{val2} "
    expected_reverse = f"{val2} "
    expected_item = val

    list = LinkedList()
    list.insertHead(val)
    list.insertTail(val2)

    removed_item = list.removeAtIndex(0)

    self.assertEqual(expected, list.returnLinkedList())
    self.assertEqual(1, list.getLen())
    self.assertEqual(expected_reverse, list.returnLinkedListReverse())
    self.assertEqual(expected_item, removed_item)

  def test_remove_at_index_two_items_remove_tail(self):
    val = 5
    val2 = 10

    expected = f"{val} "
    expected_reverse = f"{val} "
    expected_item = val2

    list = LinkedList()
    list.insertHead(val)
    list.insertTail(val2)

    removed_item = list.removeAtIndex(1)

    self.assertEqual(expected, list.returnLinkedList())
    self.assertEqual(1, list.getLen())
    self.assertEqual(expected_reverse, list.returnLinkedListReverse())
    self.assertEqual(expected_item, removed_item)

  def test_remove_at_index_second_item(self):
    val = 5
    val2 = 10
    val3 = 20
    val4 = 30

    expected = f"{val} {val3} {val4} "
    expected_reverse = f"{val4} {val3} {val} "
    expected_item = val2

    list = LinkedList()
    list.insertHead(val)
    list.insertTail(val2)
    list.insertTail(val3)
    list.insertTail(val4)

    removed_item = list.removeAtIndex(1)

    self.assertEqual(expected, list.returnLinkedList())
    self.assertEqual(3, list.getLen())
    self.assertEqual(expected_reverse, list.returnLinkedListReverse())
    self.assertEqual(expected_item, removed_item)

  def test_remove_at_index_second_to_last_item(self):
    val = 5
    val2 = 10
    val3 = 20
    val4 = 30

    expected = f"{val} {val2} {val4} "
    expected_reverse = f"{val4} {val2} {val} "
    expected_item = val3

    list = LinkedList()
    list.insertHead(val)
    list.insertTail(val2)
    list.insertTail(val3)
    list.insertTail(val4)

    removed_item = list.removeAtIndex(2)

    self.assertEqual(expected, list.returnLinkedList())
    self.assertEqual(3, list.getLen())
    self.assertEqual(expected_reverse, list.returnLinkedListReverse())
    self.assertEqual(expected_item, removed_item)

  def test_remove_at_index_multiple_removals(self):
    val = 5
    val2 = 10
    val3 = 20
    val4 = 30

    expected = f"{val} {val4} "
    expected_reverse = f"{val4} {val} "

    list = LinkedList()
    list.insertHead(val)
    list.insertTail(val2)
    list.insertTail(val3)
    list.insertTail(val4)

    removed_item1 = list.removeAtIndex(1)
    removed_item2 = list.removeAtIndex(1)

    self.assertEqual(expected, list.returnLinkedList())
    self.assertEqual(2, list.getLen())
    self.assertEqual(expected_reverse, list.returnLinkedListReverse())
    self.assertEqual(val2, removed_item1)
    self.assertEqual(val3, removed_item2)

  def test_remove_at_index_after_insert_at_index(self):
    val = 5
    val2 = 10
    val3 = 20
    val4 = 30

    expected = f"{val} {val2} {val3} "
    expected_reverse = f"{val3} {val2} {val} "
    expected_item = val4

    list = LinkedList()
    list.insertHead(val)
    list.insertTail(val2)
    list.insertTail(val4)
    list.insertAtIndex(val3, 2)
    removed_item = list.removeAtIndex(2)

    self.assertEqual(expected, list.returnLinkedList())
    self.assertEqual(3, list.getLen())
    self.assertEqual(expected_reverse, list.returnLinkedListReverse())
    self.assertEqual(expected_item, removed_item)

  def test_remove_at_index_empty_list(self):
    expected = ""
    expected_reverse = ""

    list = LinkedList()

    result = list.removeAtIndex(0)

    self.assertEqual(expected, list.returnLinkedList())
    self.assertEqual(0, list.getLen())
    self.assertEqual(expected_reverse, list.returnLinkedListReverse())
    self.assertTrue(isinstance(result, Exception))

  def test_remove_at_index_negative_index(self):
    val = 5
    val2 = 10

    expected = f"{val} {val2} "
    expected_reverse = f"{val2} {val} "

    list = LinkedList()
    list.insertHead(val)
    list.insertTail(val2)

    result = list.removeAtIndex(-1)

    self.assertEqual(expected, list.returnLinkedList())
    self.assertEqual(2, list.getLen())
    self.assertEqual(expected_reverse, list.returnLinkedListReverse())
    self.assertTrue(isinstance(result, Exception))

  def test_remove_at_index_out_of_bounds(self):
    val = 5
    val2 = 10

    expected = f"{val} {val2} "
    expected_reverse = f"{val2} {val} "

    list = LinkedList()
    list.insertHead(val)
    list.insertTail(val2)

    result = list.removeAtIndex(2)

    self.assertEqual(expected, list.returnLinkedList())
    self.assertEqual(2, list.getLen())
    self.assertEqual(expected_reverse, list.returnLinkedListReverse())
    self.assertTrue(isinstance(result, Exception))