import sys
import math
import collections
import heapq
from itertools import permutations, combinations, product
from functools import lru_cache

# Fast Input / Output
input = sys.stdin.read
def I(): return int(input().strip())
def IS(): return input().strip()
def M(): return map(int, input().split())
def L(): return list(map(int, input().split()))
def LS(): return list(input().split())

# Constants
MOD = 10**9 + 7
INF = float('inf')
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Directions for grid movement (right, down, left, up)

# Fast Exponentiation
def fast_pow(base, exp, mod=MOD):
    result = 1
    while exp:
        if exp % 2:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

# Modular Inverse using Fermat's Little Theorem
def mod_inv(a, p=MOD):
    return fast_pow(a, p - 2, p)

# GCD and LCM
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

# Sieve of Eratosthenes for Prime Numbers
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return [x for x in range(n + 1) if is_prime[x]]

# Prime Factorization
def prime_factors(n):
    factors = []
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors

# Combinatorics (Factorial and nCr)
fact = [1] * (10**6 + 1)
def precompute_factorials(limit, mod=MOD):
    for i in range(2, limit+1):
        fact[i] = fact[i-1] * i % mod

def nCr(n, r, mod=MOD):
    if r > n: return 0
    return fact[n] * mod_inv(fact[r], mod) * mod_inv(fact[n-r], mod) % mod

# Binary Search
def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Graph Utilities (BFS, DFS, Dijkstra)
def bfs(graph, start):
    visited = set()
    queue = collections.deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

def dfs(graph, node, visited=set()):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def dijkstra(graph, start):
    dist = {node: INF for node in graph}
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            new_dist = d + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    return dist

# Sorting Utilities
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# Disjoint Set Union (Union-Find)
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

# Miscellaneous Utilities
def is_palindrome(s):
    return s == s[::-1]

def reverse_string(s):
    return s[::-1]

def rotate_array(arr, k):
    k %= len(arr)
    return arr[-k:] + arr[:-k]

def print_grid(grid):
    for row in grid:
        print(' '.join(map(str, row)))

# Main
def main():
    # Code here
    pass

if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    main()
