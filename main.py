import colorama
import subprocess
import time
import os
import sys

# option selection
print(colorama.Fore.LIGHTBLUE_EX + "[1] DNS Flush (One Time)")
print("[2] DNS Flush (Flushes DNS every 10 seconds.)")
print("[3] Check ping")
print("[4] Check ping with DNS Flush \n")
option = int(input("Select an option: "))


# functions
def flush_dns():
    subprocess.run(["ipconfig", "/flushdns"], capture_output=True)


def clear_screen():
    os.system("cls")


def check_ping():
    ping_cmd = str(subprocess.run(["ping", "mco.cubecraft.net"], capture_output=True))
    ping = ping_cmd[185:195]
    # remove non-numbers
    ping = ''.join([i for i in ping if i.isdigit()])
    # check if there is not an internet connection
    if ping == "":
        return f"{colorama.Fore.LIGHTRED_EX} No internet connection."
    else:
        return f"{colorama.Fore.LIGHTBLUE_EX} Ping: {ping}ms"


# selection for options

if option == 1:
    try:
        flush_dns()
        print("Flushed DNS!")
    except Exception as e:
        print(f"There was an error while flushing dns: {e}")

elif option == 2:
    print("Flushing DNS...")
    while True:
        try:
            flush_dns()
        except Exception as e:
            print(f"There was an error while flushing dns: {e}")
        time.sleep(10)

elif option == 3:
    clear_screen()
    while True:
        sys.stdout.write(f"\r{check_ping()}")
        sys.stdout.flush()
        time.sleep(3)

elif option == 4:
    clear_screen()
    while True:
        flush_dns()
        for p in range(3):
            sys.stdout.write(f"\r{check_ping()}")
            sys.stdout.flush()
            time.sleep(3.33)
else:
    print("Invalid option selected.")
