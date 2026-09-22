

"""

Project 1: Projectile Motion Simulator
বিষয়: Physics + Math | লেভেল: Basic Python

এই স্ক্রিপ্টটা ৫টা ধাপে ভাগ করা। প্রতিটা ধাপ একটা function।
নিচ থেকে উপরে না পড়ে, উপর থেকে নিচে পড়ুন - main() function-টাই
সব ধাপকে একসাথে জোড়া দেয়।
"""

import math
import matplotlib.pyplot as plt


# ----------------------------------------------------------------
# ধাপ ১: শুরুর বেগ (v) ও কোণ (angle) থেকে vx, vy বের করা
# ----------------------------------------------------------------
def get_components(v, angle_deg):
    """
    v         : শুরুর বেগ (m/s)
    angle_deg : ছোঁড়ার কোণ (ডিগ্রিতে, যেমন 45)

    রিটার্ন করে (vx, vy) - অনুভূমিক ও উলম্ব বেগ
    """
    angle_rad = math.radians(angle_deg)  # ডিগ্রি -> রেডিয়ান
    vx = v * math.cos(angle_rad)
    vy = v * math.sin(angle_rad)
    return vx, vy


# ----------------------------------------------------------------
# ধাপ ২: বাতাসে থাকার মোট সময় (Time of Flight)
# ----------------------------------------------------------------
def time_of_flight(vy, g=9.8):
    """সূত্র: T = 2 * vy / g"""
    return 2 * vy / g


# ----------------------------------------------------------------
# ধাপ ৩: সর্বোচ্চ উচ্চতা (Max Height)
# ----------------------------------------------------------------
def max_height(vy, g=9.8):
    """সূত্র: H = vy^2 / (2 * g)"""
    return (vy ** 2) / (2 * g)


# ----------------------------------------------------------------
# ধাপ ৪: পুরো trajectory (path)-এর (x, y) বিন্দুগুলো বের করা
# ----------------------------------------------------------------
def trajectory(vx, vy, g=9.8, dt=0.01):
    """
    dt = ছোট time step (সেকেন্ড)। এই লুপ ধরে ধরে t = 0, dt, 2*dt, ...
    সময়ে বস্তুর অবস্থান হিসাব করে, যতক্ষণ না বস্তু মাটিতে (y <= 0) পড়ে।

    রিটার্ন করে দুটো list: x_points, y_points
    """
    x_points = []
    y_points = []

    t = 0.0
    while True:
        x = vx * t
        y = vy * t - 0.5 * g * (t ** 2)

        if y < 0:  # বস্তু মাটির নিচে চলে গেলে লুপ থামাও
            break

        x_points.append(x)
        y_points.append(y)
        t += dt

    return x_points, y_points


# ----------------------------------------------------------------
# ধাপ ৫: গ্রাফ আঁকা
# ----------------------------------------------------------------
def plot_trajectory(x_points, y_points, angle_deg, v):
    plt.figure(figsize=(8, 5))
    plt.plot(x_points, y_points, linewidth=2, color="#2563eb")
    plt.title(f"Projectile Motion (v = {v} m/s, angle = {angle_deg} deg)")
    plt.xlabel("Horizontal Distance (m)")
    plt.ylabel("Height (m)")
    plt.grid(True, alpha=0.3)
    plt.axhline(0, color="black", linewidth=0.8)
    plt.savefig("projectile_motion_plot.png", dpi=150, bbox_inches="tight")
    print("গ্রাফ সেভ হয়েছে: projectile_motion_plot.png")


# ----------------------------------------------------------------
# সব ধাপ একসাথে চালানো
# ----------------------------------------------------------------
def main():
    # --- এখানে বেগ ও কোণ বদলে বদলে চেষ্টা করুন ---
    v = 30          # m/s
    angle_deg = 45  # degree
    g = 9.8         # m/s^2

    vx, vy = get_components(v, angle_deg)

    T = time_of_flight(vy, g)
    H = max_height(vy, g)
    R = vx * T  # Range = vx * total time

    print(f"শুরুর বেগ: {v} m/s, কোণ: {angle_deg} ডিগ্রি")
    print(f"অনুভূমিক বেগ vx = {vx:.2f} m/s")
    print(f"উলম্ব বেগ vy    = {vy:.2f} m/s")
    print(f"সময়কাল (T)     = {T:.2f} সেকেন্ড")
    print(f"সর্বোচ্চ উচ্চতা (H) = {H:.2f} মিটার")
    print(f"পাল্লা (R)      = {R:.2f} মিটার")

    x_points, y_points = trajectory(vx, vy, g)
    plot_trajectory(x_points, y_points, angle_deg, v)


if __name__ == "__main__":
    main()