
import logging


class LogWriter:
    def __init__(self,name) -> None:

        self.name = name

        logging.basicConfig(filename='./app.log',level=logging.WARNING)

        self.logger = logging.getLogger(__name__)


    def log_info(self,message: str):
        self.logger.info(message)

    def log_debug(self,message: str):
        self.logger.debug(message)

    def log_warning(self,message: str):
        self.logger.warning(message)

    def log_error(self,message: str):
        self.logger.error(message)

    def log_critical(self,message: str):
        self.logger.critical(message)
