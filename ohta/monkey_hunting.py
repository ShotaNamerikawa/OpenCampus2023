import math
G = 9.80665

# 初期値を入力する部分
while True:
    try:
        v_bullet = float(input("v_bullet[m/s] = "))
        ang_bullet = float(input("ang_bullet[度] = "))
        m_bullet = float(input("m_bullet[kg] = "))
        h_monkey = float(input("h_monkey[m] = "))
        l_monkey = float(input("l_monkey[m] = "))
        m_monkey = float(input("m_monkey[kg] = "))
        r_monkey = float(input("r_monkey[m] = "))
        dt = float(input("dt[s] = "))
        break
    except:
        print("エラー　もう一度入力\n")
        continue
x_bullet = 0.0
y_bullet = 0.0
x_monkey = l_monkey
y_monkey = h_monkey
t_hit = 0.0


# シミュレーション部分
with open("monkey_hunting.txt", "w") as ofs:
    t = 0.0
    while True:
        x_bullet = v_bullet * math.cos(math.pi * ang_bullet / 180) * t
        y_bullet = v_bullet * math.sin(math.pi * ang_bullet / 180) * t - (0.5 * G * t * t)
        y_monkey = h_monkey - 0.5 * G * t * t

        ofs.write(f"{t} {x_bullet} {y_bullet} {x_monkey} {y_monkey}\n")

        if y_bullet < 0 or y_monkey <= r_monkey:
            print("no hit")
            t_hit = -1
            break
        elif ((x_monkey - x_bullet)**2 + (y_monkey - y_bullet)**2 < r_monkey**2 ):
            print("hit")
            t_hit = t
            break

        t += dt

if t_hit != -1:
    vx_bullet = v_bullet * math.cos(math.pi * ang_bullet / 180)
    vy_bullet = v_bullet * math.sin(math.pi * ang_bullet / 180) - G * t_hit
    vy_monkey = -G * t_hit
    V_x = m_bullet * vx_bullet / (m_bullet + m_monkey)
    V_y = (m_bullet * vy_bullet + m_monkey * vy_monkey) / (m_bullet + m_monkey)

    with open("monkey_hunting.txt", "a") as ofs:
        t = 0.1
        while True:
            X = V_x * t
            Y = V_y * t - 0.5 * G * t * t

            ofs.write(f"{t + t_hit} {x_bullet + X} {y_bullet + Y} {x_monkey + X} {y_monkey + Y}\n")

            if y_monkey + Y <= r_monkey:
                break

            t += dt