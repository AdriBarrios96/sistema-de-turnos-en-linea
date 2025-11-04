from databases import Database

DATABASE_URL = "mysql+aiomysl://root:adminadmin@localhost:3306/turnos_cliente_db"

db = Database(DATABASE_URL)