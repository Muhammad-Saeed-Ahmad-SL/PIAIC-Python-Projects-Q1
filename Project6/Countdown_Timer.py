import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)  # Convert seconds into minutes and seconds
        timer_format = f"{mins:02d}:{secs:02d}"
        print(timer_format, end="\r")  # Print the timer in the same line
        time.sleep(1)  # Wait for 1 second
        seconds -= 1

    print("⏰ Time's up!")

# Get user input for the countdown time
try:
    total_time = int(input("Enter countdown time in seconds: "))
    countdown_timer(total_time)
except ValueError:
    print("⚠️ Please enter a valid integer for seconds!")
