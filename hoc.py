import random
s1 = "hello"
s2 = "world"
char_to_find = 'o'
current_string = random.choice([s1, s2])

i = 0
while i < len(current_string):
    if current_string[i] == char_to_find:
        print(f"Tìm thấy chữ '{char_to_find}' trong chuỗi '{current_string}' tại vị trí {i}")
        break
    i += 1

if i == len(current_string):
    print(f"Không tìm thấy chữ '{char_to_find}' trong chuỗi '{current_string}'.")