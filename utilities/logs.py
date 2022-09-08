import logging
from importlib import reload

class GetLogs:
    @staticmethod
    def get_logs(file_name):
        reload(logging)
        logging.basicConfig(filename=f'../web_banking/Logs/{file_name}.log',
                            filemode='w',
                            level=logging.DEBUG)
        logger = logging.getLogger()
        return logger