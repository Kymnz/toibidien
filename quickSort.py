def quick_sort(sequence):
    leght = len(sequence)
    if leght <= 1:
        return sequence
    else:
        pivot = sequence.pop()

        items_greater = []
        items_lower = []
    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)
print(quick_sort([1,5,515,16,9,8,5,11,51,65165,1,6]))