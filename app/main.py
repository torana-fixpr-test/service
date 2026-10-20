"""Issue and verify signed tokens. The dependency (pyjwt) comes from the base image."""
import os
import sys

import jwt

SECRET = os.environ.get("TOKEN_SECRET", "dev-only-secret")


def issue(subject: str) -> str:
    return jwt.encode({"sub": subject}, SECRET, algorithm="HS256")


def verify(token: str) -> dict:
    return jwt.decode(token, SECRET, algorithms=["HS256"])


if __name__ == "__main__":
    tok = issue(sys.argv[1] if len(sys.argv) > 1 else "demo")
    print(tok)
    print(verify(tok))
