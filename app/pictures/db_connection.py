import asyncio

from connection import connection

loop = asyncio.get_event_loop()


async def put_img_query(file_name):
    conn = await connection()
    query = '''INSERT INTO img(name) VALUES('%s')''' % file_name
    await conn.execute(query)
    await conn.close()


async def get_img_query(img_id):
    conn = await connection()
    query = 'SELECT * FROM img where id = %d' % img_id
    values = await conn.fetchrow(query)
    await conn.close()
    return values


def get_img_name(img_id=1):
    img = loop.run_until_complete(get_img_query(img_id))
    return img['name']


def path_redactor(filename):
    return '../app/pictures/img/' + filename + '.jpeg'


def get_img(id_pic=1):
    return path_redactor(get_img_name(id_pic))


def put_img(file_name):
    loop.run_until_complete(put_img_query(file_name))


