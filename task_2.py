class Solution(object):
    def addTwoNumbers(l1, l2):
        total = 0
        for i in range(len(l1)):
            total += l1[i]*10**(i)
        for i in range(len(l2)):
            total += l2[i]*10**(i)
        return list(str(total))

print(Solution.addTwoNumbers([2,4,3], [5,6,4]))
