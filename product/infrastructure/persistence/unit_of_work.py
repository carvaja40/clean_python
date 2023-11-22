import logging

from product.infrastructure.factory_infra import InfraFactory


class UnitOfWork:

    def __init__(self):
        logging.info("UnitOfWork:__init__::start")
        self.session_maker = InfraFactory.create_data_config().get_session

    def __enter__(self):
        logging.info("UnitOfWork:__enter__::start")
        self.session = self.session_maker()
        return self

    def __exit__(self, exc_type, exc_val, traceback):
        logging.info("__exit__::start")
        logging.info("__exit__::end")

    def commit(self):
        logging.info("UnitOfWork:commit::start")
        self.session.commit()

    def rollback(self):
        self.session.rollback()

    def close(self):
        self.session.close()
