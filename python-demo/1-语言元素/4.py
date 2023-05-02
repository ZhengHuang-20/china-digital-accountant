"""
运算符

Python支持多种运算符，下表大致按照优先级从高到低的顺序列出了所有的运算符，运算符的优先级指的是多个运算符同时出现时，先做什么运算然后再做什么运算。除了我们之前已经用过的赋值运算符和算术运算符，我们稍后会陆续讲到其他运算符的使用。

| 运算符                                                       | 描述                           |
| ------------------------------------------------------------ | ------------------------------ |
| `[]` `[:]`                                                   | 下标，切片                     |
| `**`                                                         | 指数                           |
| `~` `+` `-`                                                  | 按位取反, 正负号               |
| `*` `/` `%` `//`                                             | 乘，除，模，整除               |
| `+` `-`                                                      | 加，减                         |
| `>>` `<<`                                                    | 右移，左移                     |
| `&`                                                          | 按位与                         |
| `^` `\|`                                                      | 按位异或，按位或               |
| `<=` `<` `>` `>=`                                            | 小于等于，小于，大于，大于等于 |
| `==` `!=`                                                    | 等于，不等于                   |
| `is`  `is not`                                               | 身份运算符                     |
| `in` `not in`                                                | 成员运算符                     |
| `not` `or` `and`                                             | 逻辑运算符                     |
| `=` `+=` `-=` `*=` `/=` `%=` `//=` `**=` `&=` `|=` `^=` `>>=` `<<=` | （复合）赋值运算符             |


说明： 在实际开发中，如果搞不清楚运算符的优先级，可以使用括号来确保运算的执行顺序。
"""


"""
财务计算：投资回报和税收计算
使用所有Python运算符进行财务计算

Version: 0.1
Author: huangzheng
"""

# 用户输入
initial_investment = float(input('请输入初始投资额（如：10000）: '))
annual_growth_rate = float(input('请输入年增长率（如：0.1）: '))
investment_years = int(input('请输入投资年限（如：5）: '))
annual_tax_rate = float(input('请输入年税收率（如：0.2）: '))

# 计算未来价值和税收
future_value = initial_investment * (1 + annual_growth_rate) ** investment_years
taxes = (future_value - initial_investment) * annual_tax_rate

# 调整未来价值，减去税收
future_value_after_tax = future_value - taxes

# 输出结果
print(f'未来价值（不含税）: {future_value:.2f}')
print(f'税收: {taxes:.2f}')
print(f'未来价值（含税）: {future_value_after_tax:.2f}')

# 使用比较运算符进行比较
initial_investment_doubled = initial_investment * 2
if future_value_after_tax > initial_investment_doubled:
    print('未来价值（含税）大于初始投资翻倍。')
else:
    print('未来价值（含税）未达到初始投资翻倍。')

# 使用逻辑运算符检查投资是否达到某个目标
target_value = float(input('请输入您的目标价值（如：30000）: '))
is_target_reached = future_value_after_tax >= target_value
print(f'达到目标价值: {is_target_reached}')

# 使用位运算符进行二进制计算（仅用于演示）
initial_investment_binary = int(initial_investment)
binary_result = initial_investment_binary & int(annual_growth_rate * 100)
print(f'二进制计算结果（仅用于演示）: {binary_result}')
