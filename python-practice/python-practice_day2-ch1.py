# Automate the Boring Stuff - Chapter 1
# Day 2 学习记录
# 进度: Storing Values in Variables

# ========== 第一部分: Basic Math Operators ==========
# Python 可以当计算器用

print(2 + 2)        # 加法
print(7 - 3)        # 减法
print(2 * 3)        # 乘法
print(22 / 7)       # 除法 (结果是小数 float)
print(22 // 7)      # 整除 (只保留整数部分)
print(22 % 7)       # 取余 (除完之后剩多少)
print(2 ** 3)       # 幂运算 (2 的 3 次方 = 8)


# ========== 第二部分: Order of Operations ==========
# 跟数学一样: 括号 > 幂 > 乘除 > 加减

print(2 + 3 * 6)        # = 20 (先算 3*6)
print((2 + 3) * 6)      # = 30 (括号优先)


# ========== 第三部分: Data Types ==========
# 三种基本类型:
# - 整数 (int):     42, -3, 0
# - 浮点数 (float): 3.14, -0.5, 2.0
# - 字符串 (str):   'hello', "world"

# 整数
age = 27

# 浮点数
pi = 3.14159

# 字符串 (单引号双引号都行)
name = '杨沙威'
city = "Brussels"


# ========== 第四部分: String Concatenation ==========
# 字符串拼接用 + 号
# 注意: 字符串和数字不能直接相加

greeting = 'Hello, ' + name
print(greeting)             # Hello, 杨沙威

# 字符串"乘以"数字 = 重复
print('Ha' * 3)             # HaHaHa


# ========== 第五部分: Storing Values in Variables ==========
# 变量 = 用来存值的"盒子"
# 起名规则:
#   1. 只能用字母、数字、下划线
#   2. 不能以数字开头
#   3. 区分大小写 (spam 跟 SPAM 是不同变量)
#   4. 不能用 Python 保留字 (比如 if, for, def)

# 赋值: 用 = 号
# 不是数学的"相等", 而是"把右边的值放到左边的盒子里"

spam = 40       # 把 40 放到名为 spam 的盒子里
print(spam)     # 40

# 变量可以被重新赋值
spam = 'Hello'  # 现在 spam 盒子里换成了字符串
print(spam)     # Hello

# 变量之间也可以赋值
eggs = spam     # 把 spam 盒子里的内容复制一份给 eggs
print(eggs)     # Hello


# ========== Day 2 学到这里 ==========
# 明天 (Day 3) 继续 Automate Ch.2: 流程控制 (if/else/for/while)
#
# 今天的感受:
# - Python 比想象的友好, 语法比较直觉
# - 看完 cookbook 后再看这些基础, 知道这些基础将来要拼成什么样的代码了
# - 学不动的时候停下来是对的, 强撑没用
