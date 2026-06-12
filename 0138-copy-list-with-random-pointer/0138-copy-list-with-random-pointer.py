"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldtoCopy={None:None}
        cur=head
        while cur:
            copy=Node(cur.val)
            oldtoCopy[cur]=copy
            cur=cur.next
        cur=head
        while cur:
            copy=oldtoCopy[cur]
            copy.next=oldtoCopy[cur.next]
            copy.random=oldtoCopy[cur.random]
            cur=cur.next
        return oldtoCopy[head]
        