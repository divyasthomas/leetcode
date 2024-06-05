import logging
from typing import Optional
class ListNode:
    def __init__(self,val =0, next= None) -> None:
        self.val  = val
        self.next =next

class Solution:
    def ReverseList(self, head: Optional[ListNode]) ->Optional[ListNode]:
        prev_node =None
        cur_node = head

        while cur_node:
            temp = cur_node.next
            cur_node.next =prev_node
            prev_node = cur_node
            cur_node = temp
       
        head = prev_node
        return head

def makeLinkedList(userlist: list[int]) -> ListNode:
    if not userlist: return None
    head = ListNode(userlist[0])
    cur_node = head
    for ele in userlist[1:]:
        cur_node.next = ListNode(ele)
        cur_node = cur_node.next
    return head

def printLinkedList(head:ListNode):
    print('Printing Linked List')
    cur_node = head
    while cur_node:
        print(f'{cur_node.val} ->', end=" ")
        cur_node = cur_node.next
    print('\n.')        

def main():
    while True:
        try:
             user_input = input('Enter list of integers separated by comma:')
             user_list = [ int(each.strip()) for each in user_input.split(',')]
             break
        except ValueError as v:
            logging.error('You must enter integers only. Bad Input. Try again!')
        except Exception as e:
            logging.error('I am momo! Try again!')
        
    print(f'cur list is {user_list} ')
    my_head = makeLinkedList(user_list)
    printLinkedList(my_head)

    solution = Solution()
    reverse_head = solution.ReverseList(my_head)
    printLinkedList(reverse_head)

        


        


if __name__=="__main__":
    main()