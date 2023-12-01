from product.infrastructure.db_config.database_configuration import DatabaseConfiguration

"""
"""


class InfraFactory:

    @staticmethod
    def create_data_config() -> DatabaseConfiguration:
        """
        Method to create Data configuration
        """
        return DatabaseConfiguration()
