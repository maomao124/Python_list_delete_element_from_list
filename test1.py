"""
 * Project name(项目名称)：Python_list列表删除元素
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/22 
 * Time(创建时间)： 10:47
 * Version(版本): 1.0
 * Description(描述)：
根据目标元素所在位置的索引进行删除，可以使用 del 关键字或者 pop() 方法；
根据元素本身的值进行删除，可使用列表（list类型）提供的 remove() 方法；
将列表中所有元素全部删除，可使用列表（list类型）提供的 clear() 方法。

del：根据索引值删除元素
del 是 Python 中的关键字，专门用来执行删除操作，它不仅可以删除整个列表，还可以删除列表中的某些元素
del list name[index]
其中，list name 表示列表名称，index 表示元素的索引值。
del list name[start : end]
其中，start 表示起始索引，end 表示结束索引。del 会删除从索引 start 到 end 之间的元素，不包括 end 位置的元素。

pop()：根据索引值删除元素
Python pop() 方法用来删除列表中指定索引处的元素，具体格式如下：
list name.pop(index)
其中，list name 表示列表名称，index 表示索引值。如果不写 index 参数，默认会删除列表中的最后一个元素

remove()：根据元素值进行删除
除了 del 关键字，Python 还提供了 remove() 方法，该方法会根据元素本身的值来进行删除操作。
需要注意的是，remove() 方法只会删除第一个和指定值相同的元素，而且必须保证该元素是存在的，否则会引发 ValueError 错误。

clear()：删除列表所有元素
 """

if __name__ == '__main__':
    lang = ["Python", "C++", "Java", "PHP", "Ruby", "MATLAB"]
    print(lang)
    # 使用正数索引
    del lang[3]
    print(lang)
    # 使用负数索引
    del lang[-1]
    print(lang)
    lang1 = ["Python", "C++", "Java", "PHP", "Ruby", "MATLAB"]
    del lang1[2:4]
    print(lang1)
    lang2 = ["Python", "C++", "Java", "PHP", "Ruby", "MATLAB"]
    print(lang2.pop(2))
    print(lang2)
    print(lang2.pop())
    print(lang2)
    lang3 = ["Python", "C++", "Java", "PHP", "Ruby", "MATLAB"]
    lang3.remove("Java")
    print(lang3)

    lang3.clear()
    print(lang3)

    input()
