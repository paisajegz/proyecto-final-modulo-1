import bcrypt


class Crypt:
    @staticmethod
    def encrypt_password(plain_text: str) -> str:
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(plain_text.encode("utf-8"), salt)
        return hashed.decode("utf-8")

    @staticmethod
    def verify_password(plain_text: str, hashed_text: str) -> bool:
        try:
            return bcrypt.checkpw(
                plain_text.encode("utf-8"), hashed_text.encode("utf-8")
            )
        except ValueError:
            return False
