#include <iostream>
using namespace std;

class constructoversample
{
public:
    constructoversample()
    {
        cout << "New film list \n";
    }
    constructoversample(string movie1)
    {
        cout << "The first new film watch in sunday is " << movie1 << endl;
    }
    constructoversample(string movie1,string movie2)
    {
        cout << "\n The Second new film watch in last week are " << movie1 << "," << movie2 << endl;
    }
    constructoversample(string movie1, string movie2,string movie3)
    {
        cout << "\n The Third new film watch in last last night " << movie1 << "," << movie2 << "," << movie3 << endl;
    }
};
int main()
{

    string movie1,movie2,movie3;
    constructoversample cs;
    cin >> movie1;
    constructoversample cs1(movie1);
     cin >> movie1 >> movie2;
    constructoversample cs2(movie1, movie2);
     cin >> movie1>> movie2>>movie3;
    constructoversample cs3(movie1, movie2,movie3);


    return 0;
}
