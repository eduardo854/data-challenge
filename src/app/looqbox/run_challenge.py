import concurrent.futures
from src.lib.logs.logs_system import log_manager
from datetime import datetime
from time import time
from src.app.looqbox.questions import question01, question02, question03, question04, question05
from src.app.looqbox.graphs import graph01, graph02, graph03

logger = log_manager(name='challenge', filename='challenge.log', log_level='INFO')

questions = [question01, question02, question03, question04, question05]


def run_challenge():

    start = time()
    logger.info(f'-----------------------CHALLENGE-----------------------')

    with concurrent.futures.ThreadPoolExecutor() as executor:

        logger.info(f'Running graphs: ')
        results_questions = [executor.submit(quest)
                          for quest in questions]
        for future in concurrent.futures.as_completed(results_questions):
            logger.info(future.result())
        
        logger.info("\n The goal of visualizing data is to make it easier to understand and read. Having multiple simple graphs is always better than one elaborate graph! \n")

        logger.info(f'Running Graph 01...')
        graph01()
        
        logger.info(f'Running Graph 02...')
        graph02()
        
        logger.info(f'Running Graph 03...')
        graph03()

        final = time()
        logger.info(f'Fim: {datetime.fromtimestamp(final)}')
        logger.info(f'Tempo Total: {datetime.fromtimestamp(final) - datetime.fromtimestamp(start)}')


if __name__ == "__main__":
    run_challenge()
