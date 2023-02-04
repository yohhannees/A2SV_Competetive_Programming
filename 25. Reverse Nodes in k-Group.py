class Solution:
  def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head:
      return None

    tail = head

    for _ in range(k):
      if not tail:  
        return head
      tail = tail.next

    newHead = self._reverse(head, tail)
    head.next = self.reverseKGroup(tail, k)
    return newHead

  def _reverse(self, head: Optional[ListNode], tail: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head

    while curr != tail:
      next = curr.next
      curr.next = prev
      prev = curr
      curr = next

    return prev
