#include<bits/stdc++.h>
using namespace std;

void printArray(vector<int>& temp,int n){
  cout << "Array : ";
  for (int i=0;i<n;i++){
    cout << temp[i]<< ' ';
  }
  cout << endl;
}

int bubble_sort(vector<int>& arr,int n){
  auto start = chrono::high_resolution_clock::now();
  for (int i=0;i<n-1;i++){
    bool swapped=false;
    for (int j=0;j<n-i-1;j++){
      if (arr[j]>arr[j+1]){
        swap(arr[j],arr[j+1]);
        swapped=true;
      }
    }
    if (!swapped){
      break;
    }
  }
  auto stop = chrono::high_resolution_clock::now();
  auto duration = chrono::duration_cast<chrono::microseconds>(stop - start);
  return (int)duration.count();
}

int insertion_sort(vector<int>& arr,int n){
  auto start = chrono::high_resolution_clock::now();
  for (int i=1;i<n;i++){
    int j=i;
    while (arr[j-1]>arr[j] && j>0){
      swap(arr[j-1],arr[j]);
      j--;
    }
  }
  auto stop = chrono::high_resolution_clock::now();
  auto duration = chrono::duration_cast<chrono::microseconds>(stop - start);
  return (int)duration.count();

}

int selection_sort(vector<int>& arr,int n){
  auto start = chrono::high_resolution_clock::now();
  for (int i=0;i<n-1;i++){
    int minimum=i;
    for (int j=i+1;j<n;j++){
      if (arr[j]<arr[minimum]) minimum=j;
    }
    swap(arr[i],arr[minimum]); 
  }
  auto stop = chrono::high_resolution_clock::now();
  auto duration = chrono::duration_cast<chrono::microseconds>(stop - start);
  return (int)duration.count();

}

void merge(vector<int>& arr,int start,int end){
  int mid=(start+end)/2;
  int l1=mid-start+1;
  int l2=end-mid;
  // int* arr1=new int[l1];
  // int* arr2=new int[l2];
  vector<int> arr1(l1);
  vector<int> arr2(l2);
  int arrayindex=start;

  for (int i=0;i<l1;i++){
    arr1[i]=arr[arrayindex++];
  }
  for (int j=0;j<l2;j++){
    arr2[j]=arr[arrayindex++];
  }

  int i=0;
  int j=0;
  arrayindex=start;

  while (i<l1 && j<l2){
    if (arr1[i]<arr2[j]){
      arr[arrayindex++]=arr1[i++];
    }
    else {
      arr[arrayindex++]=arr2[j++];
    }
  }
  while (i<l1){
    arr[arrayindex++]=arr1[i++];
  }
  while (j<l2){
    arr[arrayindex++]=arr2[j++];
  }
}


void merge_sort(vector<int>& arr,int start,int end){
  int mid=(start+end)/2;
  if (start>=end){
    return;
  }
  merge_sort(arr,start,mid);
  merge_sort(arr,mid+1,end);
  merge(arr,start,end);

}

int quick(vector<int>& arr,int start,int end){
  int element=arr[start];
  int count=0;
  for (int i=start;i<=end;i++){
    if (arr[i]<element){
      count++;
    }
  }
  swap(arr[start],arr[start+count]);
  int index=start+count;
  int i=start;
  int j=end;
  while (i<index && j>index){
    while (arr[i]<element){
      i++;
    }
    while (arr[j]>element){
      j--;
    }
    if (arr[i]>element && arr[j]<element ){
      swap(arr[i++],arr[j--]);
    }
  }
  return index;

}

void quick_sort(vector<int>& arr,int start,int end){
  if (start>=end){
    return;
  }
  int index=quick(arr,start,end);

  quick_sort(arr,start,index-1);
  quick_sort(arr,index+1,end);
  return;

}

void Shuffle(vector<int>& arr,int n){
  for (int i=0;i<n;i++){
    swap(arr[i],arr[rand()%n]);
  }
}

bool checkSorted(vector<int> arr,int n){
  for (int i=0;i<n-1;i++){
    if (arr[i]>arr[i+1]){
      return false;
    }
  }
  return true;
}

int bogo_sort(vector<int>& arr,int n){
  auto start = chrono::high_resolution_clock::now();
  while(!checkSorted(arr,n)){
    Shuffle(arr,n);
  }
  auto stop = chrono::high_resolution_clock::now();
  auto duration = chrono::duration_cast<chrono::microseconds>(stop - start);
  return (int)duration.count();
}

void tryBubble(vector<int>& arr,int n)
{
  vector<int> temp(arr.begin(),arr.end());
  int time = bubble_sort(temp,n);
  printArray(temp,n);
  cout << "Time taken by bubble sort: "<< time << " microseconds" << endl;
}

void tryInsertion(vector<int>& arr,int n){
  vector<int> temp(arr.begin(),arr.end());
  int time = insertion_sort(temp,n);
  printArray(temp,n);
  cout << "Time taken by insertion sort: "<< time << " microseconds" << endl;
}

void trySelection(vector<int>& arr,int n){
  vector<int> temp(arr.begin(),arr.end());
  int time = selection_sort(temp,n);
  printArray(temp,n);
  cout << "Time taken by selection sort: "<< time << " microseconds" << endl;
}

void tryMerge(vector<int>& arr,int n){
  vector<int> temp(arr.begin(),arr.end());
  auto start = chrono::high_resolution_clock::now();
  merge_sort(temp,0,n-1);
  auto stop = chrono::high_resolution_clock::now();
  auto time = chrono::duration_cast<chrono::microseconds>(stop - start);
  printArray(temp,n);
  cout << "Time taken by merge sort: "<< time.count() << " microseconds" << endl;
}

void tryQuick(vector<int>& arr,int n){
  vector<int> temp(arr.begin(),arr.end());
  auto start = chrono::high_resolution_clock::now();
  quick_sort(temp,0,n-1);
  auto stop = chrono::high_resolution_clock::now();
  auto time = chrono::duration_cast<chrono::microseconds>(stop - start);
  printArray(temp,n);
  cout << "Time taken by quick sort: "<< time.count() << " microseconds" << endl;
}

void tryBogo(vector<int>& arr,int n){
  vector<int> temp(arr.begin(),arr.end());
  int time = bogo_sort(temp,n);
  printArray(temp,n);
  cout << "Time taken by bogo sort: "<< time << " microseconds" << endl;
}

int main(){
  int n;
  cout << "Size of array : ";
  cin >> n;
  // int *arr=new int[n];
  vector<int> arr(n,0);
  cout << "Enter the array (with spaces between elements) : ";
  for (int i=0;i<n;i++){
    cin>> arr[i];
  }
  cout << "Enter \n-1 -> To take a new array \n0 -> To exit \n1 -> To try bubble sort \n2 -> To try insertion sort \n3 -> To try selection sort \n4 -> To try merge sort \n5 -> To try quick sort \n6 -> To try bogo sort\n7 -> To try and compare all the sorting"<< endl;
  int choice;
re:
  cout << "Choice : ";
  cin >> choice;
  while (choice <=-2 || choice>=8){
    cout << "Invalid input ."<< endl;
    cout << "Choice : ";
    cin >> choice;
  }
  while(1){
    if (choice==-1){
      cout << "Size of array : ";
      cin >> n;
      // int *arr=new int[n];
      arr.clear();
      cout << "Enter the array (with spaces between elements) : ";
      for (int i=0;i<n;i++){
        int k;
        cin >> k;
        arr.emplace_back(k);
      }
    }
    else if (choice == 1){
      tryBubble(arr,n);
    }
    else if (choice == 2){
      tryInsertion(arr,n);
    }
    else if (choice == 3){
      trySelection(arr,n);
    }
    else if (choice == 4){
      tryMerge(arr,n);
    }
    else if (choice == 5){
      tryQuick(arr,n);
    }
    else if (choice == 6){
      tryBogo(arr,n);
    }
    else if (choice == 7){
      tryBubble(arr,n);
      tryInsertion(arr,n);
      trySelection(arr,n);
      tryMerge(arr,n);
      tryQuick(arr,n);
      tryBogo(arr,n);
    }
    else{
      cout << "Thanks for using my program !!"<< endl;
      return 0;
    }
    goto re;

  }
 
  
}
