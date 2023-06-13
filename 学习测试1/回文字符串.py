def is_plalindrome(string):
  string = list(string)
  length = len(string)
  left = 0
  right = length - 1
  while left < right:
    if string[left] != string[right]:
      print("不是回文字符串")

    left += 1
    right -= 1
    print("是回文字符串")

s = input("请输入字符串：")
is_plalindrome(s)