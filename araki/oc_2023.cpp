//オープンキャンパス2023[モンキーハンティング]
#include<iomanip>
#include<iostream>
#include<cmath>
#include<vector>
#include<fstream>
#include<stdio.h>
using namespace std;

# define G 9.80665

int main(){
    double v_bullet;
    double ang_bullet;
    const double m_bullet = 0.01;
    double h_monkey;
    double l_monkey;
    const double m_monkey = 15;
    const double r_monkey = 0.8;
    double dt = 0.01;
    
    cout << "v_bullet = ";
    cin >> v_bullet;
    cout << "ang_bullet = ";
    cin >> ang_bullet;
    cout << "h_monkey = ";
    cin >> h_monkey;
    cout << "l_monkey = ";
    cin >> l_monkey;

    double x_bullet;
    double y_bullet;
    double x_monkey = l_monkey;
    double y_monkey;
    double t_hit = 0;
    for(double t = 0;; t+=dt){
        x_bullet = v_bullet * cos(M_PI*ang_bullet/180) * t;
        y_bullet = v_bullet * sin(M_PI*ang_bullet/180) * t - (0.5 * G * t*t);
        y_monkey = h_monkey - 0.5 * G * t*t;
        char name[100];
        sprintf(name, "monkey_hunting.txt");
        const char *filename = name;
        ofstream ofs (filename, std::ios::app);
        if(!ofs){
            cout << "failed to open file" << endl;
        }
        ofs << t << " " << x_bullet << " " << y_bullet << " " << x_monkey << " " << y_monkey << endl;
        if((y_bullet < 0) || (y_monkey <= r_monkey)){
            cout << "no hit" << endl;
            t_hit = -1;
            break;
        }else if((x_monkey - x_bullet <= r_monkey) && (fabs(y_monkey - y_bullet) <= r_monkey)){
            cout << "hit" << endl;
            t_hit = t;
            break;
        }
    }
    if(t_hit != -1){
        double vx_bullet = v_bullet * cos(M_PI*ang_bullet/180);
        double vy_bullet = v_bullet * sin(M_PI*ang_bullet/180) - G * t_hit;
        double vy_monkey = -G * t_hit;
        double V_x = m_bullet * vx_bullet / (m_bullet + m_monkey);
        double V_y = (m_bullet * vy_bullet + m_monkey * vy_monkey) / (m_bullet + m_monkey);
        for(double t = 0.1;; t+=dt){
            double X = V_x*t;
            double Y = V_y*t - 0.5*G*t*t;
            char name[100];
            sprintf(name, "monkey_hunting.txt");
            const char *filename = name;
            ofstream ofs (filename, std::ios::app);
            if(!ofs){
                cout << "failed to open file" << endl;
            }
            ofs << t + t_hit << " " << x_bullet + X << " " << y_bullet + Y << " " << x_monkey + X << " " << y_monkey + Y << endl;
            if(y_monkey + Y <= r_monkey){
                break;
            }
        }
    }
}
