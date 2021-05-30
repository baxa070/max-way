from django.db import connection
from contextlib import closing


def get_categories():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from maxway_category""")
        categories = dictfetchall(cursor)
        return categories


def get_categories_news_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute(
            """select maxway_category.name as category, count(maxway_post.*) as count from maxway_category
            left join maxway_post on maxway_category.id = maxway_post.category_id 
            group by maxway_category.name"""
        )
        categories = dictfetchall(cursor)
        return categories

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, rows))
        for rows in cursor.fetchall()
    ]


def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))
