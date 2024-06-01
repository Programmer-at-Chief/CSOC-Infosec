#include<bits/stdc++.h>
using namespace std;

void Shuffle(int* arr,int n){
  for (int i=0;i<n;i++){
    swap(arr[i],arr[rand()%n]);
  }
}

bool checkSorted(int *arr,int n){
  for (int i=0;i<n-1;i++){
    if (arr[i]>arr[i+1]){
      return false;
    }
  }
  return true;
}


void printArray(int *arr,int n){
  cout << "Array : ";
  for (int i=0;i<n;i++){
    cout << arr[i]<< ' ';
  }
  cout << endl;
}

int bogoSort(int*arr,int n,int count){
  while(!checkSorted(arr,n)){
    Shuffle(arr,n);
    count++;
  }
  return count;
}



int main(){
  int n;
  cout << "Size of array : ";
  cin >> n;
  int *arr=new int[n];
  cout << "Enter the array (with spaces between elements) : ";
  for (int i=0;i<n;i++){
    cin>> arr[i];
  }
  
  auto start = chrono::high_resolution_clock::now();
  int runs = bogoSort(arr,n,0);
  auto stop = chrono::high_resolution_clock::now();
  auto duration = chrono::duration_cast<chrono::microseconds>(stop - start);
  printArray(arr,n);
  cout << "Time taken by function: "<< duration.count() << " microseconds" << endl;
  cout << "No of iterations : "<< runs<< endl;
}
