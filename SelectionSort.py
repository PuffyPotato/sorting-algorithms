def SelectionSort(list):
    n = len(list)
    for i in range(n):
        for j in range(i+1, n):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]

lista = [int(i) for i in input().split()]
print(lista)
SelectionSort(lista)
print(lista)