#Code from https://www.w3schools.com/dsa/dsa_data_binarytrees.php
#Useful videos to undertand tree data structures:
#https://www.youtube.com/watch?v=1-l_UOFi1Xw&t=13s
#https://www.youtube.com/watch?v=EPwWrs8OtfI 

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

from collections import deque

def bfs_traverse(root):
    if root is None:
        return

    result = []
    queue = deque([root])

    while(queue):
        q_length = len(queue)
        level = []

        for _ in range(q_length):
            node = queue.popleft()
            level.append(node.data)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)

bfs_traverse(root)
