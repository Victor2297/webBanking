import logging
from importlib import reload

class GetLogs:
    @staticmethod
    def get_logs():
        reload(logging)
        logging.basicConfig(filename='../Logs\login.log',
                            filemode='w',
                            level=logging.DEBUG)
        logger = logging.getLogger()
        return logger