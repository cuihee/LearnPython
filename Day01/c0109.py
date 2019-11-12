"""
 这些运算符都怎么用，什么意思
"""
'''
==
!=
>
>=
<
<=

=
+=
-=
*=
/=
%=
**=
//=

位运算
&
|
^
~
<<
>>

逻辑运算
and
or
not

成员
in
not in

身份运算
is
is not



'''

# 关于 is 和 ==
a = [1, 2, 3]
print("b是a的另一个名字")
b = a
print(b is a)
print(b == a)

print("b是a的复制体")
b = a[:]
print(b is a)
print(b == a)
