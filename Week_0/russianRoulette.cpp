#include<bits/stdc++.h>
using namespace std;
int main(){
  cout << "Enter \n1 -> To play the game\n0 -> To exit \nEnter your choice (0/1) : ";
  int choice;
  cin >> choice;
  if (choice !=0 && choice !=1){
    cout << "Enter a valid number .";
    cout << "Choice (0/1) : ";
    cin >> choice;
  }
  while(choice==1){
    this_thread::sleep_for(chrono::seconds(2));
    cout << "\nThe gun is handed to you ....\n";
    this_thread::sleep_for(chrono::seconds(1));
    cout << endl;
    this_thread::sleep_for(chrono::seconds(1));
    vector<int> magazine(6,0); // a magazine vector will store work as the revolver magazine
    magazine[rand()%6]=1; // a random index between 0 to 5 will contain a bullet
    // bool alive=true;
    int points=0;
    int index=0;
    int chamber;
    cout << "Enter the chambers to skip : "<< endl;
    cin >> chamber;
    index=chamber%6;
    this_thread::sleep_for(chrono::seconds(1));
    cout << index<< " Chambers skipped."<< endl;
    while(1){
      cout << "Press y to pull the trigger \nPress n to stop the game \nChoice : ";
      char pull;
      cin >> pull;
      if (pull=='n'){
        goto end;
      }
      else if (pull!='y'){
        cout << "Come,on. Do it.\n";
        cout << "Choice : ";
        cin >> pull;
      }

      this_thread::sleep_for(chrono::seconds(1));
      index++;
      cout << endl;

      this_thread::sleep_for(chrono::seconds(1));
      cout << "Click ..."<< endl;
      if (magazine[index%6]){
        break;
      }
       cout << "\nCongratulation!! You are safe .." << endl;
        points++;

    }
    // while(!magazine[index%6]);
    cout << "\nSuka Blyat!! You Died." << endl;

end:
    cout << "You have "<< points<< " points." << endl;
    cout << "Wanna play again??"<< endl;
    cout << "Choice (0/1) : ";
    cin >> choice;
  }
  cout << "\nThanks for playing!!"<< endl;
}
