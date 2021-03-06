from django.db import connection
from contextlib import closing


def get_status_info(status):
    with closing(connection.cursor()) as cursor:
        cursor.execute(f"""select maxway_delilveryinfo.*, maxway_order.status as status
            from maxway_delilveryinfo left join maxway_order 
            on maxway_delilveryinfo.order_id = maxway_order.id where status in ({str(status).strip("[]")}) """
                       )
        status = dict_fetchall(cursor)
    return status


def get_status_1():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(status) from maxway_order where status = 1""")
        status = dict_fetchall(cursor)
    return status


def get_status_2():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(status) from maxway_order where status = 2""")
        status = dict_fetchall(cursor)
    return status


def get_status_3():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(status) from maxway_order where status = 3""")
        status = dict_fetchall(cursor)
    return status


def get_order_by_id(pk):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from  maxway_order 
                 where id = %s""", [pk])
        status = dict_fetchone(cursor)
    return status


def get_category_by_id(pk):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from  maxway_category 
                 where id = %s""", [pk])
        status = dict_fetchone(cursor)
    return status


def get_category_count():
    with closing(connection.cursor()) as cur:
        cur.execute("""select count(name) as name from maxway_category """)
        count_cat = dict_fetchone(cur)
    return count_cat


def news_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select name, count(title) as news_count from 
            maxway_category left join maxway_product on maxway_category.id=maxway_product.category_id
             group by name""")
        news = dict_fetchall(cursor)
    return news


def get_product_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(title) as title from maxway_product""")
        count_prod = dict_fetchone(cursor)
    return count_prod


def get_user():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from maxway_delilveryinfo""")
        users = dict_fetchall(cursor)
        return users


def get_order():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from maxway_order""")
        orders = dict_fetchall(cursor)
    return orders


def get_category():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from maxway_category""")
        categories = dict_fetchall(cursor)
    return categories


def get_product():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from maxway_product""")
        products = dict_fetchall(cursor)
    return products


def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row))
            for row in cursor.fetchall()]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))