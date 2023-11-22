# src/product/infrastructure/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
import logging


class DatabaseConfiguration:
    _instance = None
    DATABASE_URL = "XXXXXXXXXXXXXXXXXX"

    def __new__(cls):
        """
            Singleton Database Configuration
        """
        logging.info("DatabaseConfiguration::__new__::start")
        if cls._instance is None:
            cls._instance = super(DatabaseConfiguration, cls).__new__(cls)
            try:
                cls._instance._initialize()
            except OperationalError as e:
                logging.error(f" DatabaseConfiguration:: Error connections : {e}")
        logging.info("DatabaseConfiguration::__new__::end")
        return cls._instance

    def _initialize(self):
        """
            _initialize
        """
        logging.info("DatabaseConfiguration::_initialize::start")
        logging.info(self.DATABASE_URL)
        self.engine = create_engine(self.DATABASE_URL)
        logging.info("create_engine")
        self.session_maker = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        logging.info("DatabaseConfiguration::_initialize::end")

    def get_session(self):
        """
        Get the session.

        Returns:
            SessionLocal: The database session.
        """
        logging.info("DatabaseConfiguration::get_session::start")
        return self.session_maker()
