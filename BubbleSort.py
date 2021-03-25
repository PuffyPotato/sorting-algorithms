def BubbleSort(list):
    n = len(list)
    for i in range(n):
        swapped = False
        for j in range(0, n-1-i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                swapped = True
        else:
            if not swapped:
                break


f = open('tests/A/100.in')
lista = [int(i) for i in f]

BubbleSort(lista)
print(lista)

