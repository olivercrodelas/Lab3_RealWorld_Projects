# main.py
import access_control
import media_engine

SEED_NUM = 2
CONTROL_NUM = max(1, SEED_NUM)
FAVORITE_ARTIST = "Ariana Grande" 
ARTIST_LENGTH = len(FAVORITE_ARTIST)

print("\n=== EXERCISE 1: ACCESS CONTROL ===")
access_level = access_control.compute_access_level(CONTROL_NUM, ARTIST_LENGTH)
threshold = CONTROL_NUM * 5
decision = access_control.validate_access(access_level, threshold)

print(f"Access Level: {access_level}")
print(f"Threshold: {threshold}")
print(f"Decision: {decision}")

print("\n=== EXERCISE 2: SIGNAL SHUTDOWN ===")

def auth_log(func):
    def wrapper(*args, **kwargs):
        print("Authorization Started")
        result = func(*args, **kwargs)
        print("Authorization Completed")
        return result
    return wrapper

@auth_log
def signal_shutdown(power, calls=0):
    print(f"Current signal strength: {power}")
    if power == 0:
        return calls
    return signal_shutdown(power - 1, calls + 1)

initial_power = CONTROL_NUM + ARTIST_LENGTH
total_calls = signal_shutdown(initial_power)
print(f"Total Recursive Calls: {total_calls}")

print("\n=== EXERCISE 3: MEDIA ENGINE ===")
stream_limit = CONTROL_NUM + ARTIST_LENGTH

@media_engine.monitor
def process_stream(limit):
    plays = list(media_engine.play_count_stream(limit))
    return plays

generated_plays = process_stream(stream_limit)
total_plays = sum(generated_plays)
records_processed = len(generated_plays)

print(f"Generated Play Counts: {generated_plays}")
print(f"Total Plays: {total_plays}")
print(f"Number of Records Processed: {records_processed}")
