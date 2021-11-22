from src.db.mysql.process_graph import Graph


def run():
    sql = """
      SELECT IFNULL(floor(mov.metascore/10)*10, 0) as bin_meta,
             count(*) as tot
        FROM looqbox_challenge.IMDB_movies mov
       GROUP BY 1
       ORDER BY 1;
    """
    results = Graph(title='Most frequent movie scores',
                    explain= 'In the second chart I wanted to illustrate the frequency of film scores. The histogram is an ideal chart for summarizing a large amount of data. Since we have a list with 1000 movies, I thought it would be interesting to see if there are more high or low Metascores. In this result we can see that most scores are above average, between 50 and 70.',
                    query=sql).histogram_chart()

    return results


