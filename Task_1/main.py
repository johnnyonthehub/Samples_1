from fastapi import FastAPI
import queries
app = FastAPI()
#queries.select_all_cities('R')

@app.get('/city')
def select_all_cities():
    with sqlite3.connect ("sakila.db") as conn:
        cursor = conn.cursor()
        cities = f"SELECT * FROM %city%"
        cursor.execute(cities)
        data = cursor.fetchall()
    return data
    print(select_all_cities)
