import sqlite3
from unicodedata import category
from newspaper import Article
import newspaper

def getALL(query):
    conn = sqlite3.connect("data/newsdb.db")
    data = conn.execute(query).fetchall()
    conn.close()
    return data

# lay chi tiet bai bao theo category
def getNewsByID(newsID):
    conn = sqlite3.connect("data/newsdb.db")
    sql = '''
    SELECT N.subject, N.description, N.image, N.original_url, C.name, C.url
    FROM news N INNER JOIN category C ON N.category_id = C.id
    WHERE N.id=?
    '''
    news = conn.execute(sql, (newsID, )).fetchone()
    conn.close()
    
    return news



# them comment vao bai bao
def addComment(newsID, content):
    conn = sqlite3.connect("data/newsdb.db")
    sql = '''
    INSERT INTO comment(content, news_id) VALUES (?, ?)
    '''
    conn.execute(sql, (content, newsID))
    conn.commit()
    conn.close()



# add bai bao moi
def addNews(conn, url, category_id):
    sql = """
    INSERT INTO news(subject, description, image, original_url, category_id)
    VALUES (?, ?, ?, ?, ?)
    """
    article = Article(url)
    article.download()
    article.parse() 

    # thuc thi 
    conn.execute(sql, (article.title, article.text, article.top_image, article.url, category_id))
    conn.commit()

# lay url cua bai bao
def getNewsUrl():
    cats = getALL("SELECT * FROM category")
    

    conn = sqlite3.connect("data/newsdb.db")
    for cat in cats:
        cat_id = cat[0] 
        url = cat[2]
        # build newspaper
        cat_paper = newspaper.build(url)
        # duyet qua ca url cua bai bao
        for article in cat_paper.articles:
            try:
                print("===", article.url)
                addNews(conn, article.url, cat_id)
            except Exception as ex:
                print("ERROR: " + str(ex))
                pass

    conn.close()


if __name__ == "__main__":
    getNewsUrl()