from src.db.mysql.process_graph import Graph


def run():
    sql = """
      SELECT mov.title AS title,
             mov.year AS year
        FROM looqbox_challenge.IMDB_movies mov
       WHERE mov.Actors like '%Vin Diesel%'
       ORDER BY mov.year ASC;         
    """
    results = Graph(title='Vin Diesel movies timeline',
                    explain= "Finally a simple Timeline listing an actor's movies per year. In my concept, Timeline chart is one of the best ways to present data in chronological order. With this chart we can have a lot of insights as that in 2010 and 2012 Vin Diesel didn't release any movies, on the other hand, from 2013 on, he released 5 movies in 3 years.",
                    query=sql).timeline_chart()

    return results


