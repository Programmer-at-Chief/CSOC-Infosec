"""
Six sorting algorithms have been used :
1. Bubble Sort
2. Insertion Sort
3. Selection Sort
4. Merge Sort
5. Quick Sort
6. Bogo Sort
Some useful information such as the time and space Complexity of all the algorithms have been displayed alongside 
as well
"""

import random as rand
import copy
import time
import os

# This surt class holds all the sorting codes for the program , but the class methods are not called directly but 
# through another class acting as a mediator to perform other functions in between
class Surt:
    def __init__(self):
        self.clearScreen()
        print('-'*40)
        print('''
        ░█──░█ █▀▀ █── █▀▀ █▀▀█ █▀▄▀█ █▀▀ 　 ▀▀█▀▀ █▀▀█ 　 ░█▀▀▀█ █──█ █▀▀█ ▀▀█▀▀ █ █ 
        ░█░█░█ █▀▀ █── █── █──█ █─▀─█ █▀▀ 　 ──█── █──█ 　 ─▀▀▀▄▄ █──█ █▄▄▀ ──█── ▀ ▀ 
        ░█▄▀▄█ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀───▀ ▀▀▀ 　 ──▀── ▀▀▀▀ 　 ░█▄▄▄█ ─▀▀▀ ▀─▀▀ ──▀── ▄ ▄''')
        print('-'*40)
        print('''Enter \n-1 -> To take a new array \n0 -> To exit \n1 -> To try bubble sort \n2 -> To try insertion sort \n3 -> To try selection sort \n4 -> To try merge sort \n5 -> To try quick sort \n6 -> To try bogo sort\n7 -> To try and compare all the sorting''')

    def clearScreen(self):
        if (os.name == 'nt'):
            os.system("cls")
        else:
            os.system("clear")
    def bubble_sort(self,arr,n):
        for i in range(n-1):
            sorted=False
            for j in range(0,n-i-1):
                if (arr[j]>arr[j+1]):
                    arr[j],arr[j+1]=arr[j+1],arr[j]
                    sorted=True
            if (not sorted):
                return

    def insertion_sort(self,arr,n):
        for i in range(1,n):
            j=i
            while(j>0 and arr[j]<arr[j-1]):
                arr[j],arr[j-1]=arr[j-1],arr[j]
                j-=1

    def selection_sort(self,arr,n):
        for i in range(n-1):
            minimum=i
            for j in range(i+1,n):
                if (arr[j]<=arr[minimum]):
                    minimum=j
            arr[i],arr[minimum]=arr[minimum],arr[i]

    def merge(self,arr,start,end):
        mid=(start+end)//2
        l1=mid-start+1
        l2=end-mid
        arr1=arr[start:mid+1]
        arr2=arr[mid+1:]
        index=start
        i=0
        j=0
        while(i<l1 and j<l2):
            if (arr1[i]<arr2[j]):
                arr[index]=arr1[i]
                index+=1
                i+=1
            else:
                arr[index]=arr2[j]
                index+=1
                j+=1
        while(i<l1):
            arr[index]=arr1[i]
            index+=1
            i+=1
        while(j<l2):
            arr[index]=arr2[j]
            index+=1
            j+=1

    def merge_sort(self,arr,start,end):
        if (start>=end):
            return
        mid=(start+end)//2
        self.merge_sort(arr,start,mid)
        self.merge_sort(arr,mid+1,end)
        self.merge(arr,start,end)

    def quick(self,arr,start,end):
        count=0
        for i in range(start+1,end+1):
            if (arr[i]<=arr[start]):
                count+=1
        arr[start],arr[start+count]=arr[start+count],arr[start]
        index=start+count
        element=arr[index]
        i=start
        j=end
        while (i<index and j>index):
            while (arr[i]<=element and i<index):
                i+=1
            while (arr[j]>element and j>index):
                j-=1
            if (i<index and j>index):
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
                j-=1
        return index

    def quick_sort(self,arr,start,end):
        if (start>=end):
            return
        index=self.quick(arr,start,end)
        self.quick_sort(arr,start,index-1)
        self.quick_sort(arr,index+1,end)
        return

    def shuffle(self,arr):
        for i in range(len(arr)):
            num=rand.randrange(0,len(arr))
            arr[i],arr[num]=arr[num],arr[i]

    def check(self,arr):
        for i in range(len(arr)-1):
            if (arr[i]>arr[i+1]):
                return False
        return True

    def bogo_sort(self,arr):
        while(not self.check(arr)):
            self.shuffle(arr)
    def end(self):
        print("Thanks for trying Surt !!")
        exit()

sort=Surt()
"""
This SurtGame class acts as a mediator for the sorting functions by performing the more important functions such as 
managing the output and also calculating the time taken by the sorting algorithms for good comparisions
"""

class SurtGame:
    def __init__(self):
        pass
    def doBubbleSort(self,arr,n):
        start_time = time.time()
        print("Initial Array : ",end="")
        for i in arr:
            print(i,end=" ")
        print()
        sort.bubble_sort(arr,n)
        print("Final Array : ",end="")
        for i in arr:
            print(i,end=" ")
        print()
        end_time = time.time()
        execution_time = end_time - start_time
        print("Time taken by Bubble Sort is ",f"{execution_time:.4e}")
        print("-"*40)
    def doInsertionSort(self,arr,n):
        start_time = time.time()
        print("Initial Array : ",end="")
        for i in arr:
            print(i,end=" ")

        print()
        sort.insertion_sort(arr,n)
        print("Final Array : ",end="")
        for i in arr:
            print(i,end=" ")

        print()
        end_time = time.time()
        execution_time = end_time - start_time
        print("Time taken by Insertion Sort is ",f"{execution_time:.4e}")
        print("-"*40)
    def doSelectionSort(self,arr,n):
        start_time = time.time()
        print("Initial Array : ",end="")
        for i in arr:
            print(i,end=" ")

        print()
        sort.selection_sort(arr,n)
        print("Final Array : ",end="")
        for i in arr:
            print(i,end=" ")

        print()
        end_time = time.time()
        execution_time = end_time - start_time
        print("Time taken by Selection Sort is ",f"{execution_time:.4e}")
        print("-"*40)
    def doMergeSort(self,arr,n):
        start_time = time.time()
        print("Initial Array : ",end="")
        for i in arr:
            print(i,end=" ")
        print()

        sort.merge_sort(arr,0,n-1)
        print("Final Array : ",end="")
        for i in arr:
            print(i,end=" ")
        print()

        end_time = time.time()
        execution_time = end_time - start_time
        print("Time taken by Merge Sort is ",f"{execution_time:.4e}")
        print("-"*40)
    def doQuickSort(self,arr,n):
        start_time = time.time()
        print("Initial Array : ",end="")
        for i in arr:
            print(i,end=" ")
        print()

        sort.quick_sort(arr,0,n-1)
        print("Final Array : ",end="")
        for i in arr:
            print(i,end=" ")
        print()

        end_time = time.time()
        execution_time = end_time - start_time
        print("Time taken by Quick Sort is ",f"{execution_time:.4e}")
        print("-"*40)
    def doBogoSort(self,arr,n):
        start_time = time.time()
        print("Initial Array : ",end="")
        for i in arr:
            print(i,end=" ")
        print()

        sort.bogo_sort(arr)
        print("Final Array : ",end="")
        for i in arr:
            print(i,end=" ")
        print()

        end_time = time.time()
        execution_time = end_time - start_time
        print("Time taken by Bogo Sort is ",f"{execution_time:.4e}")
        print("-"*40)

game=SurtGame()
try:
    choice=int(input("Enter your choice : "))
except:
    print("Invalid Input")
    choice=int(input("Enter your choice : "))

while (choice==-1):
    print("No array has been initialised till now , so please choose an appropriate option.")
    choice=int(input("Enter your choice : "))

while (choice <=-2 or choice >=8):
    print('Invalid Choice ')
    choice=int(input("Enter your choice : "))

if (choice==0):
    sort.end()
n=int(input("Enter size of Array : "))
print("Enter the array with spaces between numbers : ",end="")
str=input("")
arr=[int(i) for i in str.split(" ")]

"""
This is the starting point of the program 
Ascii art fonts have been used to cater to the eye candy needs of the program
"""
while(True):
    if (choice==-1):
        sort.clearScreen()
        n=int(input("Enter size of Array : "))
        print("Enter the array with spaces between numbers : ",end="")
        str=input("")
        arr=[int(i) for i in str.split(" ")]
        print("New array has been initialised !!")
    elif (choice==0):
        sort.end()
    elif (choice==1):
        sort.clearScreen()
        print("*"*40)
        print('''
╭━━╮╱╱╱╭╮╱╭╮╱╭╮╱╱╱╱╭━━━╮╱╱╱╱╭╮
┃╭╮┃╱╱╱┃┃╱┃┃╱┃┃╱╱╱╱┃╭━╮┃╱╱╱╭╯╰╮
┃╰╯╰┳╮╭┫╰━┫╰━┫┃╭━━╮┃╰━━┳━━┳┻╮╭╯
┃╭━╮┃┃┃┃╭╮┃╭╮┃┃┃┃━┫╰━━╮┃╭╮┃╭┫┃
┃╰━╯┃╰╯┃╰╯┃╰╯┃╰┫┃━┫┃╰━╯┃╰╯┃┃┃╰╮
╰━━━┻━━┻━━┻━━┻━┻━━╯╰━━━┻━━┻╯╰━╯''')
        print("*"*40)

        print("**Time Complexity:** O(n^2) in both average and worst cases.")
        print("**Space Complexity:** O(1), because only a single additional memory space is required.")
        print("-"*40)
        arr1=copy.deepcopy(arr)
        game.doBubbleSort(arr1,n)
    elif (choice==2):
        sort.clearScreen()
        print("*"*40)
        print('''
╭━━╮╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╭━━━╮╱╱╱╱╭╮
╰┫┣╯╱╱╱╱╱╱╱╱╱╭╯╰╮╱╱╱╱╱╱╱┃╭━╮┃╱╱╱╭╯╰╮
╱┃┃╭━╮╭━━┳━━┳┻╮╭╋┳━━┳━╮╱┃╰━━┳━━┳┻╮╭╯
╱┃┃┃╭╮┫━━┫┃━┫╭┫┃┣┫╭╮┃╭╮╮╰━━╮┃╭╮┃╭┫┃
╭┫┣┫┃┃┣━━┃┃━┫┃┃╰┫┃╰╯┃┃┃┃┃╰━╯┃╰╯┃┃┃╰╮
╰━━┻╯╰┻━━┻━━┻╯╰━┻┻━━┻╯╰╯╰━━━┻━━┻╯╰━╯''')
        print("*"*40)
        print("**Time Complexity:** O(n^2) in the worst case, but O(n) in the best case when the array is already sorted.")
        print("**Space Complexity:** O(1), as it only needs a constant amount of extra space.")
        print("-"*40)
        arr1=copy.deepcopy(arr)
        game.doInsertionSort(arr1,n)
    elif (choice ==3):
        sort.clearScreen()
        print("*"*40)
        print('''
╭━━━╮╱╱╭╮╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╭━━━╮╱╱╱╱╭╮
┃╭━╮┃╱╱┃┃╱╱╱╱╱╭╯╰╮╱╱╱╱╱╱╱┃╭━╮┃╱╱╱╭╯╰╮
┃╰━━┳━━┫┃╭━━┳━┻╮╭╋┳━━┳━╮╱┃╰━━┳━━┳┻╮╭╯
╰━━╮┃┃━┫┃┃┃━┫╭━┫┃┣┫╭╮┃╭╮╮╰━━╮┃╭╮┃╭┫┃
┃╰━╯┃┃━┫╰┫┃━┫╰━┫╰┫┃╰╯┃┃┃┃┃╰━╯┃╰╯┃┃┃╰╮
╰━━━┻━━┻━┻━━┻━━┻━┻┻━━┻╯╰╯╰━━━┻━━┻╯╰━╯''')
        print("*"*40)
        print("**Time Complexity:** O(n^2) in both average and worst cases.")
        print("**Space Complexity:** O(1), similar to bubble sort, it requires minimal additional space.")

        print("-"*40)
        arr1=copy.deepcopy(arr)
        game.doSelectionSort(arr1,n)
    elif (choice==4):
        sort.clearScreen()
        print("*"*40)
        print('''
╭━╮╭━╮╱╱╱╱╱╱╱╱╱╱╱╭━━━╮╱╱╱╱╭╮
┃┃╰╯┃┃╱╱╱╱╱╱╱╱╱╱╱┃╭━╮┃╱╱╱╭╯╰╮
┃╭╮╭╮┣━━┳━┳━━┳━━╮┃╰━━┳━━┳┻╮╭╯
┃┃┃┃┃┃┃━┫╭┫╭╮┃┃━┫╰━━╮┃╭╮┃╭┫┃
┃┃┃┃┃┃┃━┫┃┃╰╯┃┃━┫┃╰━╯┃╰╯┃┃┃╰╮
╰╯╰╯╰┻━━┻╯╰━╮┣━━╯╰━━━┻━━┻╯╰━╯
╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╰━━╯''')
        print("*"*40)
        print("**Time Complexity:** O(n log n) in all cases (best, average, and worst).")
        print("**Space Complexity:** O(n), because it requires additional space to hold one half of the data during the merge process.")
        print("-"*40)
        arr1=copy.deepcopy(arr)
        game.doMergeSort(arr1,n)
    elif (choice==5):
        sort.clearScreen()
        print("*"*40)
        print('''
╭━━━╮╱╱╱╱╱╱╭╮╱╱╭━━━╮╱╱╱╱╭╮
┃╭━╮┃╱╱╱╱╱╱┃┃╱╱┃╭━╮┃╱╱╱╭╯╰╮
┃┃╱┃┣╮╭┳┳━━┫┃╭╮┃╰━━┳━━┳┻╮╭╯
┃┃╱┃┃┃┃┣┫╭━┫╰╯╯╰━━╮┃╭╮┃╭┫┃
┃╰━╯┃╰╯┃┃╰━┫╭╮╮┃╰━╯┃╰╯┃┃┃╰╮
╰━━╮┣━━┻┻━━┻╯╰╯╰━━━┻━━┻╯╰━╯
╱╱╱╰╯''')
        print("*"*40)
        print("**Time Complexity:** O(n log n) in the average case, but O(n^2) in the worst case (when the pivot selection is poor).")
        print("**Space Complexity:** O(log n) due to the recursive call stack.")
        print("-"*40)
        arr1=copy.deepcopy(arr)
        game.doQuickSort(arr1,n)
    elif (choice==6):
        sort.clearScreen()
        print("*"*40)
        print('''
╭━━╮╱╱╱╱╱╱╱╱╱╱╭━━━╮╱╱╱╱╭╮
┃╭╮┃╱╱╱╱╱╱╱╱╱╱┃╭━╮┃╱╱╱╭╯╰╮
┃╰╯╰┳━━┳━━┳━━╮┃╰━━┳━━┳┻╮╭╯
┃╭━╮┃╭╮┃╭╮┃╭╮┃╰━━╮┃╭╮┃╭┫┃
┃╰━╯┃╰╯┃╰╯┃╰╯┃┃╰━╯┃╰╯┃┃┃╰╮
╰━━━┻━━┻━╮┣━━╯╰━━━┻━━┻╯╰━╯
╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╰━━╯''')
        print("*"*40)
        print("**Time Complexity:** O((n+1)!), where n is the number of elements being sorted")
        print("**Space Complexity:** O(n), which refers to the additional space required for the temporary storage.")
        print("-"*40)
        arr1=copy.deepcopy(arr)
        game.doBogoSort(arr1,n)
    elif (choice ==7):
        sort.clearScreen()
        print("*"*40)
        print('''
▄▀█ █░░ █░░   █▀ █▀█ █▀█ ▀█▀ █▀   █ █
█▀█ █▄▄ █▄▄   ▄█ █▄█ █▀▄ ░█░ ▄█   ▄ ▄''')
        print("*"*40)
        arr1=copy.deepcopy(arr)
        start_time = time.time()
        print("Initial Array : ",end="")
        for i in arr:
            print(i,end=" ")
        print()
        sort.bubble_sort(arr1,n)
        print("Final Array : ",end="")
        for i in arr1:
            print(i,end=" ")
        print()
        end_time = time.time()
        execution_time = end_time - start_time
        print("-"*40)
        print("Time taken by Bubble Sort is ",f"{execution_time:.4e}")
        print("-"*40)

        arr1=copy.deepcopy(arr)
        start_time = time.time()
        sort.insertion_sort(arr1,n)
        end_time = time.time()
        execution_time = end_time - start_time
        print("Time taken by Insertion Sort is ",f"{execution_time:.4e}")
        print("-"*40)


        arr1=copy.deepcopy(arr)
        start_time = time.time()
        sort.selection_sort(arr1,n)
        end_time = time.time()
        execution_time = end_time - start_time
        print("Time taken by Selection Sort is ",f"{execution_time:.4e}")
        print("-"*40)


        arr1=copy.deepcopy(arr)
        start_time = time.time()
        sort.merge_sort(arr1,0,n-1)
        end_time = time.time()
        execution_time = end_time - start_time
        print("Time taken by Merge Sort is ",f"{execution_time:.4e}")
        print("-"*40)


        arr1=copy.deepcopy(arr)
        start_time = time.time()
        sort.quick_sort(arr1,0,n-1)
        end_time = time.time()
        execution_time = end_time - start_time
        print("Time taken by Quick Sort is ",f"{execution_time:.4e}")
        print("-"*40)


        arr1=copy.deepcopy(arr)
        start_time = time.time()
        sort.bogo_sort(arr1)
        end_time = time.time()
        execution_time = end_time - start_time
        print("Time taken by Bogo Sort is ",f"{execution_time:.4e}")
        print("-"*40)



    print('''Enter \n-1 -> To take a new array \n0 -> To exit \n1 -> To try bubble sort \n2 -> To try insertion sort \n3 -> To try selection sort \n4 -> To try merge sort \n5 -> To try quick sort \n6 -> To try bogo sort\n7 -> To try and compare all the sorting''')
    try:
        choice=int(input("Enter your choice : "))
    except:
        print("Invalid Input")
        choice=int(input("Enter your choice : "))

    while (choice <=-2 or choice >=8):
        print('Invalid Choice ')
        choice=int(input("Enter your choice : "))

