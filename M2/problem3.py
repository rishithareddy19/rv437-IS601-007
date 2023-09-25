a1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
a2 = [-1, 1, -2, 2, 3, -3, -4, 5]
a3 = [-0.01, -0.0001, -.15]
a4 = ["-1", "2", "-3", "4", "-5", "5", "-6", "6", "-7", "7"]


def process_array(num, arr):
    print("\nProcessing Array({}): \n\n".format(num))
    print(arr)
    print("\nPositive Output:\n")
    #rv437
    # TODO add new code here to print the desired result 
    arr1=[]
    arr2=[]
    for i in arr:
        if type(i) == str:
            i= int(i)
            arr1.append(i);
        else:
            arr1.append(i);
    for i in arr1:
        if i< 0:
            i=i * (-1);
            arr2.append(i);
        else:
            arr2.append(i);

    print(arr2)
print("Problem 3")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)