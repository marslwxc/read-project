
![原始链表](https://static001.geekbang.org/resource/image/e1/6d/e18303fcedc068e5a168de04df956f6d.jpg)
![第一级索引](https://static001.geekbang.org/resource/image/14/8e/14753c824a5ee4a976ea799727adc78e.jpg)
![第二级索引](https://static001.geekbang.org/resource/image/49/65/492206afe5e2fef9f683c7cff83afa65.jpg)
如图中那样，对链表建立一级“索引”，每两个结点提取一个结点到上一级，我们把抽出来的那一级叫做**索引**或**索引层**。图中down表示down指针，指向下一级结点。**加一层索引之后，查找一个结点需要遍历的结点个数减少了**。

**这种链表加多级所以的结构，就是跳表**
1. 跳表查询任意数据的时间复杂度是O(logn)，其实就是基于链表的二分查找
2. 跳表的空间复杂度是O(n)
3. 跳表插入、删除数据的时间复杂度也是O(logn)，其实就是O(logn)查找数据，O(1)插入、删除数据
![插入数据](https://static001.geekbang.org/resource/image/65/6c/65379f0651bc3a7cfd13ab8694c4d26c.jpg)
4. 作为一种动态数据结构，跳表通过一个随机函数，来决定索引结点的更新。
![动态生成索引](https://static001.geekbang.org/resource/image/65/6c/65379f0651bc3a7cfd13ab8694c4d26c.jpg)


```python

```
