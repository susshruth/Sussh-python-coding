items=[5,6,4,8]

input1=eval(input("type num to get factorial"))

def sort(set):
    if len(set)>1:
        mid=len(set) // 2
        leftarray=set[:mid]
        rightarray=set[mid:]

        sort(leftarray)
        sort(rightarray)

        i=0 # index into the left array
        j=0 # index into the right array
        k=0 # index into merged array

        # while both arrays have content
        while i < len(leftarray) and j < len(rightarray):
            if leftarray[i] < rightarray[j]:
                set[k] = leftarray[i]
                i += 1
            else:
                set[k] = rightarray[j]
                j += 1
            k += 1

        # if the left array still has values, add them
        while i < len(leftarray):
            set[k] = leftarray[i]
            i += 1
            k += 1

        # if the right array still has values, add them
        while j < len(rightarray):
            set[k] = rightarray[j]
            j += 1
            k += 1

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
    
print("the factorial for {} is {}".format(input1, factorial(input1)))    
    
print(items)
sort(items)
print(items)
