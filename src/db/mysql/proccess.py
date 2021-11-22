import json
from datetime import datetime
import pandas as pd
from src.db.mysql.connection import new_connection as conn_mysql
from src.lib.logs.logs_system import log_manager

logger = log_manager(name='process', filename='process.log', log_level='INFO')


class Extraction:

    def __init__(self, **kwargs):
        self.args = kwargs

    def extraction_datas(self):
        start_dh = datetime.now()
        
        extract_mysql(question=self.args['question'], query=self.args['query'])

        final_dh = datetime.now()

        tempo_total = str(final_dh - start_dh)

        return json.dumps({'content': {'question': self.args['question'], 'tempo_total': tempo_total}})


def extract_mysql(**kwargs):
    with conn_mysql() as conn:
        try:
            result_dataFrame = pd.read_sql(kwargs['query'], conn)
        except Exception as error:
            logger.error(error)

        print("\n\n", kwargs['question'], "\n")
        print(" Consult: ")
        print(kwargs['query'])
        print(" Result: \n")
        print("Index", result_dataFrame, "\n")