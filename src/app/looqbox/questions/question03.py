from src.db.mysql.proccess import Extraction


def run():
    sql = """
      SELECT dp.dep_cod AS dep_cod,
             dp.dep_name AS dep_name,
             dp.SECTION_COD AS section_cod,
             dp.section_name AS section_name
        FROM looqbox_challenge.data_product dp
       WHERE dp.dep_name = 'BEBIDAS'
          OR dp.dep_name = 'PADARIA'
       GROUP BY dp.dep_cod,
                dp.dep_name,
                section_cod,
                dp.section_name
       ORDER BY 1, 3;        
    """
    results = Extraction(question=" 3) What sections do the 'BEBIDAS' and 'PADARIA' departments have? ",
                         query=sql).extraction_datas()

    return results


