#include <iostream>
using namespace std;

class Prasanthvlog
{
public:

    int  vlogerlist()
    {
        string name;
        cout << "Enter the name";
        cin >> name ;
        cout << "Hey..." << name << endl;
    }
    int vlogerlist(string name)
    {
        cout << "Hey..." << name << "\tWelcome to prasanth Vlogs" << endl;
    }
    int vlogerlist(string name,string location)
    {
        cout << "Hey..." << name << "\tWelcome to prasanth Vlogs\t" << location << endl;
    }
    int vlogerlist(string name,string location, int no )
    {
         cout << "Hey..." << name << "\tWelcome to prasanth Vlogs\t" << location << no << endl;
    }
};

int main ()
{
    Prasanthvlog PV;
    PV .vlogerlist();

    PV .vlogerlist("Siddhu");
    PV .vlogerlist ("Yogaraj", "Thanjavur");
    PV .vlogerlist ("Saravanan", "Thanjavur ",20);
    return 0;


}
