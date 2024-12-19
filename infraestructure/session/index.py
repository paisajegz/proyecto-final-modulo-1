class Session:
    _id_user: int
    _type_user: str
    _first_name: str
    _last_name: str
    _email: str
    _count_buyer: int

    def __init__(
        self,
        id_user: int = 0,
        type_user: str = "",
        first_name: str = "",
        last_name: str = "",
        email: str = "",
    ) -> None:
        self._id_user = id_user
        self._type_user = type_user
        self._first_name = first_name
        self._last_name = last_name
        self._email = email

    @property
    def id_user(self):
        return self._id_user

    @id_user.setter
    def id_user(self, id_user: int):
        self._id_user = id_user

    @property
    def type_user(self):
        return self._type_user

    @type_user.setter
    def type_user(self, type_user: str):
        self._type_user = type_user

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        self._last_name = last_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email: str):
        self._email = email


class SessionProvider:
    UserSession: Session = Session()

    @staticmethod
    def set_session(session: Session) -> None:
        SessionProvider.UserSession = session

    @staticmethod
    def get_session() -> Session:
        return SessionProvider.UserSession

    @staticmethod
    def clear_sesion() -> None:
        SessionProvider.UserSession = Session()
