import colorama
import subprocess
import time
import os
import sys

#option selection
print(colorama.Fore.LIGHTBLUE_EX + "[1] DNS Flush (One Time)")
print("[2] DNS Flush (Flushes DNS every second.)")
print("[3] Check ping")
print("[4] Check ping with DNS Flush \n")
option = int(input("Select an option: "))
#functions
def flush_dns():
    subprocess.run(["ipconfig", "/flushdns"], capture_output=True)

def clear_screen():
    os.system("cls")
def check_ping():
    ping_cmd = str(subprocess.run(["ping", "mco.cubecraft.net"], capture_output=True))
    return ping_cmd[190:194]
if option == 1:
    try:
        flush_dns()
        print("Flushed DNS!")
    except:
        sys.exit("Something went wrong.")

elif option == 2:
    print("Flushing DNS...")
    while True:
        try:
            flush_dns()
        except:
            sys.exit("Something went wrong.")
        time.sleep(1)
elif option == 3:
    clear_screen()
    while True:
        sys.stdout.write(f"\rPing: {check_ping()}")
        sys.stdout.flush()
        time.sleep(3)
elif option == 4:
    while True:
        flush_dns()
        sys.stdout.write(f"\rPing: {check_ping()}")
        sys.stdout.flush()
        time.sleep(3)
else:
    print("Invalid Option Selected.")