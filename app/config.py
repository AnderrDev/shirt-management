class Config:
    MYSQL_USER = 'user'
    MYSQL_PASSWORD = 'userpassword'
    MYSQL_HOST = 'mysql_container'  # Docker redirige el puerto 3306 al localhost
    MYSQL_DB = 'base_camisetas'
    MYSQL_PORT = 3306
    SWAGGER = {
        'title': 'API de Gestión de Camisetas',
        'uiversion': 3
    }
