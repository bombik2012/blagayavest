import time

USER_REQUEST_COOLDOWN = 600
_last_requests = {}

def can_send_request(user_id: int) -> bool:
    now = time.time()
    last = _last_requests.get(user_id)
    if last and now - last < USER_REQUEST_COOLDOWN:
        return False
    _last_requests[user_id] = now
    return True
