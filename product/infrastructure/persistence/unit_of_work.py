import logging
from product.infrastructure.factory.factory_infra import InfraFactory


class UnitOfWork:
    """
            Manages a unit of work for database operations.

            Attributes:
                session_maker: A function that creates a database session.

            Methods:
                __init__():
                    Initializes the UnitOfWork instance.

                __enter__():
                    Enters the unit of work context, creating a database session.

                __exit__(exc_type, exc_val, traceback):
                    Exits the unit of work context, committing or rolling back changes based on exceptions.

                commit():
                    Commits the changes made during the unit of work.

                rollback():
                    Rolls back the changes made during the unit of work.

                close():
                    Closes the database session.
    """

    def __init__(self):
        logging.info("UnitOfWork:__init__::start")
        self.session_maker = InfraFactory.create_data_config().get_session

    def __enter__(self):
        logging.info("UnitOfWork:__enter__::start")
        self.session = self.session_maker()
        return self

    def __exit__(self, exc_type, exc_val, traceback):
        """
               Exits the unit of work context, committing or rolling back changes based on exceptions.

               Args:
                   exc_type: The type of exception, if any.
                   exc_val: The exception value, if any.
                   traceback: The traceback object.

        """
        logging.info("__exit__::start")
        if exc_type is not None:
            self.rollback()
            self.session.close()
        self.session.close()
        logging.info("__exit__::end")

    def commit(self):
        logging.info("UnitOfWork:commit::start")
        self.session.commit()

    def rollback(self):
        self.session.rollback()

    def close(self):
        self.session.close()
