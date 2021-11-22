from src.db.mysql.proccess import Extraction


def run():
    sql = """
      SELECT dp.PRODUCT_COD AS cod_product,
             dp.PRODUCT_NAME AS name_product,
             dp.PRODUCT_VAL AS val_product
        FROM looqbox_challenge.data_product dp
       ORDER BY dp.PRODUCT_VAL DESC
       LIMIT 10;          
    """
    results = Extraction(question=' 2) What are the 10 most expensive products in the company? ',
                         query=sql).extraction_datas()

    return results


