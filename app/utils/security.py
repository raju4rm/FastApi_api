import bcrypt

def hash_password(password: str) -> str:
    # bcrypt works with bytes
    password_bytes = password.encode("utf-8")

    # gensalt default cost = 12 (secure)
    salt = bcrypt.gensalt()

    hashed = bcrypt.hashpw(password_bytes, salt)

    # store as string in DB
    return hashed.decode("utf-8")


def verify_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(
        password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )
