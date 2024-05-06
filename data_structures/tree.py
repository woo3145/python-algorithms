class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    """중위 순회"""
    result = []
    if root:
        result.extend(inorder_traversal(root.left))
        result.append(root.val)
        result.extend(inorder_traversal(root.right))
    return result

def preorder_traversal(root):
    """전위 순회"""
    result = []
    if root:
        result.append(root.val)
        result.extend(preorder_traversal(root.left))
        result.extend(preorder_traversal(root.right))
    return result

def postorder_traversal(root):
    """후위 순회"""
    result = []
    if root:
        result.extend(postorder_traversal(root.left))
        result.extend(postorder_traversal(root.right))
        result.append(root.val)
    return result

def array_to_tree(arr, index):
    """배열을 이용하여 트리 생성"""
    if index < len(arr):
        if arr[index] is None:
            return None
        root = TreeNode(arr[index])
        root.left = array_to_tree(arr, 2 * index + 1)
        root.right = array_to_tree(arr, 2 * index + 2)
        return root
    return None

# 트리 생성을 위한 배열
tree_array = [1, 2, 3, 4, 5, None, None]

# 배열로부터 트리 생성
tree_root = array_to_tree(tree_array, 0)

# 트리 순회 예시
inorder_result = inorder_traversal(tree_root)  # [4, 2, 5, 1, 3]
preorder_result = preorder_traversal(tree_root)  # [1, 2, 4, 5, 3]
postorder_result = postorder_traversal(tree_root)  # [4, 5, 2, 3, 1]

print(inorder_result)
print(preorder_result)
print(postorder_result)
