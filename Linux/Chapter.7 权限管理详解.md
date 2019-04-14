
# ACL访问控制权限

在普通权限中，用户对文件只有三种身份，就是属主、属组和其他人；每种用户身份拥有读（read）、写（write）和执行（execute）三种权限。
![](http://c.biancheng.net/uploads/allimg/181011/2-1Q011153333H0.jpg)
根目录中有一个 /project 目录，这是班级的项目目录。班级中的每个学员都可以访问和修改这个目录，老师也需要对这个目录拥有访问和修改权限，其他班级的学员当然不能访问这个目录。需要怎么规划这个目录的权限呢？应该这样：老师使用 root 用户，作为这个目录的属主，权限为 rwx；班级所有的学员都加入 tgroup 组，使 tgroup 组作为 /project 目录的属组，权限是 rwx；其他人的权限设定为 0。这样这个目录的权限就可以符合我们的项目开发要求了。

有一天，班里来了一位试听的学员 st，她必须能够访问 /project 目录，所以必须对这个目录拥有 r 和 x 权限；但是她又没有学习过以前的课程，所以不能赋予她 w 权限，怕她改错了目录中的内容，所以学员 st 的权限就是 r-x。可是如何分配她的身份呢？变为属主？当然不行，要不 root 该放哪里？加入 tgroup 组？也不行，因为 tgroup 组的权限是 rwx，而我们要求学员 st 的权限是 r-x。如果把其他人的权限改为 r-x 呢？这样一来，其他班级的所有学员都可以访问 /project 目录了。

当出现这种情况时，普通权限中的三种身份就不够用了。

ACL 权限就是为了解决这个问题的。在使用 ACL 权限给用户 st 陚予权限时，st 既不是 /project 目录的属主，也不是属组，仅仅赋予用户 st 针对此目录的 r-x 权限。这有些类似于 Windows 系统中分配权限的方式，单独指定用户并单独分配权限，这样就解决了用户身份不足的问题。

**ACL是Access Control List（访问控制列表）的缩写，不过在Linux系统中，ACL用于设定用户针对文件的权限，而不是在交换路由器中用来控制数据访问的功能（类似于防火墙）。**

## 开启ACL权限
查看ACL权限：
```bash
[root@localhost ~]# mount
/dev/sda1 on /boot type ext4 (rw)
/dev/sda3 on I type ext4 (rw)
…省略部分输出…
#使用mount命令可以看到系统中已经挂载的分区，但是并没有看到ACL权限的设置
[root@localhost ~]# dumpe2fs -h /dev/sda3
#dumpe2fs是查询指定分区文件系统详细信息的命令
…省略部分输出…
Default mount options: user_xattr acl
…省略部分输出…

[root@localhost ~]# mount -o remount, acl /
#手动添加ACL，重新挂载根分区，并加入ACL权限

[root@localhost ~]#vi /etc/fstab
UUID=c2ca6f57-b15c-43ea-bca0-f239083d8bd2 /ext4 defaults, acl 1 1
#加入ACL权限
[root@localhost ~]# mount -o remount /
#重新挂载文件系统或重启系统，使修改生效
```
其中，dumpe2fs 命令可选的选项及其含义如下：
- -h：仅显示超级块中的信息，而不显示磁盘块组的详细信息；

## ACL权限设置
### ACL权限管理命令
命令格式：
```bash
[root@localhost ~]# getfacle 文件名
#查看ACL权限
[root@localhost ~]# setfacl 选项 文件名
#设定ACL权限
```
选项：
- -m：设定 ACL 权限。如果是给予用户 ACL 权限，则使用"u:用户名：权限"格式赋予；如果是给予组 ACL 权限，则使用"g:组名：权限" 格式赋予；
- -x：删除指定的 ACL 权限；
- -b：删除所有的 ACL 权限；
- -d：设定默认 ACL 权限。只对目录生效，指目录中新建立的文件拥有此默认权限；
- -k：删除默认 ACL 权限；
- -R：递归设定 ACL 权限。指设定的 ACL 权限会对目录下的所有子文件生效；

### 给用户和用户组添加ACL权限
举个例子，就来看看上图中的权限怎么分配。我们要求 root 是 /project 目录的属主，权限是 rwx；tgroup 是此目录的属组，tgroup 组中拥有班级学员 zhangsan 和 lisi，权限是 rwx；其他人的权限是 0。这时，试听学员 st 来了，她的权限是 r-x。我们来看具体的分配命令。
```bash
[root@localhost ~]# useradd zhangsan
[root@localhost ~]# useradd lisi
[root@localhost ~]# useradd st
[root@localhost ~]# groupadd tgroup
#添加需要试验的用户和用户组，省略设定密码的过程
[root@localhost ~]# mkdir /project #建立需要分配权限的目录
[root@localhost ~]# chown root:tgroup /project/
#改变/project目录的属主和属组
[root@localhost ~]# chmod 770 /project/
#指定/project目录的权限
[root@localhost ~]# ll -d /project/
drwxrwx--- 2 root tgroup 4096 1月19 04:21 /project/
#查看一下权限，已经符合要求了
#这时st学员来试听了，如何给她分配权限
[root@localhost ~]# setfacl -m u:st:rx /project/
#给用户st赋予r-x权限，使用"u:用户名：权限" 格式
[root@localhost /]# cd /
[root@localhost /]# ll -d project/
drwxrwx---+ 3 root tgroup 4096 1月19 05:20 project/
#使用ls-l査询时会发现，在权限位后面多了一个"+"，表示此目录拥有ACL权限
[root@localhost /]# getfacl project
#查看/prpject目录的ACL权限
#file: project <-文件名
#owner: root <-文件的属主
#group: tgroup <-文件的属组
user::rwx <-用户名栏是空的，说明是属主的权限
user:st:r-x <-用户st的权限
group::rwx <-组名栏是空的，说明是属组的权限
mask::rwx <-mask权限
other::--- <-其他人的权限
```
st 用户既不是 /prpject 目录的属主、属组，也不是其他人，我们单独给 st 用户分配了 r-x 权限。这样分配权限太方便了，完全不用先辛苦地规划用户身份了。

给用户赋予ACL权限：
```bash
[root@localhost /]# groupadd tgroup2
#添加测试组
[root@localhost /]# setfacl -m g:tgroup2:rwx project/
#为组tgroup2纷配ACL权限，使用"g:组名:权限"格式
[root@localhost /]# ll -d project/
drwxrwx---+ 2 root tgroup 4096 1月19 04:21 project/
#属组并没有更改
[root@localhost /]# getfacl project/
#file: project/
#owner: root
#group: tgroup
user::rwx
user:st:r-x
group::rwx
group:tgroup2:rwx <-用户组tgroup2拥有了rwx权限
mask::rwx
other::--
```

# SetUID文件特殊权限
```bash
[root@localhost ~]#ll /usr/bin/passwd
-rwsr-xr-x.1 root root 25980 2月22 2012 /usr/bin/passwd
```
当一个具有执行权限的文件设置 SetUID 权限后，用户在执行这个文件时将以文件所有者的身份来执行。passwd 命令拥有 SetUID 权限，所有者为 root（Linux 中的命令默认所有者都是 root），也就是说，当普通用户使用 passwd 命令更改自己的密码的时候，实际上是在用 passwd 命令所有者 root 的身份在执行 passwd 命令，root 当然可以将密码写入 /etc/shadow 文件，所以普通用户也可以修改 /etc/shadow 文件，命令执行完成后，该身份也随之消失。

SetUID 的功能可以这样理解：
- 只有可以执行的二进制程序才能设定 SetUID 权限。
- 命令执行者要对该程序拥有 x（执行）权限。
- 命令执行者在执行该程序时获得该程序文件属主的割分（在执行程序的过程中变为文件的属主）。
- SetUID 权限只在该程序执行过程中有效，也就是说身份改变只在程序执行过程中有效。


```bash
[root@localhost ~]# su - lamp
[lamp@localhost ~]$ passwd
更改用户lamp的密码。
为lamp更改STRESS密码。
（当前）UNIX密码：
#输入旧密码
新的密码：
#输入新密码
重新输入新的密码：
passwd:所有的身份验证令牌已经成功更新
#lamp可以修改自己的密码
[lamp@localhost ~]$ cat /etc/shadow
cat:/etc/shadow:权限不够
#但是不能査看/etc/shadow文件的内容
```
![](http://c.biancheng.net/uploads/allimg/181011/2-1Q0111H312U8.jpg)
从示意图中可以知道:
passwd 是系统命令，可以执行，所以可以赋予 SetUID 权限。
lamp 用户对 passwd 命令拥有 x（执行）权限。
lamp 用户在执行 passwd 命令的过程中，会暂时切换为 root 身份，所以可以修改 /etc/shadow 文件。
命令结束，lamp 用户切换回自己的身份。

```bash
[root@localhost ~]# chmod u-s /usr/bin/passwd
#属主取消SetUID权限
[root@localhost ~]# ll /usr/bin/passwd
-rwxr-xr-x.1 root root 25980 2月22 2012/usr/bin/passwd
[root@localhost ~]# su -lamp
[lamp@localhost ~]$ passwd
更改用户lamp的密码。
为lamp更改STRESS密码。
（当前）UNIX密码：
#看起来没有什么问题
新的密码：
重新输入新的密码：
passwd:鉴定令牌操作错误
#但是最后密码没有生效
```

# SetGID（SGID）文件特殊权限
当 s 标志在属主的 x 位置时是 SetUID，那么 s 标志在属组的 x 位置时是 SetGID，简称为SGID。

## SetGID针对文件的作用
SetGID 既可以针对文件生效，也可以针对目录生效，这和 SetUID 明显不同。

如果针对文件，那么 SetGID 的含义如下：
- 只有可执行的二进制程序才能设置 SetGID 权限。
- 命令执行者要对该程序拥有 x（执行）权限。
- 命令执行者在执行程序的时候，组身份升级为该程序文件的属组。
- SetGID 权限同样只在该程序执行过程中有效，也就是说，组身份改变只在程序执行过程中有效。

当普通用户 lamp 执行 locate 命令时，会发生如下事情：
- /usr/bin/locate 是可执行二进制程序，可以被赋予 SetGID 权限。
- 执行用户 lamp 对 locate 命令拥有执行权限。
- 执行 locate 命令时，组身份会升级为 slocate 组，而 slocate 组对/var/lib/mlocate/mlocate.db 数据库拥有 r 权限，所以普通用户可以使用 locate 命令査询 mlocate.db 数据库。
- 命令结束，lamp 用户的组身份返回为 lamp 组。

## SetGID针对目录的作用
如果 SetGID 针对目录设置，则其含义如下：
- 普通用户必须对此目录拥有 r 和 x 权限，才能进入此目录。
- 普通用户在此目录中的有效组会变成此目录的属组。
- 若普通用户对此目录拥有 w 权限，则新建文件的默认属组是这个目录的属组。

# Stick BIT（SBIT）文件特殊权限
**Sticky BIT 意为粘着位（或粘滞位），也简称为 SBIT。**它的作用如下：
- 粘着位目前只对目录有效。
- 普通用户对该目录拥有 w 和 x 权限，即普通用户可以在此目录中拥有写入权限。
- 如果没有粘着位，那么，因为普通用户拥有 w 权限，所以可以删除此目录下的所有文件，包括其他用户建立的文件。一旦被赋予了粘着位，除了 root 可以删除所有文件，普通用户就算拥有 w 权限，也只能删除自己建立的文件，而不能删除其他用户建立的文件。

# Linux文件特殊权限设置详解
前面章节中介绍了 SUID、SGID 以及 SBIT 特殊权限，那么到底该如何设置特殊权限呢？

其实还是依赖 chmod 命令的，只不过文件的普通权限只有三个数字，例如，"755"代表属主拥有读、写、执行权限；属组拥有读、执行权限；其他人拥有读、执行权限。如果把特殊权限也考虑在内，那么权限就应该写成"4755"，其中"4"就是特殊权限 SetUID了，"755"还是代表属主、属组和其他人的权限。

这几个特殊权限这样来表示：
- 4 代表 SetUID；
- 2 代表 SetGID；
- 1 代表 SBIT；

可以通过"u+s"赋予 SetUID 权限，通过"g+s"赋予 SetGID 权限，通过"o+t"赋予 SBIT 权限。特殊权限只针对具有可执行权限的文件有效，不具有 x 权限的文件被赋予了 SetUID 和 SetGID 权限会被标记为 S，SBIT 权限会被标记为 T，仔细想一下，如果没有可执行权限，则设置特殊权无可意义。

# chattr命令详解：修改文件系统的权限属性
chatrr 只有 root 用户可以使用，用来修改文件系统的权限属性，建立凌驾于 rwx 基础权限之上的授权。

chatrr 命令格式如下：
```bash
[root@localhost ~]# chattr [+-=] [选项] 文件或目录名
```
选项：
- +：増加权限；
- -：删除权限；
- =：等于某权限；
- i：如果对文件设置属性，那么不允许对文件进行删除、改名，也不能添加和修改数据；如果对目录设置 i 属性，那么只能修改目录下文件中的数据，但不允许建立和删除文件；
- a：如果对文件设置 a 属性，那么只能在文件中増加数据，但是不能删除和修改数据；如果对目录设置 a 属性，那么只允许在目录中建立和修改文件，但是不允许删除文件；
- e：Linux 中的绝大多数文件都默认拥有 e 属性，表示该文件是使用 ext 文件系统进行存储的，而且不能使用"chattr -e"命令取消 e 属性；

# lsattr命令：查看文件系统属性
lsattr 命令比较简单，其命令格式如下：
```bash
[root@localhost ~]# lsattr 选项 文件名
```
选项：
- -a：显示所有文件和目录；
- -d：如果目标是目录，则仅列出目录本身的属性，而不会列出文件的属性；

# sudo命令用法详解：系统权限管理
sudo 的操作对象是系统命令，也就是 root 把本来只能由超级用户执行的命令赋予普通用户执行。

sudo 使用简单，管理员 root 使用 visudo 命令即可编辑其配置文件 /etc/sudoers 进行授权。
```bash
[root@localhost ~]# visudo
…省略部分输出…
root ALL=(ALL) ALL
#用户名 被管理主机的地址=(可使用的身份) 授权命令(绝对路径)
#%wheel ALL=(ALL) ALL
#%组名 被管理主机的地址=(可使用的身份) 授权命令(绝对路径)
…省略部分输出…
```
4 个参数的具体含义如下：
- 用户名/组名：代表 root 给哪个用户或用户组赋予命令，注意组名加"%"。
- 用户可以用指定的命令管理指定 IP 地址的服务器。如果写 ALL，则代表用户可以管理任何主机；如果写固定 IP，则代表用户可以管理指定的服务器。如果我们在这里写本机的 IP 地址，则不代表只允许本机的用户使用指定命令，而代表指定的用户可以从任何 IP 地址来管理当前服务器。
- 可使用的身份：就是把来源用户切换成什么身份使用，(ALL) 代表可以切换成任意身份。这个字段可以省略。
- 授权命令：代表 root 把什么命令授权给普通用户。默认是 ALL，代表任何命令，这当然不行，如果需要给哪个命令授权，则只需写入命令名即可。不过需要注意，一定要写绝对路径。


