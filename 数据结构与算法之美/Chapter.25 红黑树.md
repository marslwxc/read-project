
### 平衡二叉查找树
平衡二叉查找树：二叉树中任意一个节点的左右子树的高度相差不能大于1.
![平衡二叉树](https://static001.geekbang.org/resource/image/dd/9b/dd9f5a4525f5029a8339c89ad1c8159b.jpg)
**平衡二叉树中“平衡”的意思，其实就是让整棵树左右看起来比较对称、比较“平衡”，不要出现左子树很高、右子树很矮的情况。这样就让整棵树的高度相对来说低一些，相应的插入、删除、查找等操作的效率高一些。**

### 红黑树
红黑树：Red-Black Tree，简称R-B Tree。是一种不严格的平衡二叉查找树。红黑树中的节点，一类被标记为黑色，一类被标记为红色。除此之外，一棵红黑树还需要满足以下要求：
- 根节点是黑色的
- 每个叶子节点都是黑色的空节点(NIL)，也就是说，叶子节点不存储数据
- 任何相邻的节点都不能同时为红色，也就是说，红色节点是被黑色节点隔开的
- 每个节点，从该节点到达其可达叶子节点的所有路径，都包含相同数目的黑色节点
![红黑树](https://static001.geekbang.org/resource/image/90/9a/903ee0dcb62bce2f5b47819541f9069a.jpg)
红黑树的高度近似2log2n

左旋 rotate left 全称围绕某个节点的左旋

右旋 rotate right 全称围绕某个节点的右旋
![左旋和右旋](https://static001.geekbang.org/resource/image/0e/1e/0e37e597737012593a93105ebbf4591e.jpg)

#### 插入操作的平衡调整
**红黑树规定，插入节点必须是红色的。而且，二叉查找树中新插入的节点都是放在叶子节点上。**
- 如果插入的节点的父节点是黑色的，那么我们就什么都不做，它仍然满足红黑树的定义。
- 如果插入的节点是根节点，那就直接改变它的颜色，把它变成黑色就可以了
除此之外，其他情况都会违背红黑树的定义，于是我们就需要进行调整，调整的过程包含两种基础操作：左右旋转和改变颜色。红黑树的平衡调整过程是一个迭代的过程。我们**把正在处理的节点叫做关注节点**。关注节点会随着不停地迭代处理而不断发生变化。最开始的关注节点就是新插入的节点。
- Case1：如果关注节点是a，它的叔叔节点d是红色，我们就一次执行下面的操作：
    1. 将关注节点a的父亲节点b、叔叔节点d的颜色都设置成黑色
    2. 将关注节点a的祖父节点c的颜色设置成红色
    3. 关注节点变成a的祖父节点c
    4. 跳到Case2或者Case3
    ![新增Case1](https://static001.geekbang.org/resource/image/60/40/603cf91f54b5db21bd02c6c5678ecf40.jpg)
- Case2：如果关注节点是a，它的叔叔节点d是黑色，关注节点a是其父节点b的右子节点：
    1. 关注节点变成节点a的父节点b
    2. 围绕新的关注节点b左旋
    3. 跳到Case3
    ![新增Case2](https://static001.geekbang.org/resource/image/44/ad/4480a314f9d83c343b8adbb28b6782ad.jpg)
- Case3：如果关注节点是a，它的叔叔节点d是黑色的，关注节点a是其父节点b的左子节点：
    1. 围绕关注节点a的祖父节点c右旋
    2. 将关注节点a的夫节点b、兄弟节点c的颜色互换
    3. 调整结束
    ![新增Case3](https://static001.geekbang.org/resource/image/04/12/04650d9470b1e67899f5b8b7b8e33212.jpg)

#### 删除操作的平衡调整
删除操作的平衡调整分为两步，**第一步是针对删除节点初步调整**。初步调整只是保证整棵红黑树在一个节点删除后，仍然满足最后一条定义的要求，即每个节点，从该节点到达叶子节点的所有路径都包含相同数目的黑色节点。**第二步是针对关注点进行二次调整**，让它满足红黑树的第三条定义，即不存在相邻的两个红色节点
##### 针对删除节点初步调整
红黑树的定义中，“只包含红色节点和黑色节点”，经过初步调整之后，为了满足红黑树定义的最后一条要求，有些节点会被标记成两种颜色，“红-黑”或者“黑-黑”。**如果一个节点被标记成了“黑-黑”，那在计算黑色节点个数的时候，要算成两个黑色黑色节点**。**初步调整只是保证整棵红黑树在一个节点删除后，仍然满足最后一条定义的要求，即每个节点，从该节点到达叶子节点的所有路径都包含相同数目的黑色节点**。
- Case1：如果要删除的节点是a，它只有一个子节点b：
    1. 删除节点a，并且把节点b替换到节点a的位置，这一部分操作和普通的二叉查找树的删除操作一样
    2. 节点b只能是红色，所以节点a只能是黑色，其他情况均不符合红黑树的定义。这种情况下，把节点b改为黑色
    3. 调整结束，不需要进行二次调整
    ![删除1Case1](https://static001.geekbang.org/resource/image/a6/c3/a6c4c347b7cbdf57662bab399ed36cc3.jpg)
- Case2：如果要删除的节点a有两个非空子节点，并且它的后继节点就是节点a的右子节点c。
    1. 如果节点a的后继节点就是右子节点c，那右子节点c肯定没有左子树。我们把节点a删除，并且将节点c替换到节点a的位置。这一部分操作和普通的二叉查找树的删除操作无异
    2. 然后把节点c的颜色设置成跟节点a相同的颜色
    3. 如果节点c是黑色，为了不违反红黑树的最后一条定义，我们给予节点c的右子树d多加一个黑色，这个时候节点d就成了“红-黑”或者“黑-黑”。
    4. 关注点变成节点d，第二步的调整操作针对新关注点来做
    ![删除1Case2](https://static001.geekbang.org/resource/image/48/4e/48e3bd2cdd66cb635f8a4df8fb8fd64e.jpg)
- Case3：如果要删除的是节点a，它有两个非空子节点，并且节点a的后继节点不是右子节点：
    1. 找到后继节点d，并将它删除，删除后继节点d的过程参照Case1
    2. 将节点a替换成后继节点d
    3. 把节点d的颜色设置成跟节点a相同的颜色
    4. 如果节点d是黑色，为了不违反红黑树的最后一条定义，给节点d的右子节点c多加一个黑色，这个时候节点c就成了“红-黑”或者“黑-黑”
    5. 关注点变成节点c，第二步的调整操作针对新关注点来做
    ![删除1Case3](https://static001.geekbang.org/resource/image/b9/29/b93c1fa4de16aee5482424ddf49f3c29.jpg)
##### 针对关注节点进行二次调整
经过初步调整后，关注节点变成了“红-黑”或者“黑-黑”节点。针对这个关注点，再分四种情况来进行二次调整。**二次调整是为了让红黑树中不存在相邻的红色节点**
- Case1：如果关注节点是a，它的兄弟节点c是红色的：
    1. 围绕关注节点a的父节点b左旋
    2. 关注节点a的父节点b和祖父节点c交换颜色
    3. 关注节点不变
    4. 继续从四种情况中选择合适的规则来调整
    ![删除2Case1](https://static001.geekbang.org/resource/image/ac/91/ac76d78c064a2486e2a5b4c4903acb91.jpg)
- Case2：如果关注节点是a，它的兄弟节点c是黑色的，并且节点c的左右子节点d、e都是黑色的
    1. 将关注节点a的兄弟节点c的颜色变成红色
    2. 从关注节点a中去掉一个黑色，这个时候节点a就是单纯的红色或者黑色
    3. 给关注节点a的父节点b添加一个黑色
    4. 关注节点从a变成其父节点b
    5. 继续从四种情况中选择符合的规则来调整
    ![删除2Case2](https://static001.geekbang.org/resource/image/ec/ec/eca118d673c607eb2b103f3476fb24ec.jpg)
- Case3：如果关注节点是a，它的兄弟节点c是黑色，c的左子节点d是红色，c的右子节点e是黑色
    1. 围绕关注节点a的兄弟节点c右旋
    2. 节点c和节点d交换颜色
    3. 关注节点不变
    4. 跳转Case4，继续调整
    ![删除2Case3](https://static001.geekbang.org/resource/image/44/af/44075213100edd70315e1492422c92af.jpg)
- Case4：如果关注节点a的兄弟节点c是黑色的，并且c的右子节点是红色的
    1. 围绕关注节点a的父节点b左旋
    2. 将关注节点a的兄弟节点c的颜色跟关注节点a的父节点b设置成相同的颜色
    3. 将关注节点a的父节点b的颜色设置成黑色
    4. 从关注节点a中去掉一个黑色
    5. 将关注节点a的叔叔节点e设置成黑色
    6. 调整结束
    ![删除2Case4](https://static001.geekbang.org/resource/image/5f/44/5f73f61bf77a7f2bb75f168cf432ec44.jpg)


```python
from queue import Queue
import pygraphviz as pgv
import random


class TreeNode:
    def __init__(self, value=None, color=None):
        self.val = value
        assert color in ['r', 'b']
        self.color = 'red' if color == 'r' else 'black'
        
        self.left = None
        self.right = None
        self.parent = None
        
    def is_black(self):
        return self.color == 'black'
    
    def set_black(self):
        self.color = 'black'
        return
    
    def set_red(self):
        self.color = 'red'
        
        
class RedBlackTree:
    def __init__(self, val_list=None):
        self.root = None
        self.black_leaf = TreeNode(color='b') # 共用的黑色叶子节点
        
        # 可用数组初始化
        if type(val_list) is list:
            for n in val_list:
                assert type(n) is int
                self.insert(n)
                
    def search(self, val):
        if self.root is None:
            return None
        
        n = self.root
        while n != self.black_leaf:
            if val < n.val:
                n = n.left
            elif val > n.val:
                n = n.right
            else:
                return n
        return None
    
    def insert(self, val):
        assert type(val) is int
        
        new_node = TreeNode(val, 'r') # 新插入的节点为红色
        
        # 根节点
        if self.root is None:
            self.root = new_node
        else:
            n = self.root
            while n != self.black_leaf:
                p = n
                if val < n.val:
                    n = n.left
                elif val > n.val:
                    n = n.right
                else:
                    raise KeyError('val:{} already exists') # 该值已存在，插入失败
            
            if val < p.val:
                p.left = new_node
            else:
                p.right = new_node
            new_node.parent = p
            
            new_node.left = new_node.right = self.black_leaf
            self._insert_fixup(new_node)
            
    def _insert_fixup(self, node):
        n = node
        while n is not self.root and not n.parent.is_black():
            # 父p 叔u 祖父g
            p = self.parent(n)
            u = self.bro(p)
            g = self.parent(p)
            
            if not u.is_black():    # case 1
                p.set_black()
                u.set_black()
                g.get_red()
                n = g
                continue
                
            if p == g.left:    # p为左节点
                if n == p.right:    # case 2
                    self.rotate_l(p)
                    n, p = p, n
                p.set_black()    # case3
                g.set_red()
                self.rotate_r(g)
            else:
                if n == p.right:    # case 2
                    self.rotate_l(p)
                    n, p = p, n
                p.set_black()    # case3
                g.set_red()
                self.rotate_l(g)
                
        # 根节点强制置黑，有两种情况根节点是红色：
        # 1. 新插入时是红色
        # 2. 经过case 1调整过后变红色
        self.root.color = 'black'
        
    def delete(self, val):
        assert type(val) is int
        
        n = self.self.search(val)
        if n is None:
            print('can not find any nodes with value {}'.format(val))
            return
        
        self._delete_node(n)
        
    def _delete_node(self, node):
        n = node
        
        # n的子节点个数等于2
        if self.children_count(n) == 2:
            # 寻找n的后继s
            s = n.right
            while s.left != self.black_leaf:
                s = s.left
            n.val = s.val
            n = s
            
        # n的子节点个数小于2
        if n.left == self.black_leaf:
            c = n.right
        else:
            c = n.left
        self._transplant(n, c)
        
        # 删除的节点是黑色，需要调整
        if n.is_black():
            self._delete_fixup(c)
        return
    
    def _delete_fixup(self, node):
        n = node
        while n != self.root and n.is_black():
            p = self.parent(n)
            b = self.bro(n)
            
            # 左右节点对称
            if p.left == n:
                if not b.is_black():
                    b.set_black()    # case 1
                    p.set_red()
                    self.rotate_l(p)
                    # new bro after rotate
                    b = self.bro(n)
                
                if b.left.is_black() and b.right.is_black():
                    b.set_red()                     # case 2
                    n = p                           # case 2
                else:
                    if b.right.is_black():
                        b.left.set_black()          # case 3
                        b.set_red()                 # case 3
                        self.rotate_r(b)            # case 3
                        # new bro after rotate
                        b = self.bro(n)             # case 3

                    # 注意，因为p可能是红或黑，所以不能直接赋值颜色，只能copy
                    b.color = p.color               # case 4
                    p.set_black()                   # case 4
                    b.right.set_black()             # case 4
                    self.rotate_l(p)                # case 4
                    # trick, 调整结束跳出while
                    n = self.root                   # case 4
            else:
                if not b.is_black():
                    b.set_black()                   # case 1
                    p.set_red()                     # case 1
                    self.rotate_r(p)                # case 1
                    # new bro after rotate
                    b = self.bro(n)                 # case 1

                if b.left.is_black() and b.right.is_black():
                    b.set_red()                     # case 2
                    n = p                           # case 2
                else:
                    if b.left.is_black():
                        b.right.set_black()         # case 3
                        b.set_red()                 # case 3
                        self.rotate_l(b)            # case 3
                        # new bro after rotate
                        b = self.bro(n)             # case 3

                    # 注意，因为p可能是红或黑，所以不能直接赋值颜色，只能copy
                    b.color = p.color               # case 4
                    p.set_black()                   # case 4
                    b.left.set_black()              # case 4
                    self.rotate_r(p)                # case 4
                    # trick, 调整结束跳出while
                    n = self.root                   # case 4

        # 将n设为黑色，从上面while循环跳出，情况有两种
        # 1. n是根节点，直接无视附加的黑色
        # 2. n是红色的节点，则染黑
        n.set_black()

    def _transplant(self, n1, n2):
        """
        节点移植， n2 -> n1
        :param n1: 原节点
        :param n2: 移植节点
        :return:
        """
        if n1 == self.root:
            if n2 != self.black_leaf:
                self.root = n2
                n2.parent = None
            else:
                self.root = None    # 只有删除根节点时会进来
        else:
            p = self.parent(n1)
            if p.left == n1:
                p.left = n2
            else:
                p.right = n2

            n2.parent = p

    def rotate_l(self, node):
        """
        左旋
        :param node:
        :return:
        """
        if node is None:
            return

        if node.right is self.black_leaf:
            return
            # raise Exception('try rotate left , but the node "{}" has no right child'.format(node.val))

        p = self.parent(node)
        x = node
        y = node.right

        # node为根节点时，p为None，旋转后要更新根节点指向
        if p is not None:
            if x == p.left:
                p.left = y
            else:
                p.right = y
        else:
            self.root = y

        x.parent, y.parent = y, p

        if y.left != self.black_leaf:
            y.left.parent = x

        x.right, y.left = y.left, x

    def rotate_r(self, node):
        """
        右旋
        :param node:
        :return:
        """
        if node is None:
            return

        if node.left is self.black_leaf:
            return
            # raise Exception('try rotate right , but the node "{}" has no left child'.format(node.val))

        p = self.parent(node)
        x = node
        y = node.left

        # 同左旋
        if p is not None:
            if x == p.left:
                p.left = y
            else:
                p.right = y
        else:
            self.root = y

        x.parent, y.parent = y, p

        if y.right is not None:
            y.right.parent = x

        x.left, y.right = y.right, x

    @staticmethod
    def bro(node):
        """
        获取兄弟节点
        :param node:
        :return:
        """
        if node is None or node.parent is None:
            return None
        else:
            p = node.parent
            if node == p.left:
                return p.right
            else:
                return p.left

    @staticmethod
    def parent(node):
        """
        获取父节点
        :param node:
        :return:
        """
        if node is None:
            return None
        else:
            return node.parent

    def children_count(self, node):
        """
        获取子节点个数
        :param node:
        :return:
        """
        return 2 - [node.left, node.right].count(self.black_leaf)

    def draw_img(self, img_name='Red_Black_Tree.png'):
        """
        画图
        用pygraphviz画出节点和箭头
        箭头的红色和黑色分别代表左和右
        :param img_name:
        :return:
        """
        if self.root is None:
            return

        tree = pgv.AGraph(directed=True, strict=True)

        q = Queue()
        q.put(self.root)

        while not q.empty():
            n = q.get()
            if n != self.black_leaf:  # 黑色叶子的连线由各个节点自己画
                tree.add_node(n.val, color=n.color)
                #  画父节点箭头
                # if n.parent is not None:
                #     tree.add_edge(n.val, n.parent.val)

                for c in [n.left, n.right]:
                    q.put(c)
                    color = 'red' if c == n.left else 'black'
                    if c != self.black_leaf:
                        tree.add_edge(n.val, c.val, color=color)
                    else:
                        tree.add_edge(n.val, 'None', color=color)

        tree.graph_attr['epsilon'] = '0.01'
        tree.layout('dot')
        tree.draw(OUTPUT_PATH + img_name)
        return True


if __name__ == '__main__':
    rbt = RedBlackTree()

    # insert
    nums = list(range(1, 25))
    # random.shuffle(nums)
    for num in nums:
        rbt.insert(num)

    # search
    search_num = 23
    n = rbt.search(search_num)
    if n is not None:
        print(n)
    else:
        print('node {} not found'.format(search_num))

    # delete
    rbt.delete(4)

    # draw image
    rbt.draw_img('rbt.png')
```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    <ipython-input-1-d45e639f348e> in <module>()
          1 from queue import Queue
    ----> 2 import pygraphviz as pgv
          3 import random
          4 
          5 
    

    ModuleNotFoundError: No module named 'pygraphviz'

