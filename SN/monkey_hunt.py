import math
import numpy as np
import matplotlib.pyplot as plt

G = 9.80665


def velocity_y(t, init_vy):
    vy = init_vy - G*t
    return vy


def position(t, init_x, init_y, init_vx, init_vy):
    """
    物体の位置を計算する。

    Parameters
    ----------
    t::時刻
    init_x::初期位置のx成分
    init_x::初期位置のy成分
    init_vx::初速のx成分
    init_vy::初速のy成分

    Returns
    -------
    xt::時刻tの位置のx成分
    yt::時刻tの位置のy成分
    """
    xt = init_x + init_vx * t
    yt = init_y + init_vy * t - (0.5 * G * t * t)
    return xt, yt


def calc_Vx_Vy(t, init_vx_bullet, init_vy_bullet, m_bullet, m_monkey):
    """
    衝突後の弾と猿の重心速度を計算する。

    Parameters
    ----------
    t::衝突時間
    vx_bullet::弾の初速度(t=0)のx成分
    vx_bullet::弾の初速度(t=0)のy成分
    m_bullet::弾の質量
    m_monkey::猿の質量

    Returns
    -------
    Vx::重心速度のx成分
    """
    vx_bullet = init_vx_bullet
    vy_bullet = velocity_y(t, init_vy_bullet)
    vy_monkey = velocity_y(t, 0)
    Vx = m_bullet * vx_bullet / (m_bullet + m_monkey)
    Vy = (m_bullet * vy_bullet + m_monkey * vy_monkey) / (m_bullet + m_monkey)
    return Vx, Vy

def calc_all_position(t, t_land, t_hit, 
                      vx_bullet,vy_bullet, 
                      l_monkey, h_monkey,
                      r_monkey, m_bullet, m_monkey):
    
    if t_land >= 0:
        t = t_land  

    if t_hit < 0:
        x_bullet, y_bullet = position(t, 0, 0, vx_bullet, vy_bullet)
        x_monkey, y_monkey = position(t, l_monkey, h_monkey, 0, 0)
        if (x_monkey - x_bullet)**2 + (y_monkey - y_bullet)**2 <= r_monkey**2:  # this not count x_bullet etc!
            t_hit = t
    elif t_hit >= 0:
        x_bullet, y_bullet = position(t_hit, 0, 0, vx_bullet, vy_bullet)
        x_monkey, y_monkey = position(t_hit, l_monkey, h_monkey, 0, 0)
        Vx, Vy = calc_Vx_Vy(t_hit, vx_bullet, vy_bullet, m_bullet, m_monkey)
        X, Y = position(t - t_hit, 0, 0, Vx, Vy)
        x_bullet = X + x_bullet
        y_bullet = Y + y_bullet
        x_monkey = X + x_monkey
        y_monkey = Y + y_monkey
    if y_bullet < 0 or y_monkey <= r_monkey:
        t_land = t
        
    return t_land, t_hit, x_bullet, y_bullet, x_monkey, y_monkey