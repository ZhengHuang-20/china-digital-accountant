# 可以使用Python中内置的函数对变量类型进行转换。

# int()：将一个数值或字符串转换成整数，可以指定进制。
# float()：将一个字符串转换成浮点数。
# str()：将指定的对象转换成字符串形式，可以指定编码。
# chr()：将整数转换成该编码对应的字符串（一个字符）。
# ord()：将字符串（一个字符）转换成对应的编码（整数）。


"""
下面是对Python中内置的函数对变量类型转换应用案例
财务计算：利息和本金的计算
计算存款在特定期限和利率下的利息和本金总和

Version: 0.1
Author: huangzheng
"""

# 获取用户输入
principal = float(input('请输入本金（如：10000）: '))
rate = float(input('请输入年利率（如：0.03）: '))
years = int(input('请输入存款年限（如：5）: '))

# 计算利息和本金总和
total_interest = principal * rate * years
final_amount = principal + total_interest

# 输出计算结果
print(f'总利息为: {total_interest:.2f}')
print(f'本金和利息总和为: {final_amount:.2f}')
