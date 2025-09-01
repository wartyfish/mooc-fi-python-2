# WRITE YOUR SOLUTION HERE:
class Node:
    """ Class is modeling single node in binary tree """
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

def greatest_node(root: Node):
    greatest = root.value
    print(greatest)

    # program goes all the way down the left-most branch
    # left-most node return it's value to its parent node
    # the parent node compares its value to returned value
    # and reassigns its value if the returned one is greater
    # the parent node then repeats process with its right node
    # and again compares its value with the returned one
    # parent node returns the greatest value up the stack
    # etc. 
    if root.left_child is not None:
        l_greatest = greatest_node(root.left_child)
        if greatest < l_greatest:
            greatest = l_greatest

    if root.right_child is not None:
        r_greatest = greatest_node(root.right_child)
        if greatest < r_greatest:
            greatest = r_greatest

    return greatest

if __name__ == "__main__":
    tree = Node(2)

    tree.left_child = Node(3)
    tree.left_child.left_child = Node(5)
    tree.left_child.right_child = Node(8)

    tree.right_child = Node(4)
    tree.right_child.left_child = Node(12)
    tree.right_child.right_child = Node(11)

    print(greatest_node(tree))