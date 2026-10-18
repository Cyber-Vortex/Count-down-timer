import time

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end="\r") # Ek hi line me update karne ke liye
        time.sleep(1)
        seconds -= 1
    
    print("Time's up! 🚨")

# 10 seconds ka countdown
countdown(10)
