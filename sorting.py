#Name: Kinz
#Date: 05/10/23
#Purpose: To sort and search specific values in a list

namelist=["Danny","Harlen","Adam","Jordan","Aiden","Austin","Jacob","Konnor","Senjou","Mayoi","Shinobu","Karen","Koyomi","Chihiro","Kanbaru"]




def bubbleSort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return

def binary_search(arr, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1

def search():
    search = input("Who would you like to search for: ")
    result = binary_search(namelist, 0, len(namelist)-1, search)
    if not result == -1:
        print(f"You have searched for: {search}\n {search} was found in: {result}")
    else:
        print(f"{search} was not found.")

def quit():
    quit = input("If you would like to exit enter a q: \n If you would like to continue")
    
    if quit == ("q"):
        exit()


run = True
while run:    
    
    bubbleSort(namelist)
    print(f'{namelist}')
    search()
    quit()
