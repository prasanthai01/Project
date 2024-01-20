#include <stdio.h>
#include <stdlib.h>

int main()
{
   int a=5;
   int b=10;
   int c;
   Additionprogram(a,b);
   Subtractionprogram(a,b);
   Multiplicationprogram(a,b);
   Divisionprogram(a,b);
   Modulusprogram(a,b);
   Incrementprogram(a);
   Decrementprogram(b);
   AssignmentDemoOperatorsprogram();
   ComparisionDemoOperatorsprogram();
   LogicalDemoOperatorsprogram();

   return 0;

}
int Additionprogram(int a,int b)
{
    int c=a+b;
    printf("\nAddition :");
    printf("\n\t Added value of...%d",c);
}
int Subtractionprogram(int a,int b)
{
    int c=b-a;
    printf("\nSubtraction :");
    printf("\n\t Subtracted value of...%d",c);
}
int Multiplicationprogram(int a,int b)
{
    int c=a*b;
    printf("\nMultiplication :");
    printf("\n\t Multiply value of...%d",c);
}
int Divisionprogram(int a,int b)
{
    int c=a/b;
    printf("\nDIVISION :");
    printf("\n\t divided value of...%d",c);
}
int Modulusprogram(int a,int b)
{
    int c=a%b;
    printf("\nMODULUS :");
    printf("\n\t modulus value of...%d",c);
}
int Incrementprogram(int a)
{
    while (a>10)
    printf("\nINCREMENT :");
    printf("\n\t increment value of...%d",++a);
}
int Decrementprogram(int b)
{
    while (b>15)
    printf("\nDECREMENT :");
    printf("\n\t decrement value of...%d",--b);
}
int AssignmentDemoOperatorsprogram()
{
    int a=4;
    int b=8;
    int c,d,e,f,g;
    d=450;
    e=35;
    f=45;
    g=600;
    c=b;
    d+=a;
    e-=b;
    f/=a;
    g*=4;
    printf("\nASSIGNMENT OPERATORS PROGRAM :");
    printf("\n\t the value of equal to is...%d\n\t the value of += is....%d\n\t the value of -= is...%d\n\t the value of /= is...%d\n\t the value of *= is...%d\n",c,d,e,f,g);
    return 0;
}

int ComparisionDemoOperatorsprogram()
{
    int a=5;
    int b=10;
    int c=15;
    int d=20;
    int e=25;
    int f=30;
    int i,j,k,l,m,n;
    i=a<b;
    j=b>c;
    k=c<=b;
    l=d>=c;
    m=e!=d;
    n=f==e;
    printf("\nCOMPARISION OPERATORS PROGRAM :");
    printf("\n\tThe value Less than A is...%d\n\t The value Greater than B is...%d\n\t The value Less than or equal C is...%d\n\t The value Greater than or equal D is...%d\n\t The value Not equal E is...%d\n\t The valur Equal equal F is ...%d\n",i,j,k,l,m,n);
    return 0;
}
int LogicalDemoOperatorsprogram()
{
    printf("\n LOGICAL OPERATORS PROGRAM :");
    int a=7;
    if (a<10 && 3>a)
{
    printf("\n\t The Logical AND value is...%d",a);
}
 else if(a=10 || a>15)
{
   printf("\n\t The Logical OR value is...%d",a);
}
 else if (a!=5)
 {
     printf("\n\t The Logical NOT value is...%d",a);
 }
else
{
    printf("\n't NO Logical value");
}
}
