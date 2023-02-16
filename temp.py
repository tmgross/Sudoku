def sort(A):
    minimum = min(A)
    maximum = max(A)
    R = maximum - minimum

    count = list()
    for i in range(R):
        count[i] = 0

    for num in A:
        count[A[num]] += 1

    for i in range(1, R):
        count[i] += count[i - 1]

    sortedA = list()
    for i in range(len(A)):
        sortedA[count[A[i]] - 1] = A[i]
        count[A[i]] = count[A[i]] - 1

    return sortedA


def main():
    nums = [1,4,1,2,7,5,2]
    newNums = sort(nums)
    for i in newNums:
        print(newNums)