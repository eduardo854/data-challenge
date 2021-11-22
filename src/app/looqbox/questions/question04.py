from src.db.mysql.proccess import Extraction


def run():
    sql = """
      SELECT dss.STORE_CODE AS store_code,
             dsc.STORE_NAME AS store_name,
             dss.DATE AS date,
             sum(dss.SALES_QTY) AS sales_qty
        FROM looqbox_challenge.data_store_sales dss
        JOIN looqbox_challenge.data_store_cad dsc ON dss.STORE_CODE = dsc.STORE_CODE
       GROUP BY dss.date,
                dss.store_code,
                dsc.store_name
       ORDER BY sales_qty DESC
       LIMIT 1;            
    """
    results = Extraction(question=' 4) Which store sold the most products in one day? Which day? ',
                         query=sql).extraction_datas()

    return results


