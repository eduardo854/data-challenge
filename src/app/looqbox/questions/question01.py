from src.db.mysql.proccess import Extraction


def run():
    sql = """
      SELECT COUNT(*) AS tot_products
        FROM looqbox_challenge.data_product dp;            
    """
    results = Extraction(question=' 1) How many products does the company have? ',
                         query=sql).extraction_datas()

    return results


