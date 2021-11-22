from src.db.mysql.process_graph import Graph


def run():
    sql = """
      SELECT mov.title as title,
             mov.votes as votes
        FROM looqbox_challenge.IMDB_movies mov
       WHERE mov.year = 2016
       ORDER BY mov.votes DESC
       LIMIT 10;           
    """
    results = Graph(title='Top 10 voting films in 2016:',
                    explain= 'For the first chart I chose a bar model because it is the most classic and easy to interpret. The idea here was to illustrate in a simple way the TOP 10 most voted movies of 2016.',
                    query=sql).horizontal_bar_chart()

    return results


