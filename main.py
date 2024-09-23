from listen import *
import datetime

if __name__ == "__main__":
    try:
        listen_for_commands()
    except Exception as e: 
        print("A error occured. View the logs for this run at the logs.txt")
        with open("logs.txt", "a") as f:
            f.write(f"{datetime.datetime.now()} \n")
            f.write(f"{e}\n")

