
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        """

        re = ListNode(0)
        r = re
        carry = 0
        while(l1 or l2):

            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            s = x + y + carry
            carry = s//10
            r.next = ListNode(s % 10)
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

            r = r.next
        if carry > 0:
            r.next = ListNode(1)

        return re.next


if __name__ =="__main__":
    #
    # a = ListNode(2)
    # a.next = ListNode(4)
    # a.next.next = ListNode(3)
    #
    #
    # b = ListNode(5)
    # b.next = ListNode(6)
    # b.next.next = ListNode(4)
    #
    # s = Solution()
    # c = s.addTwoNumbers(a, b)
    #
    # print(c.val, c.next.val, c.next.next.val)



    a = ListNode(1)
    a.next = ListNode(8)

    b = ListNode(0)

    s = Solution()
    c = s.addTwoNumbers(a, b)

    print(c.val, c.next.val)
    print("zhangyunhong")

