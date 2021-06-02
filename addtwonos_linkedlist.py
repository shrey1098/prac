str = "abcabcbb"
copy_str = ""
count = 0
repetitions = []
for i in range(len(str)):
    x = str[i]
    count += 1
    copy_str =  str[i+1:]
    for y in copy_str:
        if x == y:
            key = (i, copy_str.index(y)+count)
            repetitions.append(key)
            break

if len(repetitions) == 0:
    print(len(str))
else:
    for i,j in repetitions:
        if i +1 == j:
            repetitions.remove((i,j))
            repetitions.append((j, len(str)))
print(repetitions)
maxval = {}
count=0
for i, j in repetitions:
    count =+1
    list = ([k in str[str.index(k)+1:j] and k != str[str.index(k)+1] for k in str[i:j]])
    print(list)

    if all(element == False for element in list):
        maxval[(i,j)] = j-i
if len(maxval) == 0:
    print(0)
else:
    final = max(maxval, key=maxval.get)
    fin = final[1] - final[0]
    print(fin)