def insertion_sort(a):
    for i in range (1,len(a)):
     j = i-1
     while j >= 0 and a[j] > a[j+1]:
        temp = a[j+1]
        a[j + 1] = a[j]
        a[j] = temp
        j = j - 1
    return a

a = [50,23,67,48,90,56,43]
print (insertion_sort(a))
