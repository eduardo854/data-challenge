import json
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from src.db.mysql.connection import new_connection as conn_mysql
from src.lib.logs.logs_system import log_manager

import matplotlib.dates as mdates
from datetime import datetime


logger = log_manager(name='process_graph', filename='process_graph.log', log_level='INFO')


class Graph:

    def __init__(self, **kwargs):
        self.args = kwargs

    def horizontal_bar_chart(self):
        start_dh = datetime.now()
                
        with conn_mysql() as conn:
            try:
                result_dataFrame = pd.read_sql(self.args['query'], conn)
            except Exception as error:
                logger.error(error)
                
        print("\n\n", self.args['title'], "\n")
        print("Explain - ", self.args['explain'], "\n")
        print(" Consult: ")
        print(self.args['query'])
        print(" Result: \n")
        print(f" Index {result_dataFrame}")
        
        plt.barh(result_dataFrame['title'], result_dataFrame['votes'])

        plt.xticks(rotation=70) 

        plt.xlabel('Votes') 
        plt.ylabel('Films') 
        plt.title(self.args['title'])
        
        plt.show()

        final_dh = datetime.now()
        

        tempo_total = str(final_dh - start_dh)

        return json.dumps({'content': {'graph': self.args['title'], 'tempo_total': tempo_total}})

    def histogram_chart(self):
        start_dh = datetime.now()
                
        with conn_mysql() as conn:
            try:
                result_dataFrame = pd.read_sql(self.args['query'], conn)
            except Exception as error:
                logger.error(error)

        print("\n\n", self.args['title'], "\n")
        print("Explain - ", self.args['explain'], "\n")
        print(" Consult: ")
        print(self.args['query'])
        print(" Result: \n")
        print("Index", result_dataFrame, "\n")
        
        plt.hist(x=list(result_dataFrame['bin_meta']),
                 bins=list(result_dataFrame['bin_meta']),
                 weights=list(result_dataFrame['tot'])
        )

        plt.xlabel('Scores')
        plt.ylabel('Frequency')
        plt.title(self.args['title'])
        plt.show()

        final_dh = datetime.now()
        

        tempo_total = str(final_dh - start_dh)

        return json.dumps({'content': {'graph': self.args['title'], 'tempo_total': tempo_total}})


    def timeline_chart(self):
        start_dh = datetime.now()
                
        with conn_mysql() as conn:
            try:
                result_dataFrame = pd.read_sql(self.args['query'], conn)
            except Exception as error:
                logger.error(error)

        print("\n\n", self.args['title'], "\n")
        print("Explain - ", self.args['explain'], "\n")
        print(" Consult: ")
        print(self.args['query'])
        print(" Result: \n")
        print("Index", result_dataFrame, "\n")
        
        
        levels = np.tile([-4, 4, -4, 4, -4, 4],
            int(np.ceil(len(result_dataFrame)/6))
        )[:len(result_dataFrame)]

        fig, ax = plt.subplots(figsize=(12.8, 4), constrained_layout=True)
        ax.set(title=self.args['title'])

        ax.vlines(result_dataFrame['year'], 0, levels, color="tab:red") 
        ax.plot(
            result_dataFrame['year'],
            np.zeros_like(result_dataFrame['year']),
            "-o",
            color="k",
            markerfacecolor="w"
        );

        for d, l, r in zip(result_dataFrame['year'], levels, result_dataFrame['title']):
            ax.annotate(
                r,
                xy=(d, l),
                xytext=(-3, np.sign(l)*3),
                textcoords="offset points",
                horizontalalignment="right",
                verticalalignment="bottom" if l > 0 else "top"
            );

        ax.yaxis.set_visible(False);
        ax.yaxis.set_visible(False);
        ax.spines["left"].set_visible(False)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)    
        ax.margins(y=0.1);
               
        plt.show();
        
        final_dh = datetime.now()
        

        tempo_total = str(final_dh - start_dh)

        return json.dumps({'content': {'graph': self.args['title'], 'tempo_total': tempo_total}})