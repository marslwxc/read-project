
### 树
- 树的每一个元素叫做 节点；用来连线相邻节点之间的关系，叫做 父子关系
![树的结构](https://static001.geekbang.org/resource/image/22/ae/220043e683ea33b9912425ef759556ae.jpg)
- 如上图，A节点就是B节点的**父节点**，B节点是A节点的**子节点**。B,C,D这三个节点的父节点是同一个节点，所以它们之间互称为**兄弟节点**，没有父节点的节点叫做**根节点**，没有子节点的节点叫做**叶子节点**或者**叶节点**。
![树的概念](https://static001.geekbang.org/resource/image/40/1e/4094a733986073fedb6b9d03f877d71e.jpg)
![高度、深度和层数](https://static001.geekbang.org/resource/image/50/b4/50f89510ad1f7570791dd12f4e9adeb4.jpg)

### 二叉树 Binary Tree
- 二叉树，每个节点最多有两个分叉，也就是两个节点，分别是**左子节点**和**右子节点**。
- 在一个二叉树中，叶子节点全都在最底层，除了叶子节点之外，每个节点都有左右两个子节点，这种二叉树就叫做**满二叉树**
- 在一个二叉树中，叶子节点都在最底下两层，最后一层的叶子节点都靠左排列，并且除了最后一层，其他层的节点个数都要达到最大，这种二叉树叫做**完全二叉树**。
- 存储二叉树的方法
    1. **链式存储法**：每个节点有三个字段，其中一个存储数据，另外两个是指向左右子节点的指针。
    ![链式存储法](https://static001.geekbang.org/resource/image/12/8e/12cd11b2432ed7c4dfc9a2053cb70b8e.jpg)
    2. **顺序存储法**：把根节点存储在下标i的位置，那左子节点存储在下标i*2的位置，右子节点存储在i*2+1的位置，父节点就是i/2的位置
        - 顺序存储法存储完全二叉树比较节省数组存储空间，如果存储非完全二叉树比较浪费存储空间
    ![顺序存储法](https://static001.geekbang.org/resource/image/14/30/14eaa820cb89a17a7303e8847a412330.jpg)
    ![顺序存储法存储非完全二叉树](https://static001.geekbang.org/resource/image/08/23/08bd43991561ceeb76679fbb77071223.jpg)
    - 二叉树的遍历：分为三种，**前序遍历、后序遍历和中序遍历**
        - 前序遍历：对于书中的任意节点来说，先打印这个节点，然后再打印它的左子树，最后打印它的右子树
        - 中序遍历：对于树中的任意节点来说，先打印它的左子树，然后再打印它本身，最后打印它的右子树
        - 后序遍历：对于书中的任意节点来说，先打印它的左子树，然后再打印它的右子树，最后打印节点本身
        ![前、中、后序遍历](https://static001.geekbang.org/resource/image/ab/16/ab103822e75b5b15c615b68560cb2416.jpg)


```python
from typing import TypeVar, Generic, Generator, Optional

T = TypeVar("T")

class TreeNode(Generic[T]):
    def __init__(self, value: T):
        self.val = value
        self.left = None
        self.right = None
```


```python
def pre_order(root: Optional[TreeNode[T]]) -> Generator[T, None, None]:
    if root:
        yield root.val
        yield from pre_order(root.left)
        yield from pre_order(root.right)
```


```python
def in_order(root: Optional[TreeNode[T]]) -> Generator[T, None, None]:
    if root:
        yield from in_order(root.left)
        yield root.val
        yield from in_order(root.right)
```


```python
def post_order(root: Optional[TreeNode[T]]) -> Generator[T, None, None]:
    if root:
        yield from post_order(root.left)
        yield from post_order(root.right)
        yield root.val
```


```python
    singer = TreeNode("Taylor Swift")

    genre_country = TreeNode("Country")
    genre_pop = TreeNode("Pop")

    album_fearless = TreeNode("Fearless")
    album_red = TreeNode("Red")
    album_1989 = TreeNode("1989")
    album_reputation = TreeNode("Reputation")

    song_ls = TreeNode("Love Story")
    song_wh = TreeNode("White Horse")
    song_wanegbt = TreeNode("We Are Never Ever Getting Back Together")
    song_ikywt = TreeNode("I Knew You Were Trouble")
    song_sio = TreeNode("Shake It Off")
    song_bb = TreeNode("Bad Blood")
    song_lwymmd = TreeNode("Look What You Made Me Do")
    song_g = TreeNode("Gorgeous")

    singer.left, singer.right = genre_country, genre_pop
    genre_country.left, genre_country.right = album_fearless, album_red
    genre_pop.left, genre_pop.right = album_1989, album_reputation
    album_fearless.left, album_fearless.right = song_ls, song_wh
    album_red.left, album_red.right = song_wanegbt, song_ikywt
    album_1989.left, album_1989.right = song_sio, song_bb
    album_reputation.left, album_reputation.right = song_lwymmd, song_g

    print(list(pre_order(singer)))
    print(list(in_order(singer)))
    print(list(post_order(singer)))
```

    ['Taylor Swift', 'Country', 'Fearless', 'Love Story', 'White Horse', 'Red', 'We Are Never Ever Getting Back Together', 'I Knew You Were Trouble', 'Pop', '1989', 'Shake It Off', 'Bad Blood', 'Reputation', 'Look What You Made Me Do', 'Gorgeous']
    ['Love Story', 'Fearless', 'White Horse', 'Country', 'We Are Never Ever Getting Back Together', 'Red', 'I Knew You Were Trouble', 'Taylor Swift', 'Shake It Off', '1989', 'Bad Blood', 'Pop', 'Look What You Made Me Do', 'Reputation', 'Gorgeous']
    ['Love Story', 'White Horse', 'Fearless', 'We Are Never Ever Getting Back Together', 'I Knew You Were Trouble', 'Red', 'Country', 'Shake It Off', 'Bad Blood', '1989', 'Look What You Made Me Do', 'Gorgeous', 'Reputation', 'Pop', 'Taylor Swift']
    

### 二叉查找树 Binary Search Tree
**二叉查找树要求，在树中的任意一个节点，其左子树中的每一个节点的值，都要小于这个节点的值，而右子树的值都要大于这个节点的值**
- 二叉查找树最大的特点就是支持动态数据集合的快速插入、删除、查找操作。
- 二叉查找树的查找操作
    - 先取根节点，如果它等于要找到值就返回；如果要找的数据比根节点小，那就在左子树中递归查找；如果要找到数据比根节点大，那就再右子树中递归查找
    ![二叉查找树查找操作](https://static001.geekbang.org/resource/image/96/2a/96b3d86ed9b7c4f399e8357ceed0db2a.jpg)
- 二叉查找树的插入操作
    - 二叉查找树的插入操作过程类似于查找操作。新插入的数据一般都在叶子节点上，所以只需要从根节点开始，依次比较要插入的数据和节点的大小关系。如果要插入的数据比节点的数据大，并且节点的右子树为空，就将新数据直接插到右子节点的位置；如果不为空，就再递归遍历右子树，查找插入位置。同理，如果要插入的数据比节点数值小，并且节点的左子树为空，就将新数据插入到左子节点的位置；如果不为空，就再遍历左子树，查找插入位置。
    ![二叉查找树插入操作](https://static001.geekbang.org/resource/image/da/c5/daa9fb557726ee6183c5b80222cfc5c5.jpg)
- 二叉查找树的删除操作
    - 如果要删除的节点没有子节点，只需要直接将父节点中，指向要删除节点的指针置为null
    - 如果要删除的节点只有一个子节点，只需要更新父节点中，指向要删除节点的指针，让它指向要删除节点的子节点就可以了。
    - 如果要删除的节点有两个子节点，那么就需要找到右子树中的最小节点，把它替换到要删除的节点上。然后再删除掉这个最小节点。
    ![二叉查找树删除操作](https://static001.geekbang.org/resource/image/29/2c/299c615bc2e00dc32225f4d9e3490e2c.jpg)


```python
from typing import Optional

class TreeNode:
    def __init__(self, value: int):
        self.val = value
        self.left = None
        self.right = None
```


```python
class BinarySearchTree:
    def __init__(self):
        self._root = None
        
    def find(self, value: int) -> Optional[TreeNode]:
        node = self._root
        while node and node.val != value:
            node = node.left if node.val > value else node == node.right
        return node
    
    def insert(self, value: int):
        if not self._root:
            self._root = TreeNode(value)
            return
        parent = None
        node = self._root
        while node:
            parent = node
            node = node.left if node.val > value else node.val < value
        newnode = TreeNode(value)
        if parent.val > newnode:
            parent.left = newnode
        else:
            parent.right = newnode
        
    def delete(self, value: int):
        node = self._root
        parent = None
        while node and node.val != value:
            parent = node
            node = node.left if node.val > value else node.right
        if not node: return
        
        # 要删除的节点有两个子节点
        if node.left and node.right:
            newnode = node.right
            newparent = node
            while newnode.left:
                newparent = newnode
                newnode = newnode.left
            node.val = newnode.val
            if newnode.right:
                newparent.left = newnode.right
                
        # 删除节点是叶子节点或者仅有一个子节点
        child = node.left if node.left else node.right
        if not parent:
            self._root = chilf
        elif parent.left == node:
            parent.left = child
        else:
            parent.right = child
```

#### 支持重复数据的二叉查找树
1. 二叉查找树中每一个节点不仅会存储一个数据，因此通过链表和支持动态扩容的数组等数据结构，把值相同的数据都存储在同一个节点上
![插入相同数据](https://static001.geekbang.org/resource/image/3f/5f/3f59a40e3d927f567022918d89590a5f.jpg)
2. 把相同给值当作大于这个数值的值来处理，放到右子树当中
    1. 当要查找数据的时候，遇到值相同的节点，并不会停止查找操作，而是继续在右子树中查找，直到遇到叶子节点才停止
    ![查找存储了相同数据的二叉树](https://static001.geekbang.org/resource/image/fb/ff/fb7b320efd59a05469d6d6fcf0c98eff.jpg)
    2. 对于删除操作，也需要先查找到每个要删除的节点，然后再按前面删除操作的方法，依次删除
    ![删除存储了相同数据的二叉树](https://static001.geekbang.org/resource/image/25/17/254a4800703d31612c0af63870260517.jpg)

**平衡二叉树的高度接近logn，所以插入、删除、查找操作的时间复杂度也比较稳定，是O(logn)**
