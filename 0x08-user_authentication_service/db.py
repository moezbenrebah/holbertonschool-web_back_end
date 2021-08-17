#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base, User

from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """returns a User object"""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """returns the first row found in the users table
        as filtered by the method’s input arguments
        """

        args = kwargs.keys()

        for key in args:
            if not hasattr(User, key):
                raise InvalidRequestError

        row = self._session.query(User).filter_by(**kwargs).first()
        if row is None:
            raise NoResultFound
        return row

    def update_user(self, user_id: int, **kwargs) -> None:
        """locate the user to update, then will update the user’s
        attributes as passed in the method’s arguments then commit
        changes to the database.
        """
        user = self.find_user_by(id=user_id)

        # get columns names from users table like keys
        valid_attr = User.metadata.tables['users'].columns.keys()

        for key, value in kwargs.items():
            if key not in valid_attr:
                raise ValueError
            else:
                setattr(user, key, value)

        self._session.commit()
