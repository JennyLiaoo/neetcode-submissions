# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        input: head of LL, int k
        output: the resulting LL after
        - reversing each group of k nodes
        Q: is k positive?
        Q: what to do if remaining number of node < k
        Q; time constraint? O(n) solution

        go k nodes forward if possible to get the end of the nodes to reverse. reverse that group of nodes up to that point. then continue
        - move forward k edges to node n, keep track of next node, and point first node to n. then reverse the rest
        Recursion? (pass in head of LL we want to continue reversing) returns the reversed version
        We set next value of current group -> head of reversed LL
        Q: K = 0?
        '''

        # take in head of LL we want to reverse
        # return the possibly reversed LL (<K, no changes)
        def reverse_rest(node):
        
            if node == None:
                return None
            if k == 1:
                return node
            head_of_group = node
            tail_of_group = node
            i = 1
            while tail_of_group.next != None and i < k:
                tail_of_group = tail_of_group.next
                i+=1
            if i == k:
                # reached k nodes, can reverse
                # 1. reverse the k nodes
                # 2. set the last node.next (first node of this group's next) = reverse_rest(rest. of LL)
                if k == 2:
                    next_head = tail_of_group.next
                    tail_of_group.next = head_of_group
                    head_of_group.next = reverse_rest(next_head)
                    return tail_of_group

                prev_node = head_of_group
                current_node = prev_node.next
                next_node = current_node.next
                next_head = tail_of_group.next
                while current_node != next_head:
                    current_node.next = prev_node
                    prev_node = current_node
                    current_node = next_node
                    if next_node != None:
                        next_node = next_node.next
                head_of_group.next = reverse_rest(next_head)
                return tail_of_group

            else:
                # group is short, return the current list of nodes
                return head_of_group
        return reverse_rest(head)





        


        