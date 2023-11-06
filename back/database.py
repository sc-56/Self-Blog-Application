import psycopg2 
import json

# ---------------------- structure ---------------------------- #

# do: build the structure.
class DatabaseOperator():

    def __init__(self, database, user, password, host, port):

        self.database = database
        self.user = user
        self.password = password 
        self.host = host
        self.port = port
        self.connector = self.connect_database()

    # do: you should add variable [self] here.
    def connect_database(self):


        connector = psycopg2.connect(
            
            database = self.database,
            user = self.user,
            password = self.password,
            host = self.host,
            port = self.port
        
        )

        # do: i should catch the exception here.
        # question: what is exception ? 

        return connector
    
    def extract_first_question(self):

        with self.connector.cursor() as cur:

            cur.execute("""SELECT * 
            FROM questions
            LIMIT 2;
            """)
        
            dict = {}

            for idx, info in enumerate(cur):
            
                item = {}

                item = {"question": info[1], "date": info[2], "category": info[3], "description": info[4]}
                dict.update({idx+1: item})
        
        return json.dumps(dict)
    
    # to-do: add new information into the database;
    



# script ---------------------------------------------------------- #
print("segmentation: test with structure.")

data_operator = DatabaseOperator(database='q_mgmt', 
                user='postgres', 
                password='postgres', 
                host='localhost',
                port=5432)

# do: build the functionality.
print('segmentation: test with functionality.')

connector = psycopg2.connect(
    database='q_mgmt',
    user='postgres',
    password='postgres',
    host='localhost',
    port=5432
)


# info: the connection is establised, when the 
# print("connect: {}".format(connector))

# do: use the connector to query the first question.
with connector.cursor() as cur:
    
    

    cur.execute("""SELECT * 
                FROM questions
                LIMIT 2;
                """)
    dict = {}

    for idx, info in enumerate(cur):
        
        item = {}

        item = {"question": info[1], "date": info[2], "category": info[3], "description": info[4]}
        dict.update({idx+1: item})
    
    print(json.dumps(dict))

# learn: connect.cursor() using with statement.
# q: what is the meaning of 'with' statement ?

# learn: the cur.execute() must be executed in the with statement.
# learn: the feedback of the execute is one tuple in the cur. Therefore, the information should be executed.


connector.close()
# do: print the information
