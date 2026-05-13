import unittest

from linked_list import *


class TestLinkedList(unittest.TestCase):
  def test_insert_head(self):
    val  = 5
    expected = f"{val} "
    list = linkedList()
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
    list = linkedList()
    list.insertHead(val)
    list.insertHead(val2)
    list.insertHead(val3)
    self.assertEqual(expected, list.returnLinkedList())
    self.assertEqual(3, list.len)
    self.assertEqual(expected_reverse, list.returnLinkedListReverse())



  def test_insert_tail(self):
    val  = 5
    expected = f"{val} "
    list = linkedList()
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

    list = linkedList()
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
    list = linkedList()
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

    list = linkedList()
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

    list = linkedList()
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

    list = linkedList()
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

    list = linkedList()
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

    list = linkedList()
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

    list = linkedList()
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

    list = linkedList()
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

    list = linkedList()
    list.insertHead(val)
    list.insertTail(val2)
    list.insertTail(val3)
    list.insertTail(val4)
    list.insertAtIndex(val5, 1)

    self.assertEqual(expected, list.returnLinkedList())
    self.assertEqual(5, list.len)
    self.assertEqual(expected_reverse, list.returnLinkedListReverse())