import argparse
import time

def launch_client(*args: str) -> None:
    print("Starting...")
    time.sleep(5)  # Pauses execution for 5 seconds
    print("Done!")

    parser = argparse.ArgumentParser()
    parser.add_argument("--connect")
    parser.add_argument("--password")
    parser.add_argument("--name")
    parser.add_argument("url", nargs="?")

    args = parser.parse_args()
    print(args)