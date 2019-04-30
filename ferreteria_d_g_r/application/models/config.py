import web

db_host = 'localhost'
db_name = 'ferreteria_d_g_r'
db_user = 'dani'
db_pw = 'dani.2019'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )