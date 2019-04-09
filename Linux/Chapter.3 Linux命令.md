
# Linux命令的基本格式
## 命令提示符
登录系统后，第一眼看到的内容是：
```bash
[root@localhost ~]#
```
这就是 Linux 系统的命令提示符。那么，这个提示符的含义是什么呢？
- []：这是提示符的分隔符号，没有特殊含义。
- root：显示的是当前的登录用户，笔者现在使用的是 root 用户登录。
- @：分隔符号，没有特殊含义。
- localhost：当前系统的简写主机名（完整主机名是 localhost.localdomain）。
- ~：代表用户当前所在的目录，此例中用户当前所在的目录是家目录。
- #：命令提示符，Linux 用这个符号标识登录的用户权限等级。如果是超级用户，提示符就是 #；如果是普通用户，提示符就是 \$。

## 命令的基本格式
Linux 命令的基本格式:
```bash
[root@localhost ~]# 命令[选项][参数]
```
**命令的选项用于调整命令功能，而命令的参数是这个命令的操作对象。**

# ls命令

- 命令名称：ls
- 英文原意：list
- 所在路径：/bin/ls
- 执行权限：所有用户
- 功能描述：显示当前目录下的内容
## 命令格式
```bash
[root@localhost ~]#ls [选项][文件名或目录名]
```
选项：
- -a：显示所有文件
- -color=when：支撑颜色输出，when值的默认值是always（总是显示颜色），也可以是never（从不显示颜色）和auto（自动）
- -d：显示目录信息，而不是目录下的文件
- -h：人性化显示，按照我们习惯的单位显示文件大小
- -i：显示文件的i结点号
    - 第一列：权限，具体权限的含义将在后续章节中讲解。
    - 第二列：引用计数，文件的引用计数代表该文件的硬链接个数，而目录的引用计数代表该目录有多少个一级子目录。
    - 第三列：所有者，也就是这个文件属于哪个用户。默认所有者是文件的建立用户
    - 第四列：所属组，默认所属组是文件建立用户的有效组，一般情况下就是建立用户的所在组。
    - 第五列：大小，默认单位是字节。
    - 第六列：文件修改时间，文件状态修改时间或文件数据修改时间都会更改这个时间，注意这个时间不是文件的创建时间。
    - 第七列：文件名。
- -l：长格式显示

# cd命令

- 命令名称：cd。
- 英文原意：change directory。
- 所在路径：Shell 内置命令。
- 执行权限：所有用户。
- 功能描述：切换所在目录。
## 命令格式
```bash
[root@localhost ~]#cd [目录名]
```
选项：
- -P（大写）是指如果切换的目录是软链接目录，则进入其原始的物理目录，而不是进入软链接目录；
- -L（大写）是指如果切换的目录是软链接目录，则直接进入软链接目录。

cd命令特殊符号：

符号|作用
----|----
~|代表用户的家目录
-|代表上次所在的目录
.|代表当前目录
..|代表上级目录

## 绝对路劲和相对路径
 Linux 有最高目录，也就是根目录。如果路径是从根目录开始，一级一级指定的，那使用的就是绝对路径。
 
 所谓相对路径，就是只从当前所在目录开始，切换目录。

# mkdir命令

- 命令名称：mkdir。
- 英文原意：make directories。
- 所在路径：/bin/mkdir。
- 执行权限：所有用户。
- 功能描述：创建空目录。
## 命令格式：
```bash
[root@localhost -]# mkdir [选项]目录名
```
选项：
- -p: 递归建立所需目录

# rmdir命令

- 命令名称：rmdir。
- 英文原意：remove empty directories。
- 所在路径：/bin/rmdir。
- 执行权限：所有用户。
- 功能描述：删除空目录。
## 命令格式
```bash
[root@localhost -]# rmdir [选项]目录名
```
选项：
- -p：递归删除目录

但 rmdir 命令的作用十分有限，因为只能刪除空目录，所以一旦目录中有内容，就会报错。

# touch命令
touch 的意思是触摸，如果文件不存在，则会建立空文件；如果文件已经存在，则会修改文件的时间戳（访问时间、数据修改时间、状态修改时间都会改变）。
- 命令名称：touch。
- 英文原意：change file timestamps。
- 所在路径：/bin/touch。
- 执行权限：所有用户。
- 功能描述：修改文件的时间戳。
## 命令格式
```bash
[root@localhost -]# touch [选项]文件名或目录名
```
选项：
- -a：只修改文件访问时间（Access Time）
- -c：如果文件不存在，则不新建文件
- -d：把文件的时间改为指定的时间
- -m：只修改文件的数据修改时间（Modify Time）

Linux 中的每个文件都有三个时间，分别是**访问时间（Access Time）、数据修改时间（Modify Time）和状态修改时间（Change Time）**。touch 命令只能手工指定只修改访问时间，或是只修改数据修改时间，而不能指定只修改状态修改时间。因为不论是修改访问时间，还是修改文件的数据时间，对文件来讲，状态都会发生改变，即状态修改时间会随之改变。

# stat命令
- 命令名称：stat。
- 英文原意：display file or file system status。
- 所在路径：/usr/bin/stat。
- 执行权限：所有用户。
- 功能描述：显示文件或文件系统的详细信息。
## 命令格式
```bash
[root@localhost ~]# stat [选项]文件名或目录名
```
选项：
- -f：査看文件所在的文件系统信息，而不是査看文件的信息。

# cat命令
- 命令名称：cat。
- 英文原意：concatenate files and print on the standard output。
- 所在路径：/bin/cat。
- 执行权限：所有用户。
- 功能描述：连接文件并打印输出到标准输出。

命令格式：
```bash
[root@localhost ~]# cat [选项]文件名
```
选项：
- -A：相当于 -vET 选项的整合，用于列出所有隐藏符号；
- -E：列出每行结尾的回车符 \$；
- -n：显示行号；
- -T：把 Tab 键 ^I 显示出来；
- -V：列出特殊字符；

# more命令
- 命令名称：more。
- 英文原意：file perusal filter for crt viewin。
- 所在路径：/bin/more。
- 执行权限：所有用户。
- 功能描述：分屏显示文件内容。

命令格式：
```bash
[root@localhost ~]# more 文件名
```
交互命令：
- 空格键：向下翻页。
- b：向上翻页。
- 回车键：向下滚动一行。
- / 字符串：搜索指定的字符串。
- q：退出。

# head命令
- 命令名称：head。
- 英文原意：output the first part of files。
- 所在路径：/usr/bin/head。
- 执行权限：所有用户。
- 功能描述：显示文件开头的内容。

命令格式
```bash
[root@localhost ~]# head [选项]文件名
```
选项：
- -n 行数： 从文件头开始，显示指定行数；
- -v：显示文件名；

# tail命令
- 命令名称：tail。
- 英文原意：output the last part of files。
- 所在路径：/usr/bin/tail。
- 执行权限：所有用户。
- 功能描述：显示文件结尾的内容。

命令格式：
```bash
[root@localhost ~]#tail [选项] 文件名
```
选项：
- -n 行数：从文條尾开始，显示指定行数
- -f：监听文件的新増内容

# ln命令
- 命令名称：ln。
- 英文原意：make links between file0
- 所在路径：/bin/ln。
- 执行权限：所有用户。
- 功能描述：在文件之间建立链接。

命令格式：
```bash
[root@localhost ~]# ln [选项] 源文件 目标文件    
```
选项：
- -s：建立软链接文件。如果不加"-s"选项，则建立硬链接文件；
- -f：强制。如果目标文件已经存在，则删除目标文件后再建立链接文件；

创建硬链接：
```bash
[root@localhost ~]# touch cangls
[root@localhost ~]# ln /root/cangls /tmp/
#建立硬链接文件，目标文件没有写文件名，会和原名一致
#也就是 /root/cangls 和 /tmp/cangls 是硬链接文件
```
创建软链接：
```bash
[root@localhost ~]# touch bols
[root@localhost ~]# In /root/bols /tmp/
#建立软链接文件
```
**这里需要注意，软链接文件的源文件必须写成绝对路径，而不能写成相对路径（硬链接没有这样的要求）；否则软链接文件会报错。这是初学者非常容易犯的错误。**


# rm命令
- 命令名称：rm
- 英文原意：remove files or directories。
- 所在路径：/bin/rm。
- 执行权限：所有用户。
- 功能描述：删除文件或目录。

命令格式：
```bash
[root@localhost ~]# rm[选项] 文件或目录
```
选项：
- -f：强制删除（force）
- -i：交互删除，在删除之前会询问用户
- -r：递归删除，可以删除目录（recursive）

# cp命令
- 命令名称：cp；
- 英文原意：copy files and directories；
- 所在路径：/bin/cp；
- 执行权限：所有用户；
- 功能描述：复制文件和目录；

命令格式：
```bash
[root@localhost ~]# cp [选项] 源文件 目标文件
```
选项：
- -a：相当于 -d、-p、-r 选项的集合，这几个选项我们一一介绍；
- -d：如果源文件为软链接（对硬链接无效），则复制出的目标文件也为软链接；
- -i：询问，如果目标文件已经存在，则会询问是否覆盖；
- -l：把目标文件建立为源文件的硬链接文件，而不是复制源文件；
- -s：把目标文件建立为源文件的软链接文件，而不是复制源文件；
- -p：复制后目标文件保留源文件的属性（包括所有者、所属组、权限和时间）；
- -r：递归复制，用于复制目录；

# mv命令
- 命令名称：mv。
- 英文原意：move(rename)files。
- 所在路径：/bin/mv。
- 执行权限：所有用户。
- 功能描述：移动文件或改名。

命令格式：
```bash
[root@localhost ~]# mv 【选项】 源文件 目标文件
```
选项：
- -f：强制覆盖，如果目标文件已经存在，则不询问，直接强制覆盖；
- -i：交互移动，如果目标文件已经存在，则询问用户是否覆盖（默认选项）；
- -n：如果目标文件已经存在，则不会覆盖移动，而且不询问用户；
- -v：显示详细信息；

# chmod命令
- 命令名称：chmod。
- 英文原意：change file mode bits。
- 所在路径：/bin/chmod。
- 执行权限：所有用户。
- 功能描述：修改文件的权限模式。

命令格式：
```bash
[root@localhost ~]# chmod [选项] 权限模式 文件名
```
选项：
- -R：递归设置权限，也就是给子目录中的所有文件设定权限
- 用户身份：
    - -u：代表所有者(user)。
    - -g：代表所属组(group)。
    - -o：代也人(other)。
    - -a：代表全部身份(all)。
- 赋予方式：
    - -+：加入权限。
    - --：减去权限。
    - -=：设置权限。
- 权限：
    - -r：读取权限(read)。
    - -w：写权限(write)。
    - -x：执行权限(execute)。
- 数字权限
    - 4：代表"r"权限。
    - 2：代表"w"权限。
    - 1：代表"x"权限。
- 常用权限
    - 644：这是文件的基本权限，代表所有者拥有读、写权限，而所属组和其他人拥有只读权限。
    - 755：这是文件的执行权限和目录的基本权限，代表所有者拥有读、写和执行权限，而所属组和其他人拥有读和执行权限。
    - 777:这是最大权限。在实际的生产服务器中，要尽力避免给文件或目录赋予这样的权限，这会造成一定的安全隐患。

## 权限对文件的作用。
- 读(r)：对文件有读（r）权限，代表可以读取文件中的数据。如果把权限对应到命令上，那么一旦对文件有读（r）权限，就可以对文件执行 cat、more、less、head、tail 等文件查看命令。
- 写(w)：对文件有写（w）权限，代表可以修改文件中的数据。如果把权限对应到命令上，那么一旦对文件有写（w）权限，就可以对文件执行 vim、echo 等修改文件数据的命令。注意，对文件有写权限，是不能删除文件本身的，只能修改文件中的数据。如果要想删除文件，则需要对文件的上级目录拥有写权限。
- 执行(x)：对文件有执行（x）权限，代表文件拥有了执行权限，可以运行。在 Linux 中，只要文件有执行（x）权限，这个文件就是执行文件了。只是这个文件到底能不能正确执行，不仅需要执行（x）权限，还要看文件中的代码是不是正确的语言代码。对文件来说，执行（x）权限是最高权限。

## 权限对目录的作用
- 读(r)：对目录有读 （r）权限，代表可以查看目录下的内容，也就是可以查看目录下有哪些子文件和子目录。如果把权限对应到命令上，那么一旦对目录拥有了读（r）权限，就可以在目录下执行 ls 命令，查看目录下的内容了。
- 写(w)：对目录有写（r）权限，代表可以修改目录下的数据，也就是可以在目录中新建、删除、复制、剪切子文件或子目录。如果把权限对应到命令上，那么一旦对目录拥有了写（w）权限，就可以在目录下执行 touch、rm、cp、mv 命令。对目录来说，写（w）权限是最高权限。
- 执行(x)：目录是不能运行的，那么对目录拥有执行（x）权限，代表可以进入目录。如果把权限对应到命令上，那么一旦对目录拥有了执行（x）权限，就可以对目录执行 cd 命令，进入目录。

# chown命令
- 命令名称：chown。
- 文原意：change file owner and group。
- 所在路径：/bin/chown。
- 执行权限：所有用户。
- 功能描述：修改文件和目录的所有者和所属组。

命令格式：
```bash
[root@localhost ~]# chown [选项] 所有者：所属组文件或目录
```
选项：
- -R： 递归设置权限，也就是给子目录中的所有文件设置权限

# chgrp命令
- 命令名称：chgrp。
- 英文原意：change group ownership。
- 所在路径：/bin/chgrp。
- 执行权限：所有用户。
- 功能描述：修改文件和目录的所属组。

# man命令
- 命令名称：man。
- 英文原意：format and display the on-line manual pages。
- 所在路径：/usr/bin/man。
- 执行权限：所有用户。
- 功能描述：显示联机帮助手册。

命令格式：
```bash
[root@localhost ~]# man [选项]命令
```
选项：
- -f：査看命令拥有哪个级别的帮助
- -k: 査看和命令相关的所有帮助

快捷键：

快捷键|作用
------|----
上箭头|向上移动一行
下箭头|向下移动一行
PgUp|向上翻一页
PgDn|向下翻一页
g|移动到第一页
G|移动到最后一页
q|退出
/字符串|从当前页向下搜索字符串
?字符串|从当前页向上搜索字符串
n|当搜索字符串时，可以使用n键找到下一个字符串
N|当搜索字符串时，使用N键反向查询字符串。也就是说，如果使用“/字符串”方式搜索， 则N键表示向上搜索字符串；如果使用“?字符串”方式搜索，则N键表示向下搜索字符串

# whereis命令
- 命令名称：whereis。
- 英文原意：locate the binary, source, and manual page files for a command。
- 所在路径：/usr/bin/whereis.
- 执行权限：所有用户。
- 功能描述：査找二进制命令、源文件和帮助文档的命令。

命令格式：
```bash
[root@localhost ~]# whereis [选项] 命令
```
选项：
- -b: 只査找二制命令；
- -m: 只查找帮助文档；

# which命令
- 命令名称：which。
- 英文原意：shows the full path of(shell)commands。
- 所在路径：/usr/bin/which。
- 执行权限：所有用户。
- 功能描述：列出命令的所在路径。

# locate命令
- 命令名称：locate。
- 英文原意：find files by name。
- 所在路径：/usr/bin/locate。
- 执行权限：所有用户。
- 功能描述：按照文件名搜索文件。

命令格式：
```bash
[root@localhost ~]# locate [选项] 文件名
```
选项：
- -i：忽略大小写

locate 命令的局限也很明显，它**只能按照文件名来搜索文件，而不能执行更复杂的搜索**，比如按照权限、大小、修改时间等搜索文件。如果要按照复杂条件执行搜索，则只能求助于功能更加强大的 find 命令。**locate 命令的优点鮮常明显，那就是搜索速度非常快，而且耗费系统资源非常小**。这是因为 **locate 命令不会直接搜索硬盘空间，而会先建立 locate 数据库，然后在数据库中按照文件名进行搜索，是快速的搜索命令**。

# find命令
- 命令名称：find。
- 英文原意：search for files in a directory hierarchy.
- 所在路径：/bin/find。
- 执行权限：所有用户。
- 功能描述：在目录中查找文件。

命令格式：
```bash
[root@localhost ~]# find 搜索路径 [选项] 搜索内容
```
find 是比较特殊的命令，它有两个参数：
- 第一个参数用来指定搜索路径；
- 第二个参数用来指定搜索内容。

## 按照文件名搜索：
```bash
[root@localhost ~]#find 搜索路径 [选项] 搜索内容
```
选项：
- -name: 按照文件名搜索；
- -iname: 按照文件名搜索，不区分文件名大小；
- -inum: 按照 inode 号搜索；

**find 命令是完全匹配的，必须和搜索关键字一模一样才会列出。**

## 按照文件大小搜索
```bash
[root@localhost ~]#find 搜索路径 [选项] 搜索内容
```
选项：
- -size[+-]大小：按照指定大小搜索文件。这里的"+"的意思是搜索比指定大小还要大的文件，"-" 的意思是搜索比指定大小还要小的文件。

## 按照修改时间搜索
Linux 中的文件有访问时间(atime)、数据修改时间(mtime)、状态修改时间(ctime)这三个时间，我们也可以按照时间来搜索文件。
```bash
[root@localhost ~]# find搜索路径 [选项] 搜索内容
```
选项：
- -atime [+-]时间: 按照文件访问时间搜索
- -mtime [+-]时间: 按照文改时间搜索
- -ctime [+-]时间: 按照文件修改时间搜索
这三个时间的区别我们在 stat 命令中已经解释过了，这里用 mtime 数据修改时间来举例，重点说说 "[+-]"时间的含义。
- -5：代表@内修改的文件。
- 5：代表前5~6天那一天修改的文件。
- +5：代表6天前修改的文件。

## 按照权限搜索
```bash
[root@localhost ~]# find 搜索路径 [选项] 搜索内容
```
选项：
- -perm 权限模式：査找文件权限刚好等于"权限模式"的文件
- -perm -权限模式：査找文件权限全部包含"权限模式"的文件
- -perm +权限模式：査找文件权限包含"权限模式"的任意一个权限的文件

## 按照所有者和所属组搜索
```bash
[root@localhost ~]# find 搜索路径 [选项] 搜索内容
```
选项：
- -uid 用户 ID:按照用户 ID 査找所有者是指定 ID 的文件
- -gid 组 ID:按照用户组 ID 査找所属组是指定 ID 的文件
- -user 用户名：按照用户名査找所有者是指定用户的文件
- -group 组名：按照组名査找所属组是指定用户组的文件
- -nouser：査找没有所有者的文件

## 按照文件类型搜索
```bash
[root@localhost ~]# find 搜索路径 [选项] 搜索内容
```
选项:
- -type d：查找目录
- -type f：查找普通文件
- -type l：查找软链接文件

## 逻辑运算符
```bash
[root@localhost ~]#find 搜索路径 [选项] 搜索内容
```
选项：
- -a：and逻辑与
- -o：or逻辑或
- -not：not逻辑非

# zip命令
- 命令名称：zip。
- 英文原意：package and compress(archive)files。
- 所在路径：/usr/bin/zip。
- 执行权限：所有用户。
- 功能描述：压缩文件或目录。

命令格式：
```bash
[root@localhost ~]#zip [选项] 压缩包名 源文件或源目录
```
选项：
- -r：压缩目录

# unzip命令
- 命令名称：unzip。
- 英文原意：list, test and extract compressed files in a ZIP archive。
- 所在路径：/usr/bin/unzip.
- 执行权限：所有用户。
- 功能描述：列表、测试和提取压缩文件中的文件。

命令格式：
```bash
[root@localhost ~]# unzip [选项] 压缩包名
```
选项：
- -d： 指定解压缩位置

# gzip命令
- 命令名称：gzip。
- 英文原意：compress or expand files。
- 所在路径：/bin/gzip。
- 执行权限：所有用户。
- 功能描述：压缩文件或目录。

命令格式：
```bash
[root@localhost ~]# gzip [选项] 源文件
```
选项：
- -c：将压缩数据输出到标准输出中，可以用于保留源文件；
- -d：解压缩；
- -r：压缩目录；
- -v：显示压缩文件的信息；
- -数字：用于指定压缩等级，-1 压缩等级最低，压缩比最差；-9 压缩比最高。默认压缩比是 -6；

# gunzip命令
- 命令名称：gunzip。
- 英文原意：compress or expand files。
- 所在路径：/bin/gunzip。
- 执行权限：所有用户。
- 功能描述：解压缩文件或目录。

命令格式：
常规用法就是直接解压缩文件
```bash
[root@localhost ~]# gunzip install.log.gz
```
如果要解压缩目录下的内容，则依然使用"-r"选项
```bash
[root@localhost ~]# gunzip -r test/
```
当然，"gunzip -r"依然只会解压缩目录下的文件，而不会解打包。要想解压缩".gz"格式，还可以使用 "gzip -d"命令，例如：
```bash
[root@localhost ~]# gzip -d anaconda-ks.cfg.gz
```

# tar命令
命令名称：tar。
英文原意：tar。
所在路径：/bin/tar。
执行权限：所有用户。
功能描述：打包与解打包命令。

打包命令格式：
```bash
[root@localhost ~]#tar [选项] [-f 压缩包名] 源文件或目录
```
选项：
- -c：打包；
- -f：指定压缩包的文件名。压缩包的扩展名是用来给管理员识别格式的，所以一定要正确指定扩展名；
- -v：显示打包文件过程；

解打包命令格式：
```bash
[root@localhost ~]#tar [选项] 压缩包
```
选项：
- -x：解打包；
- -f：指定压缩包的文件名；
- -v：显示打包文件过程；
- -t：测试，就是不解打包，只是査看包中有哪些文件；
- -C 目录：指定解打包位置；

# sync命令
- 命令名称：sync。
- 英文原意：flush file system buffers。
- 所在路径：/bin/sync。
- 执行权限：所有用户。
- 功能描述：刷新文件系统缓冲区。作用就是把内存中的数据强制向硬盘中保存。这个命令在常规关机的命令中其实会自动执行，但如果不放心，则应该在关机或重启之前手工执行几次，避免数据丟失。

命令格式：
```bash
[root@localhost ~]# sync
```

# shutdown命令
- 命令名称：shutdown。
- 英文原意：bring the system down。
- 所在路径：/sbin/shutdown。
- 执行权限：超级用户。
- 功能描述：关机和重启

命令格式：
```bash
[root@localhost ~]# shutdown [选项] 时间 [警告信息]
```
选项:
- -c：取消已经执行的 shutdown 命令；
- -h：关机；
- -r：重启；

# ifconfig命令
- 命令名称：ifconfig。
- 英文原意：configure a network interface。
- 所在路径：/sbin/ifconfig。
- 执行权限：超级用户。
- 功能描述：配置网络接口。

临时配置IP地址：
```bash
[root@localhost ~]#ifconfig eth0 192.168.44.3
#配置IP地址，不指定子网掩码就会使用标准子网掩码
[root@localhost ~]#ifconfig eth0 192.168.44.3 netmask 255.255.255.0
#配置IP地址，同时配置子网掩码
```

# ping命令
- 命令名称：ping。
- 英文原意：send ICMP ECHO_REQUEST to network hosts。
- 所在路径：/bin/ping。
- 执行权限：所有用户。
- 功能描述：向网络主机发送 ICMP 请求。

命令格式：
```bash
[root@localhost ~]# ping [选项] IP
```
选项：
- -b: 后面加入广播地址，用于对整个网段进行探测；
- -c 次数： 用于指定 ping 的次数；
- -s 字节： 指定探测包的大小；

# netstat命令
命令名称：netstat。
英文原意：Print network connections, routing tables, interface statistics, masquerade connections, and multicast memberships。
所在路径：/bin/netstat.
执行权限：所有用户。
功能描述：输出网络连接、路由表、接口统计、伪装连接和组播成员。

命令格式：
```bash
[root@localhost ~]# netstat [选项]
```
选项：
- -a：列出所有网络状态，包括 Socket 程序；
- -c秒数：指定每隔几秒刷新一次网络状态；
- -n：使用 IP 地址和端口号显示，不使用域名与服务名；
- -p：显示 PID 和程序名；
- -t：显示使用 TCP 协议端口的连接状况；
- -u：显示使用 UDP 协议端口的连接状况；
- -I：仅显示监听状态的连接；
- -r：显示路由表；

例子：
```bash
[root@localhost ~]# netstat -tuln
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address Foreign Address State
tcp  0  0 0.0.0.0:3306  0.0.0.0:* LISTEN
tcp  0  0 0.0.0.0:11211 0.0.0.0:* LISTEN
tcp  0  0 0.0.0.0:22 0.0.0.0:* LISTEN
tcp  0  0:::11211 :::* LISTEN
tcp  0  0 :::80 :::* LISTEN
tcp  0   0 :::22 :::* LISTEN
udp  0   0 0.0.0.0:11211 0.0.0.0:*
udp  0   0:::11211 :::*
#协议接收队列发送队列本机的 IP 地址及端口号 远程主机的 IP 地址及端口号 状态
```
1. Proto：网络连接的协议，一般就是 TCP 协议或者 UDP 协议。
2. Recv-Q：表示接收到的数据，已经在本地的缓冲中，但是还没有被进程取走。
3. Send-Q：表示从本机发送，对方还没有收到的数据，依然在本地的缓冲中，不具备 ACK 标志的数据包。
4. Local Address：本机的 IP 地址和端口号。
5. ForeignAddress：远程主机的 IP 地址和端口号。
6. State：状态。常见的状态主要有以下几种。
    - -LISTEN：监听状态，只有 TCP 协议需要监听，而 UDP 协议不需要监听。
    - -ESTABLISHED：已经建立连接的状态。如果使用"-I"选项，则看不到已经建立连接的状态。
    - -SYN_SENT：SYN 发起包，就是主动发起连接的数据包。
    - -SYN_RECV：接收到主动连接的数据包。
    - -FIN_WAIT1：正在中断的连接。
    - -FIN_WAIT2：已经中断的连接，但是正在等待对方主机进行确认。
    - -TIME_WAIT：连接已经中断，但是套接字依然在网络中等待结束。
    - -CLOSED：套接字没有被使用。

# write命令
- 命令名称：write。
- 英文原意：send a message to another user。
- 所在路径：/usr/bin/write。
- 执行权限：所有用户。
- 功能描述：向其他用户发送信息。

命令格式：
```bash
[root@localhost ~]# write 用户名 [终端号]
```

# mail命令
- 命令名称：mail。
- 英文原意：send and receive Internet mail。
- 所在路径：/bin/mail。
- 执行权限：所有用户。
- 功能描述：发送和接收电子邮件。

发送邮件
```bash
[root@localhost ~]# mail userl
Subject: hello <-邮件标题
Nice to meet you! <-邮件具体内容
. <-使用.来结束邮件输入
#发送邮件给user1用户
```
发送文件内容
```bash
[root@localhost ~]# mail -s "test mail" root </root/ anaconda-ks.cfg
#把/root/anaconda-ks.cfg文件的内容发送给root用户
```
- -s:指定邮件标题

查看已经接收的邮件。
```bash
[root@localhost ~]# mail
Heirloom Mail version 12.4 7/29/08.Type ?for help.
"/var/spool/mail/root": 1 message 1 new
>N 1 root Mon Dec 5 22:45 68/1777 "test mail"<-之前收到的由件
>N 2 root Mon Dec 5 23:08 18/602 "hello"
#未阅读编号发件人 时间 标题
&
<-等待用户输入命令
```

常用的交互命令
- headers：列出邮件标题列表，直接输入"h"命令即可。
- delete：删除指定邮件。比如想要删除第二封邮件，可以输入"d2"。
- save：保存邮件。可以把指定邮件保存成文件，如"s 2/tmp/test.mair。
- quit：退出，并把已经操作过的邮件进行保存。比如移除已删除邮件，保存已阅读邮脾。
- exit：退出，但是不保存任何操作。


```python

```
