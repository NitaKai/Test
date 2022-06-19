import asyncpg


async def connection():
    conn = await asyncpg.connect(host='localhost',
                                 port='5432',
                                 user='postgres',
                                 password='12354',
                                 database='test_application'
                                 )
    return conn
