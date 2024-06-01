#include<bits/stdc++.h>
using namespace std;

bool fileExists(string& filename){
  ifstream file(filename);
  return file.is_open();
}

void printFile(string& filename){
  ifstream file(filename);
  string str;
  int count=1;
  cout << "Tasks "<< endl;
  cout << "-------------------------------------"<< endl;
  while(getline(file,str)){
    cout <<count<< " -> "<<  str<< endl;
    count++;
  }
  cout << "-------------------------------------"<< endl;
  file.close();

}

void printLastTodo(string& filename){
  ifstream file(filename);
  string str1,str2;
  while(getline(file,str2)){
    str1=str2;
  }
  cout << str1<< endl;
  file.close();
}

void enterTodo(string& filename,vector<string> & vic,int* count){
  system("clear");
  printFile(filename);
  fstream file(filename, ios::app);
  file.seekg(0,ios::end);
  string todo;
  cout << "Enter your to-do task : "<< endl;
  getline(cin >> ws,todo);
  vic.emplace_back(todo);
  (*count)++;
  todo=todo+"\n";
  file << todo;
  file.close();
}

void deleteTodo(string& filename,vector<string>& vic){
  system("clear");
  printFile(filename);
  int index;
  cout << "Enter task index to be removed : ";
  cin >> index;
  while(index<1 || index> vic.size()){
    cout << "Invalid task index"<< endl;
    cout << "Enter task index to be removed (-1 to cancel) : ";
    cin >> index;
    if (index==-1){
      return;
    }
  }
  vic.erase(vic.begin()+index-1);
  ofstream file(filename);
  for (int i=0;i<vic.size();i++){
    string todo=vic[i];
    todo=todo+"\n";
    file << todo;
  }
  file.close();
}

int main(){
  string todo_file="to_do.txt";
  if (fileExists(todo_file)){
    cout << "To do list,File found !\n"<< endl;
  }
  else{
    cout << "To do list file not found. Would you like to create one?"<< endl;
    char choice;
    cout << "Choice (y/n) : ";
    cin>> choice;
    if (choice !='y'){
      cout << "Exiting ..."<< endl;
      return 0;
    }
    else{
      ofstream outfile(todo_file);
      outfile.close();
      cout <<"File created successfully .. "<< endl;
      cout <<"File name "<< todo_file<< endl;
      cout << endl;
    }
   
  }
  cout << "-----To Do List-----\n0 -> To exit \n1 -> To read the file \n2 -> To display the last entry \n3 -> To append a new entry into the file \n4 -> To delete a todo"<< endl;
  int choice;
  vector<string> vic;
  int count=0;

  ifstream file(todo_file);
  string prev;
  while(getline(file,prev)){
    vic.emplace_back(prev);
  }
  file.close();

  while(1){
    cout << "Choice : ";
    cin >> choice;
    while(choice<=0 && choice>=4){
      cout << "Enter valid number"<< endl;
      cout << "Choice : "<< endl;
      cin >> choice;
    }
    if (choice==0){
      cout << "Thanks for trying !! "<< endl;
      return 0 ;
    }
    else if(choice == 1){
      printFile(todo_file);
    }
    else if(choice == 2){
      printLastTodo(todo_file);
    }
    else if(choice == 3){
      enterTodo(todo_file,vic,&count);
      cout << "-----To Do List-----\n0 -> To exit \n1 -> To read the file \n2 -> To display the last entry \n3 -> To append a new entry into the file \n4 -> To delete a todo"<< endl;
    }
    else if(choice == 4){
      deleteTodo(todo_file,vic);
      cout << "-----To Do List-----\n0 -> To exit \n1 -> To read the file \n2 -> To display the last entry \n3 -> To append a new entry into the file \n4 -> To delete a todo"<< endl;
    }
    cout << endl;
  }

}
