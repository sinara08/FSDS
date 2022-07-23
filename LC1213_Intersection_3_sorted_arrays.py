def intersect_array(n1, n2, n3, arr1, arr2, arr3):
    i=j=k = 0
    rslt_arr = []

    while i < n1 and j < n2 and k < n3:
        if arr1[i] == arr2[j] == arr3[k]:
            rslt_arr.append(arr1[i])
            i += 1
            j += 1
            k += 1

        else:
            if arr1[i] < arr2[j] or arr1[i] < arr3[k]:
                i+=1
            elif arr2[j] < arr1[i] or arr2[j] < arr3[k]:
                j+=1
            else:
                k+=1

    return rslt_arr



arr1=input("enter number of elements:" )
arr1 = list(map(int,arr1.split(',')))
arr2=input("Enter number of elements: " )
arr2 = list(map(int,arr2.split(',')))
arr3=input("Enter number of elements: ")
arr3 = list(map(int,arr3.split(',')))
n1=len(arr1)
n2=len(arr2)
n3=len(arr3)

print(intersect_array(n1, n2, n3, arr1, arr2, arr3))
