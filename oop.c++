 #include <iostream>
#include <conio.h>
using namespace std;
class point {
    float x,y;
  public:
    point() {
      cout<<"point::point()\n";
      x = 0;
      y = 0;
      }
    point(float ox, float oy) {
      cout<<"point::point(float, float)\n";
      x = ox;
      y = oy;
      }
    point(point &p) {
      cout<<"point::point(point &)\n";
      x = p.x;
      y = p.y;      }
void display() ;
   void move(float dx, float dy) {
     x += dx;
     y += dy;
     }
   void Identifier() {
      cout<<"Diem khong mau \n";
      }
  };
void point::display()  {
      cout<<"Toa do : "<<x<<" "<<y<<endl;
      Identifier();
      }
 class threedimpoint : public point {
    float z;
  public:
    threedimpoint() {
      z = 0;
      }
    threedimpoint(float ox, float oy, float oz):point (ox, oy) {
      z = oz;
      }
    threedimpoint(threedimpoint &p) :point(p) {
      z = p.z;
      }
    virtual void Identifier() {
      cout<<"Toa do z : "<<z<<endl;
      }
  };
class coloredthreedimpoint : public threedimpoint {
    unsigned color;
  public:
    coloredthreedimpoint() {
      color = 0;
      }
    coloredthreedimpoint(float ox, float oy, float oz,unsigned c):
                         threedimpoint (ox, oy, oz) 
      {
        color = c;
      }
    coloredthreedimpoint(coloredthreedimpoint &p) :threedimpoint(p) {
      color = p.color;
      }
    void Identifier() {
      cout<<"Diem mau  : "<<color<<endl;
      }
  };
int main() {
  
  cout<<"point p(10,20);\n";
  point p(10,20);
  cout<<"p.display()\n";
  p.display();
  cout<<"threedimpoint p3d(2,3,4);\n";
  threedimpoint p3d(2,3,4);
  cout<<"p3d.display();\n";
  p3d.display();
  cout<<"p3d.Identifier();\n";
  p3d.Identifier();
  cout<<"coloredthreedimpoint p3dc(2,3,4,10);\n";
  coloredthreedimpoint p3dc(2,3,4,10);
  cout<<"p3dc.display();\n";
  p3dc.display();
  cout<<"p3dc.Identifier();\n";
  p3dc.Identifier();
  getch();   }


