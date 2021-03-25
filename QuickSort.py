def QuickSort(list, start, end):
    pivot = list[(start+end)//2]
    i = start
    j = end
    while i <= j:
        while list[i] < pivot:
            i+=1
        while list[j] > pivot:
            j-=1
        if i <= j:
            list[i], list[j] = list[j], list[i]
            i+=1
            j-=1
    if i < end:
        QuickSort(list, i, end)
    if j > start:
        QuickSort(list, start, j)


lista = [int(i) for i in input().split()]

print(lista)
QuickSort(lista, 0, len(lista)-1)
print(lista)






