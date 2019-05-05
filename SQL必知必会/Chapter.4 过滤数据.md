
# 4.1 使用WHERE子句
数据库表一般包含大量的数据，很少需要检索表中的所有行。通常只会根据特定操作或报告的需求提取表数据的子集。只检索所需数据需要指定**搜索条件(search criteria)** ，搜索条件也称为**过滤条件(filter condition)** 。在SELECT语句中，数据根据WHERE子句中指定的搜索条件进行过滤。

- 数据也可以在应用层过滤。为此，SQL的SELECT语句为客户端应用检索出超出实际需求的数据，然后客户端代码对返回数据进行循环，提取出需要的行。
- where的位置：在同时使用ORDER BY 和WHERE 子句时，应该让ORDER BY位于WHERE之后，否则将会产生错误。

# 4.2 WHERE子句操作符
where操作符|说明
-----------|----
=|等于
< >|不等于
!=|不等于
<|小于
<=|小于等于
!|不小于
>|大于
>=|大于等于
!>|不大于
BETWEEN|在指定的两个值之间
IS NULL|为NULL值

- 操作符兼容：并非所有DBMS都支持这些操作符。

## 4.2.1 检查单个值

```sql
- 列出所有价格小于10美元的产品
SELECT prod_name, prod_price
FROM Products
WHERE prod_price < 10;
```

## 4.2.2 不匹配检查

```sql
-列出所有不是供应商DLL01制造的产品
SELECT vend_id, prod_name
FROM Products
WHERE vend_id <> 'DLL01';
```
- 何时使用引号：单引号用来限定字符串。如果将值与字符串类型的列进行比较，就需要限定引号。用来与数据列进行比较的值不用引号。
- !=和<>通常可以互换：但是，并非所有DBMS都支持这两种不等于操作符。

## 4.2.3 范围值检查
要检查某个范围的值，可以使用BETWEEN操作符。其语法与其他WHERE子句的操作符稍有不同，因为它需要两个值，即范围的开始值和结束值。
```sql
- 检索价格在5美元和10美元之间的所有产品
SELECT prod_name, prod_price
FROM Products
WHERE prod_price BETWEEN 5 AND 10;
```
在使用BETWEEN时，必须指定两个值——所需范围的低端值和高端值。这两个值必须用AND关键字分隔。BETWEEN匹配范围中所有的值，包括指定的开始值和结束值。

## 4.2.4 空值检查
在创建表时，表设计人员可以指定其中的列能否不包含值。在一个列不包含值时，称其包含空值NULL

- NULL 空值(no value)，它与字段包含0，空字符串或仅仅包含空格不同。

确定值是否为NULL，不能简单地检查是否= NULL。SELECT语句有一个特殊的WHERE子句。可用来检查具有NULL值的列。这个WHERE子句就是IS NULL子句。
```sql
SELECT prod_name
FROM Products
WHERE prod_price IS NULL;
```

- 各DBMS特有的操作符：许多DBMS扩展了标准的操作符集，提供了更高级的过滤选择。
- NULL和非匹配：通过过滤选择不包含定制的所有行时，你可能希望返回含NULL值的行。

过滤数据时，一定要验证被过滤列中含NULL的行确实出现在返回的数据中。
