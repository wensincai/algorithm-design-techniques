def find_left_boundary(A, left, right, X):
	if left < right:
		mid = (left + right) // 2
		if X == A[mid]:
			return mid
		if A[mid] > X:
			return find_left_boundary(A, left, mid - 1, X)
		else:
			return find_left_boundary(A, mid + 1, right, X)
	else:
		if A[left] < X:
			return left
		else:
			return left

A=[1, 3, 4, 6, 8, 10, 14, 18, 25, 27, 29, 45]
X = find_left_boundary(A, 0, len(A)-1, 28)
print A[X]
