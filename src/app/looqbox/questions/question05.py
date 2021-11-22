from src.db.mysql.proccess import Extraction


def run():
    sql = """
      SELECT dsc.business_code AS business_code,
             dsc.business_name AS business_name,
             SUM(dsl.sales_value) as total_sale_products
        FROM looqbox_challenge.data_store_sales dsl
        JOIN looqbox_challenge.data_store_cad dsc ON dsl.store_code = dsc.store_code
       WHERE YEAR(dsl.date) = 2019
         AND QUARTER(dsl.date) = 1
       GROUP BY dsc.business_code,
                dsc.business_name;
    """
    results = Extraction(question=' 5) **Bonus!!** What was the total sale of products (in $) of each business area in the first quarter of 2019? ',
                         query=sql).extraction_datas()

    return results


