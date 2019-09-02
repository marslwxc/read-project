def array(array1, array2):
    index1, index2 = 0, 0
    result = []
    while index1 < len(array1) and index2 < len(array2):
        if array1[index1] <= array2[index2]:
            result.append(array1[index1])
            index1 += 1
        else:
            result.append(array2[index2])
            index2 += 1
    result += array1[index1:]
    result += array2[index2:]
    return result

if __name__ == "__main__":
    array1 = [1,3,5,6,8,9]
    array2 = [2,3,5,8,10]
    result = array(array1, array2)
    print(result)