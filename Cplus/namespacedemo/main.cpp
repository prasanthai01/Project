#include <iostream>

using namespace std;

int main()
{
 string name;
 cout << "Enter your name" << endl;
 cin >> name;
 cout << name << endl;
 fflush (stdin);
 cout << "Enter your name" << endl;
 getline (cin,name);
 cout << name << endl;


 string firstname;
 string lastname;
 cin >> firstname >> lastname;

 cout << firstname +" "+ lastname << endl;
 string fullname= firstname.append(lastname);
 cout << fullname << endl;

 lastname.push_back(' S');
 cout << lastname << endl;

 cout << firstname << endl;
 firstname.push_back('JO');
 cout << firstname;

 cout << firstname +""+ lastname;

}
