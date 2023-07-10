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
    double m_bullet;
    double h_monkey;
    double l_monkey;
    double m_monkey;
    double r_monkey;
    double dt;
    
    cout << "初期値の設定" << endl;
    cout << "v_bullet[m/s] = ";
    cin >> v_bullet;
    cout << "ang_bullet[度] = ";
    cin >> ang_bullet;
    cout << "m_bullet[kg] = ";
    cin >> m_bullet;
    cout << "h_monkey[m] = ";
    cin >> h_monkey;
    cout << "l_monkey[m] = ";
    cin >> l_monkey;
    cout << "m_monkey[kg] = ";
    cin >> m_monkey;
    cout << "r_monkey[m] = ";
    cin >> r_monkey;
    cout << "dt[ms] = ";
    cin >> dt;

    double x_bullet;
    double y_bullet;
    double x_monkey = l_monkey;
    double y_monkey;
    double t_hit = 0;
    for(double t = 0;; t+=dt){
        int ts = t/1000;
        x_bullet = v_bullet * cos(M_PI*ang_bullet/180) * ts;
        y_bullet = v_bullet * sin(M_PI*ang_bullet/180) * ts - (0.5 * G * ts*ts);
        y_monkey = h_monkey - 0.5 * G * ts*ts;
        char name[100];
        sprintf(name, "monkey_hunting.txt");
        const char *filename = name;
        ofstream ofs (filename, std::ios::app);
        if(!ofs){
            cout << "failed to open file" << endl;
        }
        ofs << ts << " " << x_bullet << " " << y_bullet << " " << x_monkey << " " << y_monkey << endl;
        if((y_bullet < 0) || (y_monkey <= r_monkey)){
            cout << "no hit" << endl;
            t_hit = -1;
            break;
        }else if((x_monkey - x_bullet <= r_monkey) && (fabs(y_monkey - y_bullet) <= r_monkey)){
            cout << "hit" << endl;
            t_hit = ts;
            break;
        }
    }
    if(t_hit != -1){
        double vx_bullet = v_bullet * cos(M_PI*ang_bullet/180);
        double vy_bullet = v_bullet * sin(M_PI*ang_bullet/180) - G * t_hit;
        double vy_monkey = -G * t_hit;
        double V_x = m_bullet * vx_bullet / (m_bullet + m_monkey);
        double V_y = (m_bullet * vy_bullet + m_monkey * vy_monkey) / (m_bullet + m_monkey);
        for(double t = dt;; t+=dt){
            int ts = t/1000;
            double X = V_x*ts;
            double Y = V_y*ts - 0.5*G*ts*ts;
            char name[100];
            sprintf(name, "monkey_hunting.txt");
            const char *filename = name;
            ofstream ofs (filename, std::ios::app);
            if(!ofs){
                cout << "failed to open file" << endl;
            }
            ofs << ts + t_hit << " " << x_bullet + X << " " << y_bullet + Y << " " << x_monkey + X << " " << y_monkey + Y << endl;
            if(y_monkey + Y <= r_monkey){
                break;
            }
        }
    }
}
