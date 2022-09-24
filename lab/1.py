
def array(lenght, start):
    arr = []
    for i in range(start, lenght, 2):
        arr.append(i)
    return arr
arr = array(15,10)
print(arr)
