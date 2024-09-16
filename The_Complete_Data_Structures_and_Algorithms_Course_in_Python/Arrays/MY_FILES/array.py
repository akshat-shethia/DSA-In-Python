import array

# 1.
a = array.array("i", [1, 2, 3, 4, 5])
for i in a:
    print(i, end=" ")


print("")
print("-" * 100)

# 2.
for i in range(len(a)):
    print(f"{i+1}th element is ----> {a[i]}")

print("")
print("-" * 100)

# 3.
a.append(99)
for i in range(len(a)):
    print(f"{i+1}th element is ----> {a[i]}")

print("")
print("-" * 100)

# 4.
a.insert(1, 100)
for i in range(len(a)):
    print(f"{i+1}th element is ----> {a[i]}")

print("")
print("-" * 100)

# 5.
a2 = array.array("i", [6, 7, 8, 9])
a.extend(a2)
for i in range(len(a)):
    print(f"{i+1}th element is ----> {a[i]}")

print("")
print("-" * 100)

# 7.
a.remove(99)
for i in range(len(a)):
    print(f"{i+1}th element is ----> {a[i]}")

print("")
print("-" * 100)

# 8.
x = a.pop()
for i in range(len(a)):
    print(f"{i+1}th element is ----> {a[i]}")

print(f"The Popped Element is ----> {x}")

print("")
print("-" * 100)

# 9.
x = a.index(1)
for i in range(len(a)):
    print(f"{i+1}th element is ----> {a[i]}")

print(f"The Index of 1 is -----> {x}")
print("")
print("-" * 100)

# 10.
a.reverse()
for i in range(len(a)):
    print(f"{i+1}th element is ----> {a[i]}")

print("")
print("-" * 100)

# 11.
print(a.buffer_info())

print("")
print("-" * 100)

# 12.
x = a.count(1)
for i in range(len(a)):
    print(f"{i+1}th element is ----> {a[i]}")

print(f"The Count of 1 is -----> {x}")

print("")
print("-" * 100)

# 13.
x = a.tobytes()
for i in range(len(a)):
    print(f"{i+1}th element is ----> {a[i]}")

print(f"The string conversion is -----> {x}")

print("")
print("-" * 100)

# 12.
x = a.count(1)
for i in range(len(a)):
    print(f"{i+1}th element is ----> {a[i]}")

print(f"The Count of 1 is -----> {x}")

print("")
print("-" * 100)
