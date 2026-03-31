import os
import smtplib
from pathlib import Path
from dotenv import load_dotenv


def clean(value: str) -> str:
    return (value or "").strip().strip("\"'")


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    load_dotenv(repo_root / ".env")

    host = clean(os.getenv("CONTACT_SMTP_HOST", ""))
    port = int(clean(os.getenv("CONTACT_SMTP_PORT", "587")) or "587")
    user = clean(os.getenv("CONTACT_SMTP_USER", ""))
    password = clean(os.getenv("CONTACT_SMTP_PASSWORD", "")).replace(" ", "")

    print(f"host={host!r} port={port} user={user!r} pw_len={len(password)}")

    with smtplib.SMTP(host, port, timeout=20) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(user, password)

    print("SMTP_LOGIN_OK")


if __name__ == "__main__":
    main()

