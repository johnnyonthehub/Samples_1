import sqlite3
import json




#20 Queries. (Activate print(function) to get result.)

# Function 1. SELECT all cities

def select_all_cities():
    with sqlite3.connect ("sakila.db") as conn:
        cursor = conn.cursor()

        cities = f"""SELECT city 
                     FROM city"""

        cursor.execute(cities)
        data = cursor.fetchall()
        return ("Query successful!",data)
    

 
# Function 2. ORDER actors BY first names

def order_actors_first_name():
    with sqlite3.connect ("sakila.db") as conn:
        cursor = conn.cursor()

        actors = f"""SELECT first_name, 
                     last_name 
                     FROM actor 
                     ORDER BY first_name"""

        cursor.execute (actors)
        data = cursor.fetchall()
    return ("Query successful!",data)


    
 
# Function 3. Order actors by last names.

def order_actors_last_name():
    with sqlite3.connect ("sakila.db") as conn:
        cursor = conn.cursor()

        actors = f"""SELECT first_name, 
                     last_name 
                     FROM actor 
                     ORDER BY last_name"""

        cursor.execute(actors)
        data = cursor.fetchall()
    return ("Query successful!",data)





# Function 4. ORDER films by release year.

def select_films():
    with sqlite3.connect ("sakila.db") as conn:
        cursor = conn.cursor()

        film = f"""SELECT * 
                   FROM film 
                   ORDER BY release_year 
                   LIMIT 5""" 

        cursor.execute(film)
        data = cursor.fetchall()
    return("Query successful!",data)




# Function 5. SELECT film titles WHERE the rating is R. LIMIT to first 5 records.

def select_films_by_rating(rate):
    with sqlite3.connect ("sakila.db") as conn:
        cursor = conn.cursor()

        film = f"""SELECT title, 
                   rating 
                   FROM film 
                   WHERE rating = '{rate.upper()}' 
                   LIMIT 100;"""

        cursor.execute(film)
        data = cursor.fetchall()
    return ("Query successful!",data)


# Function 6. SELECT customers using WHERE their surname begins with selected letter. LIMIT results to 100 records.

def select_customers_by_last_name(letter):
    with sqlite3.connect ("sakila.db") as conn:
        cursor = conn.cursor()

        film = f"""SELECT first_name, 
                   last_name, 
                   email 
                   FROM customer 
                   WHERE last_name 
                   LIKE '{letter.upper()}%'
                   ORDER by last_name 
                   LIMIT 100;
                   """ 

        cursor.execute (film)

        data = ("Query successful!",cursor.fetchall())
    return data



# Function 7. SELECT movie titles with up to the selected running using WHERE. LIMIT results to first 100 records.

def select_movies_by_running_time(max_length_in_minutes,limit_to):
    with sqlite3.connect ("sakila.db") as conn:
        cursor = conn.cursor()

        film = f"""SELECT title, 
                   rating, 
                   length 
                   FROM film 
                   WHERE length <= {max_length_in_minutes} 
                   ORDER BY title 
                   LIMIT {limit_to};
                   """

        cursor.execute (film)

        data = ("Query successful!",cursor.fetchall())
    return data



# Function 8. (1) INSERT INTO customer table new customer.

def insert_new_customer_record(first_name,last_name,email,address,district,city_id,postal_code,phone_number,store_id):
   
    with sqlite3.connect("sakila.db") as conn:
        
        cursor = conn.cursor()

        new_address = f"""INSERT 
                          INTO address 
                          (address,
                          district,
                          city_id,
                          postal_code,
                          phone,
                          last_update) 
                          VALUES 
                         ('{address.upper()}',
                         '{district.upper()}',
                          {city_id},
                          {postal_code},
                          {phone_number},
                          datetime('now'));""" 

        cursor.execute (new_address)
        address_id = cursor.lastrowid

        customerADD = f"""INSERT 
                          INTO customer 
                          (store_id,
                          first_name,
                          last_name,
                          email,
                          address_id,
                          active,
                          create_date,
                          last_update) 
                          VALUES 
                          ({store_id},
                          '{first_name.upper()}',
                          '{last_name.upper()}',
                          '{email.lower()}',
                          {address_id},{1},
                          datetime('now'),
                          datetime('now'))"""

        cursor.execute (customerADD)

        customer_id = cursor.lastrowid
        cursor.execute (f"SELECT * FROM customer WHERE customer_id= {customer_id}") 
        data = cursor.fetchall()
        return ("Insert successful!",data)





 # Function 9. DELETE a customer from customer records. 

def delete_customer(customer_id,first_name,last_name,email):
    with sqlite3.connect ("sakila.db") as conn:

        cursor = conn.cursor()

        addressid = f"SELECT address_id FROM customer WHERE customer_id = {customer_id};"

        cursor.execute (addressid)
        address_id = cursor.fetchone()[0]

        deleteadd =  f"DELETE FROM address WHERE address_id = {address_id};"

        cursor.execute (deleteadd)

        customerDel = f"""DELETE 
                          FROM customer 
                          WHERE customer_id = {customer_id} 
                          ANDfirst_name ='{first_name.upper()}' 
                          AND last_name ='{last_name.upper()}' 
                          AND email = '{email.lower()}';"""

        cursor.execute (customerDel)

        data = cursor.fetchall()
        return("Delete successful!",data)
    

 

# Function 10. UPDATE country record

def update_country_record(country_id,current_country_name,new_country_name):
    with sqlite3.connect ("sakila.db") as conn:
         cursor = conn.cursor()

         country_update =  f"""UPDATE country 
                               SET country = '{new_country_name}'
                               WHERE country_id = {country_id}
                               AND country = '{current_country_name}';
                               """

         display_new = f"""SELECT * 
                           FROM country 
                           WHERE country_id = {country_id};
                           """
         cursor.execute (country_update)
         conn.commit()
         cursor.execute (display_new)
         conn.commit()
         return('Success!',country_id,new_country_name, 'Record updated!')
         
 


#Function 11. (2) INSERT a new actor record INTO the actor table. 

def insert_new_actor(first_name,last_name):
    with sqlite3.connect ("sakila.db") as conn:
        cursor = conn.cursor()

        actor_new = f"""INSERT 
                        INTO actor 
                        (first_name,
                        last_name,
                        last_update) 
                        VALUES
                        ('{first_name.upper()}',
                        '{last_name.upper()}',
                        datetime('now'));
                        """

        cursor.fetchall()
        cursor.execute(actor_new)
        conn.commit()
        return('Success!',first_name,last_name, "New actor inserted!")
       
        

        
#Function 12. (3) INSERT a new film title INTO the films table.

 
def insert_new_film(*params):
    
    language = params[0]
    title = params[1].upper()
    description=params[2]
    release_year= params[3]
    rental_duration = params[4]
    rental_rate = params[5]
    runtime= params [6]
    replace_fee = params [7]
    rating = params [8].upper()
    special_features = params [9]

    with sqlite3.connect ("sakila.db") as conn:
        cursor = conn.cursor()

        query = f"""SELECT language_id 
                    FROM language 
                    WHERE name = '{language}';
                    """

        cursor.execute (query)
        language_id = cursor.fetchone()[0]
        print (language_id)
         
        film_new =  f"""INSERT 
                        INTO film (
                        title,
                        description,
                        release_year,
                        language_id,
                        rental_duration,
                        rental_rate,
                        length,                 
                        replacement_cost,
                        rating,
                        special_features,
                        last_update
                        )  
                        VALUES (
                       '{title}',
                       '{description}',
                        {release_year},
                        {language_id},
                        {rental_duration},
                        {rental_rate},
                        {runtime},
                        {replace_fee},
                       '{rating}',
                       '{special_features}',
                        datetime('now')
                        );
                        """
        cursor.execute(film_new)
        conn.commit()
        film_id = cursor.lastrowid
        print(film_id)

        query = f"""SELECT * 
                    FROM film 
                    WHERE film_id = {film_id};
                    """
        
        cursor.execute (query)
        cursor.fetchall()
        dict= {
            'language':language,
            'title':title,
            'description': description,
            'release_year': release_year,
            'language_id': language_id,
            'rental_duration': rental_duration,
            'rental_rate': rental_rate,
            'length': runtime,
            'replacement_cost': replace_fee,
            'rating': rating,
            'special_features': special_features,
            'last_update': 'datetime(now)'
        }
        json_object =json.dumps(dict, indent = 2,)
        return(json_object,'Success!',title,release_year,runtime,rating, 'New film added!')
        
        
    


# Function 13. (4) INSERT a record for a new language INTO the language table.


def insert_new_language(language_name):
    
    with sqlite3.connect ("sakila.db") as conn:
         cursor = conn.cursor()

         query= f"""INSERT INTO 
                    language (name,last_update)
                    VALUES ('{language_name}',
                    datetime('now'));
                    """
               
         cursor.fetchall()
         cursor.execute(query)
         conn.commit()
         #return('Success!',language_name, "New language inserted!")

         queryB= f"SELECT * FROM language WHERE name= '{language_name}';"
         cursor.execute (queryB)
         cursor.fetchall()

         dict= {
            'name':language_name,
            'last_update': 'datetime(now)'
        }
         json_object =json.dumps(dict, indent = 2,)
         return(json_object,'Success!',language_name, 'New language added!')



         


# Function 14. (5) INSERT a new country INTO country table.


def insert_new_country(country_name):
    with sqlite3.connect ("sakila.db") as conn:
         cursor = conn.cursor()
       
         new_country = f"""INSERT INTO 
                           country (country, last_update) 
                           VALUES ('{country_name.title()}', 
                           datetime('now'));
                           """
         
         cursor.fetchall()
         cursor.execute (new_country)
         conn.commit()

         query = f"""SELECT * 
                     FROM country 
                     WHERE country ='{country_name}';
                     """

         cursor.fetchall()
         cursor.execute (query)
         conn.commit()
        
         dict= {
            'country':country_name.title(),
            'last_update': 'datetime(now)'
        }
         json_object =json.dumps(dict, indent = 2,)
         return(json_object,'Success!',country_name.title(), 'New language added!')


#Function 15. (1) JOIN the film_actor table with the film table and film_id table.

def table_joinA():
   with sqlite3.connect ("sakila.db") as conn:
    cursor = conn.cursor()

    sql = f"""SELECT title, film.film_id, *  
               FROM film 
               JOIN film_actor ON film.film_id = film_actor.film_id
               JOIN actor ON actor.actor_id = film_actor.actor_id LIMIT 100;  
               """

    print (sql)
    cursor.execute (sql)
   
    data = cursor.fetchall()
    return data

#result_joinA = table_joinA()
#print(result_joinA)

#Function 16. (2) JOIN film_category table with the film table and category table.

def table_joinB():
   with sqlite3.connect ("sakila.db") as conn:
    cursor = conn.cursor()

    sql = f"""SELECT *  
               FROM film  
               JOIN film_category ON film_category.film_id = film.film_id
               JOIN category ON category.category_id = film_category.category_id
               LIMIT 100;  
               """

    print (sql)
    cursor.execute (sql)
    data = cursor.fetchall()
    return(data)
   
#result_joinB = table_joinB()
#print(result_joinB)

#Function 17. (3) JOIN customer table with payment table.

def table_joinC():
   with sqlite3.connect ("sakila.db") as conn:
    cursor = conn.cursor()

    sql = f"""SELECT *
              FROM customer
              JOIN payment ON payment.customer_id = customer.customer_id 
              LIMIT 300 
               """

    cursor.execute (sql)
    data = cursor.fetchall()
    return(data)
   
#result_joinC = table_joinC()
#print(result_joinC)



#Function 18. SELECT from payment table

def select_payments(customer_id,limit_to):
   with sqlite3.connect ("sakila.db") as conn:
    cursor = conn.cursor()

    query = f"""SELECT * 
                FROM payment 
                WHERE
                customer_id = {customer_id} 
                LIMIT {limit_to};
                """

    cursor.execute (query)
    data = cursor.fetchall()
    return("Query successful!",data)




#Function 19.  SELECT all film categories

def select_all_film_categories():
   with sqlite3.connect ("sakila.db") as conn:
    cursor = conn.cursor()

    query = f"""SELECT name 
                FROM category;
                """
    
    cursor.execute (query)
    data = cursor.fetchall()
    return("Query successful!",data)





#Function 20. SELECT all languages

def select_all_languages():
   with sqlite3.connect ("sakila.db") as conn:
    cursor = conn.cursor()

    selectl = f"""SELECT name 
                  FROM language"""
    
    cursor.execute (selectl)
   
    data = cursor.fetchall()
    print (selectl)
    return("Query successful!",data)






