from contextlib import contextmanager
import MySQLdb

try:
    from MySQLdb import connect, ProgrammingError, DatabaseError, InternalError, OperationalError
except ImportError as error:
    print(f"""
        Biblioteca mysql não encontrada.
        Favor entrar em contato com o administrador do sistema.
    """)

from src.lib.logs.logs_system import log_manager

logger = log_manager(name='connection', filename='connection.log', log_level='INFO')


parameters = dict(
    host='localhost',
    user='admin',
    passwd='admin',
    port=3306,
    db='challenge'
)


@contextmanager
def new_connection():
    try:
        conn = MySQLdb.Connection(**parameters)
    except OperationalError as error:
        raise SystemExit(error)
    except DatabaseError as error:
        raise SystemExit(error)
    except InternalError as error:
        raise SystemExit(error)

    try:
        yield conn
    except DatabaseError as error:
        logger.error(error)
        raise SystemExit(error)
    except ProgrammingError as error:
        raise SystemExit(error)
    finally:
        conn.close()

