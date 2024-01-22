#include <iostream>
using namespace std;

class stringclass
{
public :
    stringclass()
    {
        cout << "Enter the name \n";
        string name;
        cin >> name;
        cout << "Hi..." << name << "Welcome to the string constructor";
        cout << "\n Enter value for selection \t";
        int n;
        cin >> n;
        switch(n)
        {
        case 1:
            {
                cout << "Tamil welcome to switch with constructor ";
            }
        break;
        case 2:
            {
                cout << "Kaala Welcome to switch with constructor ";
            }
        break;
        case 3:
            {
                cout << "Kumar welcome to switch with constructor ";
            }
        break;
        }
    }
    stringclass (string a,string b)
    {
        string c;
        c=a+b;
        cout << "concate string value is..." << c;
    }
};
int main ()
{
    stringclass sc;
    stringclass sc1("Tamil","GS");

    return 0;
}
