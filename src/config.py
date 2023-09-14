class Config:
    SECRET_KEY = 'B!1weNAt1T^%kvhUI*S^'

class DevelpmentConfig(Config):
    DEBUG=True
    MYSQL_HOST = ''
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB= ''

config = {
    'development': DevelpmentConfig
}
