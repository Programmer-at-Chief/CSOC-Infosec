#include<bits/stdc++.h>
using namespace std;

bool fileExists(string& filename){
  ifstream file(filename);
  return file.is_open();
}

void sendToFile(vector<vector<string>>& vic,string filename){
  ofstream file(filename);
  for (int i=0;i<vic.size();i++){
    for (int j=0;j<vic[i].size();j++){
      if (j==0){
        string user=vic[i][j]+" :";
        file<< user;
        file<< endl;
        continue;
      }
      file<< vic[i][j];
      file<< endl;
    }
    file<< endl;
  }
  file.close();
}

void printFile(string& filename){
  ifstream file(filename);
  cout << "Tasks "<< endl;
  cout << "-------------------------------------"<< endl;
  string user; 
  getline(file,user);
  while(user.length()!=0){
    cout << "User : "<< user<< " To do"<< endl;
    string str;
    getline(file,str);
    int count=1;
    while(str.length()!=0){
      cout <<count<< " -> "<<  str<< endl;
      getline(file,str);
      count++;
    }
    getline(file,user);
    if (file.eof()){
      break;
    }
    cout << endl;
  }
  cout << "-------------------------------------"<< endl;
  file.close();
}

void printUsertodo(vector<vector<string>>& vic,int* user_count){
  system("clear");
  // for (int i=0;i<vic.size();i++){
  //   for (int j=0;j<vic[i].size();j++){
  //     cout << vic[i][j]<<' ';
  //   }
  //   cout << endl;
  // }
  string user;
  cout << "Enter your username : ";
  getline(cin>> ws,user);

  int index=0;
  while(vic[index][0]!=user){
    index++;
    if (index==*user_count){
      cout << "User not found."<< endl;
      return;
    }
  }
  cout << "-------------------------------------"<< endl;
  cout << user<< " To Do"<< endl;
  cout << "-------------------------------------"<< endl;

  for (int i=1;i<vic[index].size();i++){
    cout << (i) << " -> "<< vic[index][i]<< endl; 
  }
}

void enterTodo(string& filename,vector<vector<string>> & vic,int* count){
  system("clear");
  printFile(filename);
  string user;
  cout << "Enter your username : ";
  getline(cin>> ws,user);
  int index=0;
  while(index <*count && vic[index][0]!=user ){
    index++;
  }
  if (index==*count){
    cout << "\nUser not found"<< endl;
    return;
  }
  string todo;
  cout << "Enter your to-do task : ";
  getline(cin >> ws,todo);
  (vic[index]).emplace_back(todo);

  sendToFile(vic,filename);
}

void deleteTodo(string& filename,vector<vector<string>>& vic,int* count){
  system("clear");
  // printFile(filename);
  string user;
  int userindex=0;
  cout << "Enter your username : ";
  getline(cin>> ws,user);
  while(userindex <*count && vic[userindex][0]!=user ){
    userindex++;
  }
  if (userindex==*count){
    cout << "\nUser not found"<< endl;
    return;
  }
  // printUsertodo(vic,count);
  int index=0;
  cout << "-------------------------------------"<< endl;
  cout << user<< " To Do"<< endl;
  cout << "-------------------------------------"<< endl;

  for (int i=1;i<vic[userindex].size();i++){
    cout << (i) << " -> "<< vic[userindex][i]<< endl; 
  }

  cout << "Enter task index to be removed : ";
  cin >> index;
  while(index<1 || index> vic[userindex].size()){
    cout << "Invalid task index"<< endl;
    cout << "Enter task index to be removed (-1 to cancel) : ";
    cin >> index;
    if (index==-1){
      return;
    }
  }
  vic[userindex].erase(vic[userindex].begin()+index);
  sendToFile(vic,filename);
}

void newUser(string filename,vector<vector<string>>& vic,int* count){
  vector<string> temp;
  cout << "Enter username : ";
  string user;
  getline(cin>> ws,user);
  temp.emplace_back(user);
  (*count)++;
  vic.emplace_back(temp);
  sendToFile(vic,filename);

}

void deleteUser(string filename,vector<vector<string>>& vic,int *count){
  if (vic.size()==0){
    cout << "No user found, create a user first"<< endl;
    return;
  }
  string user;
  cout << "Enter username to be deleted : ";
  getline(cin>>ws,user);
  bool found=false;
  int index=0;
  while(!found){
    while(index<*count && vic[index][0]!=user){
      index++;
    }
    if (index==*count){
      cout << "Invalid username"<< endl;
      cout << "Enter username to be deleted (-1 to cancel): ";
      getline(cin>>ws,user);

    }
    if (user=="-1"){
      return;
    }
    else if(vic[index][0] == user){
      found=true;

    }
  }
  (*count)--;

  vic.erase(vic.begin()+index);
  sendToFile(vic,filename);
  cout << user << " Deleted successfully"<< endl;
  cout << "-----To Do List-----\n0 -> To exit \n1 -> To read the file \n2 -> To display a user\'s todo\n3 -> To append a new entry into the file \n4 -> To delete a todo \n5 -> To enter a new user\n6 -> To delete a user"<< endl;
  return;
}

int main(){
  string todo_file="to_do_users.txt";
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
      cout <<"File created successfully .. \n"<< endl;
    }
   
  }
  cout << "-----To Do List-----\n0 -> To exit \n1 -> To read the file \n2 -> To display a user\'s todo\n3 -> To append a new entry into the file \n4 -> To delete a todo \n5 -> To enter a new user\n6 -> To delete a user"<< endl;

  int choice;

  // retrieve the present tasks
  ifstream file(todo_file);
  vector<vector<string>>vic;
  int user_count=0;
  string user;
  getline(file,user);
  while(user.length()!=0 && !file.eof()){
    vector<string> temp;
    user=user.substr(0,user.size()-2);
    temp.emplace_back(user);
    string task;
    getline(file,task);
    while(task.length()!=0 ){
      temp.emplace_back(task);
      getline(file,task);
    }
    vic.emplace_back(temp);
    getline(file,user);
    user_count++;
    if (file.eof()) break;
  }
  // for (int i=0;i<vic.size();i++){
  //   for (int j=0;j<vic[i].size();j++){
  //     cout << vic[i][j]<<' ';
  //   }
  //   cout << endl;
  // }
  
  file.close();

  while(1){
    cout << "Choice : ";
    cin >> choice;
    while(choice<=0 && choice>=7){
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
      printUsertodo(vic,&user_count);
      cout << "-----To Do List-----\n0 -> To exit \n1 -> To read the file \n2 -> To display a user\'s todo\n3 -> To append a new entry into the file \n4 -> To delete a todo \n5 -> To enter a new user \n6 -> To delete a user"<< endl;
    }
    else if(choice == 3){
      enterTodo(todo_file,vic,&user_count);
      cout << "-----To Do List-----\n0 -> To exit \n1 -> To read the file \n2 -> To display a user\'s todo\n3 -> To append a new entry into the file \n4 -> To delete a todo\n5 -> To enter a new user\n6 -> To delete a user"<< endl;
    }
    else if(choice == 4){
      deleteTodo(todo_file,vic,&user_count);
      cout << "-----To Do List-----\n0 -> To exit \n1 -> To read the file \n2 -> To display a user\'s todo\n3 -> To append a new entry into the file \n4 -> To delete a todo\n5 -> To enter a new user\n6 -> To delete a user"<< endl;
    }
    else if (choice == 5){
      newUser(todo_file,vic,&user_count);
    }
    else if (choice == 6){
      deleteUser(todo_file,vic,&user_count);
    }
    cout << endl;
  }

}
