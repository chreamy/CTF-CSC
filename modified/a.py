import subprocess

# Replace "<file>" with the actual file path you want to calculate the MD5 hash for
file_path = "C:\\Users\\chris\\Desktop\\ctf challenge"

try:
    # Run the certutil command to calculate MD5 hash
    result = subprocess.run(["certutil", "-hashfile", file_path, "MD5"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check if the command executed successfully
    if result.returncode == 0:
        md5_hash = result.stdout
        print(f"MD5 hash of {file_path}: {md5_hash}")
    else:
        print("Error:", result.stderr)
except FileNotFoundError:
    print("Error: 'certutil' command not found. Make sure it's installed and in your system's PATH.")