# looqbox-data-challenge

Repository with the solution of the looqbox data-challenge


# Tools Used
    
*  Python - version 3.9.6 - Release Date: June 28, 2021 (https://www.python.org/downloads/release/python-396/) 
 
**IDE**
*  VSCode (https://code.visualstudio.com/download)

# Installation

**Python** 
* Download the performable in the maqina when opening the installation window check the Add Path option
* Click the option to install without customization
* After installation you can verify success by going on the prompt and typing **python**
* after this rotate the commands:

```
python -m pip install --upgrade pip
python -m pip install virtualenv
```

**VSCode**
* Download the IDE and install normally
* After the installation open the IDE go on **Extensions (Ctrl+Shift+X - windows )** and install the extension **Python and Python Preview**

**Virtual environment**
* Download the sources from this repository by making a clone of it

1. In the command prompt go to the directory where the project is located
2. Turn the command:

`python -m virtualenv modules`

Finishing execution run the command: 
`modules\Scripts\activate.bat` (windows)  
or `source bin\scripts\activate` (mac/linux)

so it will activate the virtual environment

3. After activation, turn the command:

`python -m pip install -r requirements.txt`, will install all the libs used in the challenge.


# Configure the connection to mysql

Change the database connection parameters in the connection.py - **src\db\mysql\connection.py**

```
    parameters = dict(
        host='localhost',
        user='admin',
        passwd='admin',
        port=3306,
        db='challenge'
    )
```

# How to run this challenge

In the terminal run:

`python -m src.app.looqbox.run_challenge`


# Execution Log

```
2021-11-22 02:39:01,250:INFO:challenge:-----------------------CHALLENGE-----------------------
2021-11-22 02:39:01,251:INFO:challenge:Running graphs:


  1) How many products does the company have?

 Consult:

      SELECT COUNT(*) AS tot_products
        FROM looqbox_challenge.data_product dp;

 Result:

Index    tot_products
0          9994

2021-11-22 02:39:01,419:INFO:challenge:{"content": {"question": " 1) How many products does the company have? ", "tempo_total": "0:00:00.167185"}}


  2) What are the 10 most expensive products in the company?

 Consult:

      SELECT dp.PRODUCT_COD AS cod_product,
             dp.PRODUCT_NAME AS name_product,
             dp.PRODUCT_VAL AS val_product
        FROM looqbox_challenge.data_product dp
       ORDER BY dp.PRODUCT_VAL DESC
       LIMIT 10;

 Result:

Index    cod_product                                       name_product  val_product
0       301409  Whisky Escoces THE MACALLAN Ruby Garrafa 700ml...       741.99
1       176185  Whisky Escoces JOHNNIE WALKER Blue Label Garra...       735.90
2       315481   Cafeteira Expresso 3 CORACOES Tres Modo Vermelho       499.00
3       100280  Vinho Portugues Tinto Vintage QUINTA DO CRASTO...       445.90
4       320046  Escova Dental Eletrica ORAL B D34 Professional...       399.90
5       190817  Champagne Rose VEUVE CLICQUOT PONSARDIM Garraf...       366.90
6       153795  Champagne Frances Brut Imperial MOET Rose Garr...       359.90
7       311397  Conjunto de Panelas Allegra em Inox TRAMONTINA...       359.00
8       147706  Whisky Escoces CHIVAS REGAL 18 Anos Garrafa 750ml       329.90
9       154431  Champagne Frances Brut Imperial MOET & CHANDON...       315.90



  3) What sections do the 'BEBIDAS' and 'PADARIA' departments have?

 Consult:

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

2021-11-22 02:39:01,445:INFO:challenge:{"content": {"question": " 2) What are the 10 most expensive products in the company? ", "tempo_total": "0:00:00.192469"}}
 Result:

Index    dep_cod dep_name  section_cod        section_name
0        2  BEBIDAS            4             BEBIDAS
1        2  BEBIDAS           29            CERVEJAS
2        2  BEBIDAS           30              VINHOS
3        2  BEBIDAS           31           REFRESCOS
4        7  PADARIA            8  DOCES-E-SOBREMESAS
5        7  PADARIA           19             PADARIA
6        7  PADARIA           22     QUEIJOS-E-FRIOS
7        7  PADARIA           27            GESTANTE

2021-11-22 02:39:01,448:INFO:challenge:{"content": {"question": " 3) What sections do the 'BEBIDAS' and 'PADARIA' departments have? ", "tempo_total": "0:00:00.195470"}}


  5) **Bonus!!** What was the total sale of products (in $) of each business area in the first quarter of 2019?

 Consult:

      SELECT dsc.business_code AS business_code,
             dsc.business_name AS business_name,
             SUM(dsl.sales_value) as total_sale_products
        FROM looqbox_challenge.data_store_sales dsl
        JOIN looqbox_challenge.data_store_cad dsc ON dsl.store_code = dsc.store_code
       WHERE YEAR(dsl.date) = 2019
         AND QUARTER(dsl.date) = 1
       GROUP BY dsc.business_code,
                dsc.business_name;

 Result:

Index    business_code business_name  total_sale_products
0              1        Varejo          81032347.65
1              2   Proximidade          80171122.80
2              3         Posto          32072326.40
3              4         Farma          81776691.73
4              5       Atacado          80384884.60

2021-11-22 02:39:01,464:INFO:challenge:{"content": {"question": " 5) **Bonus!!** What was the total sale of products (in $) of each business area in the first quarter of 2019? ", "tempo_total": "0:00:00.211020"}}


  4) Which store sold the most products in one day? Which day?

 Consult:

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

 Result:

Index    store_code store_name        date  sales_qty
0           2    Chicago  2019-07-03    24332.0

2021-11-22 02:39:01,684:INFO:challenge:{"content": {"question": " 4) Which store sold the most products in one day? Which day? ", "tempo_total": "0:00:00.430778"}}


2021-11-22 02:39:01,684:INFO:challenge:
 The goal of visualizing data is to make it easier to understand and read. Having multiple simple graphs is always better than one elaborate graph!

2021-11-22 02:39:01,684:INFO:challenge:Running Graph 01...

 Top 10 voting films in 2016:

Explain -  For the first chart I chose a bar model because it is the most classic and easy to interpret. The idea here was to illustrate in a simple way the TOP 10 most voted movies of 2016.

 Consult:

      SELECT mov.title as title,
             mov.votes as votes
        FROM looqbox_challenge.IMDB_movies mov
       WHERE mov.year = 2016
       ORDER BY mov.votes DESC
       LIMIT 10;

 Result:

 Index                                 title   votes
0                            Deadpool  627797
1  Batman v Superman: Dawn of Justice  472307
2          Captain America: Civil War  411656
3                       Suicide Squad  393727
4                             Arrival  340798
5                           Rogue One  323118
6                            Zootopia  296853
7                      Doctor Strange  293732
8                   X-Men: Apocalypse  275510
9                          La La Land  258682

```

<img src="/charts/chart01.png" alt="Top 10 voting films in 2016"/>


```
2021-11-22 02:39:02,804:INFO:challenge:Running Graph 02...

 Most frequent movie scores

Explain -  In the second chart I wanted to illustrate the frequency of film scores. The histogram is an ideal chart for summarizing a large amount of data. Since we have a list with 1000 movies, I thought it would be interesting to see if there are more high or low Metascores. In this result we can see that most scores are above average, between 50 and 70.

 Consult:

      SELECT IFNULL(floor(mov.metascore/10)*10, 0) as bin_meta,
             count(*) as tot
        FROM looqbox_challenge.IMDB_movies mov
       GROUP BY 1
       ORDER BY 1;

 Result:

Index     bin_meta  tot
0          0   64
1         10    8
2         20   29
3         30  104
4         40  145
5         50  182
6         60  196
7         70  152
8         80   96
9         90   23
10       100    1

```

<img src="/charts/chart02.png" alt="Most frequent movie scores"/>


```


2021-11-22 02:39:03,516:INFO:challenge:Running Graph 03...

 Vin Diesel movies timeline

Explain -  Finally a simple Timeline listing an actor's movies per year. In my concept, Timeline chart is one of the best ways to present data in chronological order. With this chart we can have a lot of insights as that in 2010 and 2012 Vin Diesel didn't release any movies, on the other hand, from 2013 on, he released 5 movies in 3 years.

 Consult:

      SELECT mov.title AS title,
             mov.year AS year
        FROM looqbox_challenge.IMDB_movies mov
       WHERE mov.Actors like '%Vin Diesel%'
       ORDER BY mov.year ASC;

 Result:

Index                      title  year
0           Fast & Furious  2009
1                Fast Five  2011
2                Furious 6  2013
3                  Riddick  2013
4  Guardians of the Galaxy  2014
5    The Last Witch Hunter  2015
6            Furious Seven  2015

```

<img src="/charts/chart03.png" alt="Vin Diesel movies timeline"/>


```

2021-11-22 02:39:04,164:INFO:challenge:Fim: 2021-11-22 02:39:04.164819
2021-11-22 02:39:04,165:INFO:challenge:Tempo Total: 0:00:02.914300
```