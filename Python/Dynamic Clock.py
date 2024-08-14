# Author : InferiorAK
# Language : Python 3.12.3
# Date : 14 Aug 2024 9:43 PM
# Dynamic Clock

import time

def main(hour, min, sec, shift):
    for hour in range(hour, 13):
        for min in range(min, 60):
            for sec in range(sec, 60):
                print(f"{hour:02}:{min:02}:{sec:02} {shift}", end="\r")
                time.sleep(1)
            

if __name__ == "__main__":
    print("InferiorAK Dynamic Clock")
    main(hour=9, min=43, sec=0, shift="PM")
