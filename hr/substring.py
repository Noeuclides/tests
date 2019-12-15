head_string = 'efghi'
lean_head_string = len(head_string)
list_substring = []
count = 1
while lean_head_string >= 1:
    print('Head -->', head_string)
    for i in range(0, len(head_string)):
        list_substring.append(head_string[:i+1])
    lean_head_string -= 1
    print(lean_head_string)
    head_string = head_string[count:]
    print('Count ', count)
    print(list_substring)