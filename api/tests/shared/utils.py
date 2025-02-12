import uuid

def is_valid_guid(value: str) -> bool:
    try:
        uuid.UUID(value, version=4) # Version 4 UUID (random)
        return True
    except ValueError:
        return False