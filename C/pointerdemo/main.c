#include<iostream>

using namespace std;

int main()
{
   // char name[10]={}; c
  string name;
    cout<< "Enter your name : " << endl;
    cin >> name;
    cout << name << endl;
    fflush(stdin);
    cout<< "Enter your name : " << endl;
    getline(cin,name);
    cout << name << endl;


  string firstname;
  string lastname;
  cin>> firstname >>lastname;

  cout << firstname +" "+ lastname << endl ;
  string fullname = firstname.append(lastname);
  cout << fullname << endl;

  lastname.push_back('k');
  cout << lastname << endl;

  cout << firstname << endl;
   firstname.push_back('pp');
  cout << firstname;

  cout << firstname +" "+ lastname << endl ;



 /* fflush(stdin);
  string fullname;
  cin>> fullname;
  fullname.insert(4," ag ");
  cout << fullname;



    return 0;
}

/*


include <iostream>

using namespace std;


namespace student{
string name="priya";
}

namespace student1{
string name="priya01";
}

using namespace student;

int main()
{


    string name="priya";
    cout << name << endl;

    string name="priya";
    cout << name << endl;
    cout << student1::name << endl;

    return 0;
}



/*
