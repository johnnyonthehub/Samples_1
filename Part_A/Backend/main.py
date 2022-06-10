from fastapi import FastAPI
import json
import queries
import hashlib
from fastapi.middleware.cors import CORSMiddleware
# import os
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=[""],
    allow_headers=["*"],
)


# querySuc: str =os.environ ["QUERY SUCCESSFUL"]


# 20 Queries from queries.py


# Query 1. get all cities

@app.get('/get_cities')
def get_all_cities():
   # print(f"{querySuc}")
    result = queries.select_all_cities()
    return result

# Query 2. get actors-order_by_first_name


@app.get('/get_actors_ordered_by_first_name')
def list_actors_by_first_name_in_alphabetical_order():
    result = queries.order_actors_first_name()
    return result


# Query 3. get actors-order_by_last_name


@app.get('/get_actors_ordered_by_last_name')
def list_actors_by_last_name_in_alphabetical_order():
    result = queries.order_actors_last_name()
    return result


# Query 4. get films-order_by_release_date


@app.get('/get_films_ordered_by_release_year')
def list_first_five_films_in_order_of_release():
    result = queries.select_films()
    return result


# Query 5. get up to 100 films of selected rating

@app.get('/get_100_films_by_rating')
def list_up_to_100_films_of_your_selected_rating(rate):
    result = queries.select_films_by_rating(rate)
    return result


# Query 6. get customers whose surnames begin with the selected letter


@app.get('/get_list_of_100_customers')
def list_the_first_100_customer_records_by_last_name_beginning_with(letter):
    result = queries.select_customers_by_last_name(letter)
    return result


# Query 7. get films with a running time of up to the selected length

@app.get('/get_films_with_a_running_time_of_up_to_selected_length')
def list_50_films_of_selected_running_time_or_less(max_length_in_minutes, limit_to):
    result = queries.select_movies_by_running_time(
        max_length_in_minutes, limit_to)
    return result


# Query 8. post new customer record

@app.post('/post_new_customer_record')
async def insert_new_customer_record(first_name, last_name, email, address, district, city_id, postal_code, phone_number, store_id):
    result = queries.insert_new_customer_record(
        first_name, last_name, email, address, district, city_id, postal_code, phone_number, store_id)
    return result

# Query 9. delete customer record


@app.delete('/delete_customer_record')
def delete_customer_record(customer_id, first_name, last_name, email):
    result = queries.delete_customer(customer_id, first_name, last_name, email)
    return result

# Query 10. patch Country Record


@app.patch('/update_country_record')
def update_country_record(country_id, current_country_name, new_country_name):
    result = queries.update_country_record(
        country_id, current_country_name, new_country_name)
    return result

# Query 11. post New Actor Record


@app.post('/insert_new_actor_record')
def insert_new_actor(first_name, last_name):
    result = queries.insert_new_actor(first_name, last_name)
    return result

# Query 12. post New Film Record


@app.post('/insert_new_film_record')
def insert_new_film(language, title, description, release_year, rental_duration, rental_rate, runtime, replace_fee, rating, special_features):
    result = queries.insert_new_film(language, title, description, release_year,
                                     rental_duration, rental_rate, runtime, replace_fee, rating, special_features)
    return result


# Query 13. post NEW Language Record

@app.post('/insert_new_language_record')
def insert_new_language(language_name):
    result = queries.insert_new_language(language_name)
    return result


# Query 14. post NEW Country Record

@app.post('/insert_new_country_record')
def insert_new_country(country_name):
    result = queries.insert_new_country(country_name)
    return result


# Query 18. get Customer Payment Records

@app.get('/get_payments')
def get_payments(customer_id, limit_to):
    result = queries.select_payments(customer_id, limit_to)
    return result


# Query 19. get Film Categories

@app.get('/get_categories')
def get_all_categories():
    result = queries.select_all_film_categories()
    return result


# Query 20. get all Languages

@app.get('/get_languages')
def get_all_languages():
    result = queries.select_all_languages()
    return result


# post Password Hash Routine

@app.post('/createPasswordHash')
def password_hash(password):
    encrypt = hashlib.sha256(password.encode()).hexdigest()
    return ("Encrypted Password:", json.dumps(encrypt))
