from fastapi import FastAPI
import queries
app = FastAPI()
#queries.select_all_cities('R')

@app.get('/films')
def select_films(ord):
    result = queries.select_films(ord)
    return result


@app.get('/city')
def select_all_cities():
    # #with .connect ("sakila.db") as conn:
    #     cursor = conn.cursor()
    #     cities = f"SELECT * FROM %city%"
    #     cursor.execute(cities)
    #     data = cursor.fetchall()
    # return data
    print(select_all_cities)
    

@app.post('/user')
def add_user(ph):
    result = queries.insert_user(ph)
    #return f"the phone number:{ph}"
    return result
 