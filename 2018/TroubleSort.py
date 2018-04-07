
def troubleSort(L):
    done = False
    while(not done):
        done = True
        for i in range(0, len(L)-2):
            if(L[i] > L[i+2]):
                done = False
                tmp = L[i]
                L[i] = L[i+2]
                L[i+2] = tmp

def index(L):
    for i in range(0, len(L)-1):
        if(L[i] > L[i+1]):
            return i

    return -1

def notSolvable(L):
    for i in range(0, len(L)-2):
        if(L[i] > L[i+2]) and ((L[i] < L[i+1]) or (L[i+1] < L[i+2])):
            return True

def solve(L):
    troubleSort(L)
    return index(L)


T = int(input())
cases = []

for i in range(0, T):
    N = input()
    L = [int(k) for k in input().split(" ")]
    cases.append((N,L))

for i in range(0, T):
    (N, L) = cases[i]
    print(L)
    result = int(solve(L))
    print(L)
    base = "Case #" + str(i+1) + ": "
    if(result > -1):
        print(base + str(result))
    else:
        print(base + "OK")
    print()
