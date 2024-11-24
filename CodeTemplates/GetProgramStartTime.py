from datetime import datetime

# IIFE
# lambda decorator
@lambda func: func()
def program_start_time() -> str:
    now: datetime = datetime.now()
    return f'{now:%c}'

print(program_start_time)
