def linear_search(arr, e):
    for i, elt in enumerate(arr):
        if elt == e:
            return i

    return "Element not in List"


arr = [1, 2, 3, 4, 5]
print(linear_search(arr, 5))
