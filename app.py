
import os
import sqlite3
import hashlib
import secrets

# Fix 1: Read password from environment variable
password = os.environ["APP_PASSWORD"]

# Fix 2: Use secure password hashing (scrypt)
salt = secrets.token_bytes(16)

user_hash = hashlib.scrypt(
    password.encode(),
    salt=salt,
    n=16384,
    r=8,
    p=1
)

# Fix 3: Use parameterized SQL query
def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username = ?",
        (username,)
    )

    result = cursor.fetchall()
    conn.close()
    return result

# Fix 4: Removed unsafe eval()
# Do not execute arbitrary user input as Python code.

print("Application security improvements applied")

