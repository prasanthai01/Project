#include <iostream>
using namespace std;

class MyFirstClass
{
    public:
    int a=0;
   // cout<<a;
void multiply()
    {
        int x,y,z;
        cout << "Enter value x\n";
        cin >> x;
        cout <<"Enter value y \n";
        cin >> y;
        cout <<"Enter value z \n"<<(x*y);
    }
};
int Addition ()
{
    int a,b,s;
    cin >> a >>b;
    s = a + b;
    cout << s;
    return 0;
}


int main()
{
    Addition();
    MyFirstClass MFC;
    MFC.a;
    MFC.multiply();
    return 0;
}
