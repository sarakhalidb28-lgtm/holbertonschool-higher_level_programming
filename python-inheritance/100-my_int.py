Tasks
12. My integer
#advanced
Write a class MyInt that inherits from int:

MyInt is a rebel. MyInt has == and != operators inverted
You are not allowed to import any module
guillaume@ubuntu:~/$ cat 100-main.py
#!/usr/bin/python3
MyInt = __import__('100-my_int').MyInt

my_i = MyInt(3)
print(my_i)
print(my_i == 3)
print(my_i != 3)

guillaume@ubuntu:~/$ ./100-main.py
3
False
True
guillaume@ubuntu:~/$ 
No test cases needed

Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: python-inheritance
File: 100-my_int.py
Score of the task
