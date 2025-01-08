import os
from sqlalchemy import Engine, create_engine, text
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
import pg8000

# Retrieve credentials from environment variables
db_user = os.getenv('DB_USER', 'admin')
db_password = os.getenv('DB_PASSWORD', 'admin')
db_host = os.getenv('DB_HOST', 'localhost')
db_port = int(os.getenv('DB_PORT', '5432'))
db_name = 'my_database' # os.getenv('DB_NAME', 'your_database_name')

Base = declarative_base()

class Table1(Base):
	__tablename__ = 'table_1'
	id = Column(Integer, primary_key=True)
	name = Column(String)

class Table2(Base):
	__tablename__ = 'table_2'
	id = Column(Integer, primary_key=True)
	name = Column(String)


class DBHandler:

	@classmethod
	def create_database(cls, database_name: str):
		connection = pg8000.connect(
			user=db_user,
			password=db_password,
			host=db_host,
			port=db_port,
			database='postgres'
		)
		# Set autocommit to True
		connection.autocommit = True
		# Create a cursor object
		cursor = connection.cursor()

		# Check if the database exists
		cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s", (database_name, ))
		exists = cursor.fetchone()       

		# Execute the CREATE DATABASE statement
		if not exists:
			cursor.execute(f'CREATE DATABASE {database_name}')
		# Close the cursor and connection
		cursor.close()
		connection.close()
		DBHandler._create_engine(database_name)

	engine: Engine = None # type: ignore

	@classmethod
	def _create_engine(cls, database_name: str):
		if DBHandler.engine is not None:
			return
		connection_url = URL.create(
			drivername='postgresql+pg8000',
			username=db_user,
			password=db_password,
			host=db_host,
			port=db_port,
			database=database_name
		)
		DBHandler.engine = create_engine(connection_url)
		print('ENGINE created')

	def version_check(self) -> 'DBHandler':
		with self.engine.connect() as connection:
			result = connection.execute(text("SELECT version();"))
			db_version = result.fetchone()
			print(f"Connected to - {db_version}")
		return self

	# Function to check if a table exists
	def table_exists(self, table_name):
		inspector = inspect(self.engine)
		return inspector.has_table(table_name)

	def create_tables(self) -> 'DBHandler':
		if not self.table_exists(Table1.__tablename__):
			Table1.__table__.create(self.engine)
			print(f"Table '{Table1.__tablename__}' created.")
		else:
			print(f"Table '{Table1.__tablename__}' already exists.")		

		if not self.table_exists(Table2.__tablename__):
			Table2.__table__.create(self.engine)
			print(f"Table '{Table2.__tablename__}' created.")
		else:
			print(f"Table '{Table2.__tablename__}' already exists.")		

		return self



if __name__ == '__main__':
	DBHandler.create_database(db_name)
	db1 = DBHandler().version_check().create_tables()
