def missingnum(arr):
    step1_sum = sum(arr) #12
    l = len(arr) #4
    step2_total = (l + 1) * (l + 2)/2 #15
    return step2_total - step1_sum

arr = [1,2,3,4,5,6,8,9,10]
print(missingnum(arr))