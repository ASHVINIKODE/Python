def printJobScheduling(arr, t):
   
    arr.sort(key=lambda x: x[2], reverse=True)

   
    result = [False] * t

  
    job = ['-1'] * t


    for i in range(len(arr)):
       
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
            if not result[j]:
                result[j] = True
                job[j] = arr[i][0]
                break

    print("Job sequence:", job)


if __name__ == '__main__':
    arr = [
        ['a', 2, 100],  
        ['b', 1, 19],
        ['c', 2, 27],
        ['d', 1, 25],
        ['e', 3, 15]
    ]

    print("Following is the maximum profit sequence of jobs:")
    printJobScheduling(arr, 3)
