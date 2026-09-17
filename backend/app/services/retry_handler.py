from tenacity import retry, stop_after_attempt, wait_fixed

@retry(
    stop = stop_after_attempt(3),
    wait = wait_fixed(2)
)

def retry_operation(operation):
    return operation()


attempts = 0

def temporary_operation():
    global attempts
    
    attempts += 1
    print(f"Attempt {attempts}")
    
    if attempts < 3:
        raise Exception("Temporary failure")
    
    return "Success"

result = retry_operation(temporary_operation)
print(result)


