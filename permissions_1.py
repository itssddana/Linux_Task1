import os

# Specify the file
file_path = "permissions_1.py"  

# Permissions for rwxrwxr-x
permissions = 0o775  # Octal value

# Apply new permissions
os.chmod(file_path, permissions)

print(f"Updated permissions for '{file_path}' to rwxrwxr-x.")
