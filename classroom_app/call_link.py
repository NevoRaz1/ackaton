import uuid


def create_room_url():
    room = f"google/{uuid.uuid4().hex[:12]}"
    return f"https://meet.jit.si/{room}"
