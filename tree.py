class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))


def diameter(root):
    if root is None:
        return 0

    lheight = height(root.left)
    rheight = height(root.right)

    ldiameter = diameter(root.left)
    rdiameter = diameter(root.right)
    # print((lheight, rheight))

    return max(lheight + rheight + 1, max(ldiameter, rdiameter))


def catalan(n):
    # Base Case
    if n <= 1:
        return 1

    # Catalan(n) is the sum
    # of catalan(i)*catalan(n-i-1)
    res = 0
    for i in range(n):
        res += catalan(i) * catalan(n - i - 1)

    return res


def binomialCoefficient(n, k):
    # since C(n, k) = C(n, n - k)
    if k > n - k:
        k = n - k
    # initialize result
    res = 1
    for i in range(k):
        res = res * (n - i)
        res = res // (i + 1)
    return res


# Driver program to test above function
n = 8
k = 2
res = binomialCoefficient(n, k)
# print("Value of C(% d, % d) is % d" %(n, k, res))

root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.right.left = Node(19)
root.right.left.left = Node(99)
root.right.left.left.left = Node(3)
root.right.left.left.left.left = Node(0)

root.right.right = Node(12)
root.right.right.right = Node(10)
root.right.right.right.right = Node(32)

# print(height(root))
# print(diameter(root))
# print(catalan(3))


################################### Binary tree array represetion.
# if range is from 1 - n
#   left -> 2(parent+1)-2
#   right -> 2(parent+1)
# if range is from 0 - n-1
#   left -> 2(parent+1) -1
#   right -> 2(parent+1)
