from fastapi import FastAPI
import json
import queries
import hashlib

app = FastAPI()

# 20 Queries from queries.py



# Query 1. get all cities

@app.get('/get Cities')
def get_all_cities():
    result = queries.select_all_cities()
    return json.dumps (result)
    
# Query 2. get actors-order_by_first_name

@app.get('/get Actors Ordered by First Name')
def list_actors_by_first_name_in_alphabetical_order(): 
    result = queries.order_actors_first_name()
    return json.dumps (result)

# Query 3. get actors-order_by_last_name

@app.get('/get Actors Ordered By Last Name')
def list_actors_by_last_name_in_alphabetical_order(): 
    result = queries.order_actors_last_name()
    return json.dumps (result)

# Query 4. get films-order_by_release_date

@app.get('/get Films Ordered By Release Year')
def list_first_five_films_in_order_of_release(): 
    result = queries.select_films()
    return json.dumps (result)


# Query 5. get up to 100 films of selected rating

@app.get('/get 100 Films By Rating')
def list_up_to_100_films_of_your_selected_rating(rate):
    result = queries.select_films_by_rating(rate)
    return json.dumps (result)

# Query 6. get customers whose surnames begin with the selected letter

@app.get('/get List of 100 Customers')
def list_the_first_100_customer_records_by_last_name_beginning_with(letter):
    result = queries.select_customers_by_last_name(letter)
    return json.dumps (result)

 
# Query 7. get films with a running time of up to the selected length

@app.get('/get Films with a Running Time of up to Selected Length')
def list_50_films_of_selected_running_time_or_less(max_length_in_minutes,limit_to):
    result = queries.select_movies_by_running_time(max_length_in_minutes,limit_to)
    return json.dumps (result)

 
# Query 8. post new customer record

@app.post('/post New Customer Record')
async def insert_new_customer_record(first_name,last_name,email,address,district,city_id,postal_code,phone_number,store_id):
    result = queries.insert_new_customer_record(first_name,last_name,email,address,district,city_id,postal_code,phone_number,store_id)
    return json.dumps(result)

#Query 9. delete customer record

@app.delete('/delete Customer Record')
def delete_customer_record(customer_id,first_name,last_name, email):
     result = queries.delete_customer(customer_id,first_name,last_name, email)
     return json.dumps (result)

#Query 10. patch Country Record

@app.patch('/update Country Record')
def update_country_record(country_id,current_country_name,new_country_name):
    result = queries.update_country_record(country_id,current_country_name,new_country_name)
    return json.dumps (result)

#Query 11. post New Actor Record

@app.post('/insert New Actor Record')
def insert_new_actor(first_name,last_name):
    result = queries.insert_new_actor(first_name,last_name)
    return json.dumps (result)

#Query 12. post New Film Record

@app.post('/insert New Film Record')
def insert_new_film(language,title,description,release_year,rental_duration,rental_rate,runtime,replace_fee,rating,special_features):
    result = queries.insert_new_film (language,title,description,release_year,rental_duration,rental_rate,runtime,replace_fee,rating,special_features)
    return json.dumps(result)
    
       
#Query 13. post NEW Language Record

@app.post('/insert New Language Record')
def insert_new_language(language_name):
    result = queries.insert_new_language(language_name)
    return json.dumps(result)


#Query 14. post NEW Country Record

@app.post('/insert New Country Record')
def insert_new_country(country_name):
    result = queries.insert_new_country(country_name)
    return json.dumps(result)


#Query 18. get Customer Payment Records

@app.get('/get Payments')
def get_payments(customer_id,limit_to):
    result = queries.select_payments(customer_id,limit_to)
    return json.dumps (result)


#Query 19. get Film Categories

@app.get('/get Categories')
def get_all_categories():
    result = queries.select_all_film_categories()
    return json.dumps (result)


#Query 20. get all Languages

@app.get('/get Languages')
def get_all_languages():
    result = queries.select_all_languages()
    return json.dumps (result)



#put Password Hash Routine

@app.put('/create Password Hash')

def password_hash(password):
    encrypt = hashlib.sha256(password.encode()).hexdigest()
    return ("Encrypted Password:",json.dumps (encrypt))
    
    
   
  
    







