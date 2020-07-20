class ListNode:
  def __init__(self, data=0, next=None):
    self.data = data
    self.next = next

  def search_in_list(self, key):
    while self and self.data != key:
        self = self.next
    return self
​
​
  def iterate(self):
    print(self.data)
    if self.next:
      self.next.iterate()
    else:
      print()
​
  def insert_after(self, new_node):
    new_node.next = self.next
    self.next = new_node
​
  def delete_after(self):
    deleted_node = self.next
    self.next = self.next.next
    deleted_node.next = None
​
​
if __name__ == "__main__":
  head = ListNode("I am the head")
  second = ListNode("I am second")
  third = ListNode("I am third")
  fourth = ListNode("I am fourth")
  fifth = ListNode("I am fifth")
  head.insert_after(second)
  second.insert_after(third)
  # head.iterate()
  third.insert_after(fourth)
  # head.iterate()
  head.delete_after()
  # head.iterate()
  # print("Search in list after")
  # print(head.search_in_list("I am second"))