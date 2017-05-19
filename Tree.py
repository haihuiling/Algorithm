# coding=utf-8


class TreeNode():

    def __init__(self, data=-1, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Tree():

    def __init__(self):
        self.root = TreeNode()
        self.myQueue = []
    """为树添加节点"""

    def add(self, item):
        node = TreeNode(item)
        # 如果树的根结点是-1，说明是根结点，对根结点进行赋值
        if self.root.data == -1:
            self.root = node
            self.myQueue.append(node)
        else:
            treeNode = self.myQueue[0]
            if treeNode.left == None:
                treeNode.left = node
                self.myQueue.append(node)
            elif treeNode.right == None:
                treeNode.right = node
                self.myQueue.append(node)
                self.myQueue.pop(0)  # 左右节点都已经满足了，pop第一个

    """利用递归实现树的先序遍历"""

    def front_digui(self, root):
        if root == None:
            return
        print(root.data)
        self.front_digui(root.left)
        self.front_digui(root.right)

    """利用递归实现树的中序遍历"""

    def middle_digui(self, root):
        if root == None:
            return
        self.middle_digui(root.left)
        print(root.data)
        self.middle_digui(root.right)

    """利用递归实现树的后序遍历"""

    def later_digui(self, root):
        if root == None:
            return
        self.later_digui(root.left)
        self.later_digui(root.right)
        print(root.data)

    """利用栈实现树的先序遍历"""

    def front_stack(self):
        root = self.root
        # 先一直遍历左边的树，如果为空 弹出最后一个值 遍历右边的值
        my_stack = []
        node = root
        while node or my_stack:
            while node:
                print(node.data)
                my_stack.append(node)
                node = node.left
            node = my_stack.pop()
            node = node.right

    """利用栈实现树的中序遍历"""

    def middle_stack(self):
        root = self.root
        # 先将左边的树压入栈中，然后依次弹出，遍历右边的值
        my_stack = []
        node = root
        while node or my_stack:
            while node:
                my_stack.append(node)
                node = node.left
            node = my_stack.pop()
            print(node.data)
            node = node.right

    """利用栈实现树的后序遍历"""

    def later_stack(self):
        root = self.root
        my_stack1 = []
        my_stack2 = []
        node = root
        my_stack1.append(node)
        while my_stack1:
            node = my_stack1.pop()
            if node.left:
                my_stack1.append(node.left)
            if node.right:
                my_stack1.append(node.right)
            my_stack2.append(node)
        while my_stack2:
            print(my_stack2.pop().data)
    """利用队列实现树的层次遍历"""

    def level_queue(self):
        root = self.root
        my_queue = []
        node = root
        my_queue.append(node)
        while my_queue:
            node = my_queue.pop(0)
            print(node.data)
            if node.left != None:
                my_queue.append(node.left)
            if node.right != None:
                my_queue.append(node.right)

if __name__=="__main__":
    tree = Tree()
    for i in range(1,6):
        tree.add(i)
    print('-------front_digui-------')
    tree.front_digui(tree.root)#1245367
    print('-------middle_digui-------')
    tree.middle_digui(tree.root)#4251637
    print('-------later_digui-------')
    tree.later_digui(tree.root)#4526731
    print('-------front_stack-------')
    tree.front_stack()
    print('-------middle_stack-------')
    tree.middle_stack()
    print('-------later_stack-------')
    tree.later_stack()
    print('-------level_queue-------')
    tree.level_queue()
