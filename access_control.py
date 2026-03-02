# access_control.py

def audit_log(func):
    def wrapper(*args, **kwargs):
        print("Authorization Started")
        result = func(*args, **kwargs)
        print("Authorization Completed")
        return result
    return wrapper

def compute_access_level(control, artist_length):
    return (control * 3) + artist_length

@audit_log
def validate_access(level, threshold):
    if level >= threshold:
        return "ACCESS GRANTED"
    else:
        return "ACCESS DENIED"