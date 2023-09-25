a1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
a2 = [-1, 1, -2, 2, 3, -3, -4, 5]
a3 = [-0.01, -0.0001, -.15]
a4 = ["-1", "2", "-3", "4", "-5", "5", "-6", "6", "-7", "7"]

def process_array(num, arr):
    print("\nProcessing Array({}): \n\n".format(num))
    print(arr)
    print("\nPositive Output:\n")
    #rv437 - 09/25/2023 
    # It takes a number and an array as input, prints the array, and then prints the absolute values of the elements in the array along with their types.
    # TODO add new code here to print the desired result 
    a2=[]
    for i in arr:
        if isinstance(i,str):
            i = abs(int(i))
            i=str(i)
        else:
            i=abs(i)
        a2.append(i)
    for j in a2:
        print(f"{j} , Type: {type(j)}")
print("Problem 3")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)