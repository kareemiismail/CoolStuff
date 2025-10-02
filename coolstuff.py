import os, sys, time, math, random
import colorama
from colorama import Fore, Back, Style

colorama.init()

# ========= SPLASH =========
def splash_screen():
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.CYAN + Style.BRIGHT + "\n" + "="*40)
    print(Fore.MAGENTA + Style.BRIGHT + "        Made by whyfi 💻✨")
    print(Fore.CYAN + Style.BRIGHT + "="*40 + "\n")
    time.sleep(2)

# ========= EFFECTS =========
def spinning_donut():
    A,B=0,0
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        z=[0]*1760
        b=[' '] *1760
        for j in range(0,628,7):
            for i in range(0,628,2):
                c=math.sin(i)
                d=math.cos(j)
                e=math.sin(A)
                f=math.sin(j)
                g=math.cos(A)
                h=d+2
                D=1/(c*h*e+f*g+5)
                l=math.cos(i)
                m=math.cos(B)
                n=math.sin(B)
                t=c*h*g-f*e
                x=int(40+30*D*(l*h*m-t*n))
                y=int(12+15*D*(l*h*n+t*m))
                o=int(x+80*y)
                N=int(8*((f*e-c*d*g)*m-c*d*e-f*g-l*d*n))
                if 1760>o>0 and D>z[o]:
                    z[o]=D
                    b[o]=".,-~:;=!*#$@"[N if N>0 else 0]
        print('\x1b[H'+''.join(b))
        A+=0.04
        B+=0.08
        time.sleep(0.03)

def spinning_cube():
    A = 0
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        z = [0]*1760
        b = [' '] *1760
        for k in range(0,628,7):
            for i in range(0,628,2):
                x = math.sin(i)*math.cos(k)
                y = math.sin(i)*math.sin(k)
                z0 = math.cos(i)
                x1 = x*math.cos(A)-z0*math.sin(A)
                z1 = x*math.sin(A)+z0*math.cos(A)
                y1 = y
                xp = int(40 + 20*x1)
                yp = int(12 + 10*y1)
                o = xp + 80*yp
                if 0 <= o < 1760:
                    b[o] = '#'
        print('\x1b[H'+''.join(b))
        A += 0.05
        time.sleep(0.03)

def wave_animation():
    for t in range(60):
        os.system("cls" if os.name == "nt" else "clear")
        line = "".join(
            Fore.CYAN + ( "~" if (i+t)%6<3 else " " )
            for i in range(60)
        )
        print("🌊 " + line)
        time.sleep(0.1)

def ascii_fireworks():
    for _ in range(20):
        os.system("cls" if os.name == "nt" else "clear")
        for _ in range(10):
            x = " " * random.randint(0,50) + random.choice(["*", "+", "x", "o"])
            print(Fore.RED + x)
        time.sleep(0.2)

# Simple maze generator
def mouse_maze(width=20, height=10):
    maze = [["#" for _ in range(width)] for _ in range(height)]
    for y in range(1, height-1):
        for x in range(1, width-1):
            maze[y][x] = " " if random.random() > 0.3 else "#"
    maze[1][1] = "M"
    maze[height-2][width-2] = "E"
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.YELLOW + "Mouse Maze 🐭")
    for row in maze:
        print("".join(row))
    input(Fore.CYAN + "\nPress Enter when done...")

def confetti():
    for _ in range(40):
        os.system("cls" if os.name == "nt" else "clear")
        for _ in range(15):
            line = "".join(random.choice([
                Fore.RED+"*", Fore.GREEN+"*", Fore.YELLOW+"*", Fore.BLUE+"*"
            ]) for _ in range(40))
            print(line)
        time.sleep(0.1)

def bouncing_ball():
    w, h = 40, 10
    x, y, dx, dy = 5, 3, 1, 1
    for _ in range(80):
        os.system("cls" if os.name == "nt" else "clear")
        for j in range(h):
            row = ""
            for i in range(w):
                row += "O" if (i,j)==(x,y) else "."
            print(row)
        x += dx; y += dy
        if x<=0 or x>=w-1: dx *= -1
        if y<=0 or y>=h-1: dy *= -1
        time.sleep(0.05)

def spiral():
    size = 20
    for t in range(size):
        os.system("cls" if os.name == "nt" else "clear")
        print(Fore.MAGENTA+"Spiral Frame",t)
        for i in range(t):
            print(" " * i + "*")
        time.sleep(0.1)

def snake():
    body = list(range(10))
    for step in range(30):
        os.system("cls" if os.name == "nt" else "clear")
        line = ""
        for i in range(30):
            if i in body: line += Fore.GREEN+"#"
            else: line += " "
        print(line)
        body = [x+1 for x in body]
        time.sleep(0.1)

def tunnel():
    for r in range(1, 20):
        os.system("cls" if os.name == "nt" else "clear")
        print(Fore.CYAN+"Tunnel depth",r)
        print(" " * r + "####")
        time.sleep(0.1)

def starfield():
    for _ in range(40):
        os.system("cls" if os.name == "nt" else "clear")
        for _ in range(10):
            print(" " * random.randint(0,50) + Fore.WHITE + "*")
        time.sleep(0.1)

def heartbeat():
    for _ in range(10):
        os.system("cls" if os.name == "nt" else "clear")
        print(Fore.RED + "  **   **  ")
        print(Fore.RED + " ****** ** ")
        print(Fore.RED + "  ******   ")
        print(Fore.RED + "   ****    ")
        time.sleep(0.3)
        os.system("cls" if os.name == "nt" else "clear")
        time.sleep(0.2)

def spinner():
    symbols = "|/-\\"
    for i in range(40):
        os.system("cls" if os.name == "nt" else "clear")
        print(Fore.YELLOW + "Loading... " + symbols[i%4])
        time.sleep(0.1)

def typing_effect():
    text = "Hello from whyfi!"
    out = ""
    for c in text:
        out += c
        os.system("cls" if os.name == "nt" else "clear")
        print(Fore.GREEN + out)
        time.sleep(0.2)

def checkerboard():
    for _ in range(20):
        os.system("cls" if os.name == "nt" else "clear")
        for y in range(8):
            row = ""
            for x in range(16):
                if (x+y)%2==0:
                    row += Fore.BLUE+"#"
                else:
                    row += Fore.WHITE+"#"
            print(row)
        time.sleep(0.2)

# ========= MENU =========
effects = {
    "0": ("Spinning Donut", spinning_donut),
    "1": ("Spinning Cube", spinning_cube),
    "2": ("Wave Animation", wave_animation),
    "3": ("Fireworks", ascii_fireworks),
    "4": ("Mouse Maze", mouse_maze),
    "5": ("Confetti", confetti),
    "6": ("Bouncing Ball", bouncing_ball),
    "7": ("Spiral", spiral),
    "8": ("Snake", snake),
    "9": ("Tunnel", tunnel),
    "A": ("Starfield", starfield),
    "B": ("Heartbeat", heartbeat),
    "C": ("Spinner", spinner),
    "D": ("Typing Effect", typing_effect),
    "E": ("Checkerboard", checkerboard),
}

def menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(Fore.CYAN + Style.BRIGHT + "=== Cool Stuff Menu ===")
        for key,(name,_) in effects.items():
            print(Fore.YELLOW + f"[{key}] " + Fore.GREEN + name)
        print(Fore.MAGENTA + "[R] Random")
        print(Fore.RED + "[Q] Quit")
        choice = input(Fore.CYAN + "\nChoose: ").upper()
        if choice == "Q":
            break
        elif choice == "R":
            _, func = random.choice(list(effects.values()))
            func()
        elif choice in effects:
            effects[choice][1]()
        else:
            print(Fore.RED+"Invalid choice!")
            time.sleep(1)

# ========= MAIN =========
if __name__ == "__main__":
    splash_screen()
    menu()
    print(Fore.WHITE + Style.DIM + "\n(c) 2025 whyfi. All rights reserved.")
