import sqlite3
import py
import datetime

#20 Python Functions. (Activate print(function) to get result.)
# Function 1. SELECT all cities

def select_all_cities():
    with sqlite3.connect ("sakila.db") as conn:
        cursor = conn.cursor()
        cities = f"SELECT * FROM city"
        cursor.execute(cities)
        data = cursor.fetchall()
    return data

for cityresult in select_all_cities():
    city =cityresult
    #print(city)


 
# Function 2. ORDER actors BY first names

def order_by_one():
    with sqlite3.connect ("sakila.db") as conn:
        cursor = conn.cursor()
        actors = f"SELECT * FROM actor ORDER BY first_name"  
        cursor.execute (actors)
        data = cursor.fetchall()
    return data

for actorresult in order_by_one():
    actor = actorresult
    #print (actor)

 
# Function 3. Order actors by last names.

def order_by_two():
    with sqlite3.connect ("sakila.db") as conn:
        cursor = conn.cursor()
        actors = f"SELECT * FROM actor ORDER BY last_name"
        cursor.execute(actors)
        data = cursor.fetchall()
    return data

for actororder in order_by_two():
    actortwo = actororder
    #print (actortwo)



# Function 4. ORDER films by release year.

def order_by_three():
    with sqlite3.connect ("sakila.db") as conn:
        cursor = conn.cursor()
        film = f"SELECT * FROM film ORDER BY release_year" 
        cursor.execute(film)
        data = cursor.fetchall()
    return data

for obthree in order_by_three():
        filmorder = obthree
        #print (filmorder)



# Function 5. SELECT films WHERE the rating is R. LIMIT to first 5 records.

def select_five():
    with sqlite3.connect ("sakila.db") as conn:
        cursor = conn.cursor()
        film =f"SELECT * FROM film WHERE rating = 'R' LIMIT(5)"
        cursor.execute(film)
        data = cursor.fetchall()
    return(data)

for sfve in select_five():
        movieorder = sfve
       # print(movieorder)
    

# Function 6. SELECT inactive customers using WHERE. LIMIT results to first 3 records.

def select_three():
    with sqlite3.connect ("sakila.db") as conn:
        cursor = conn.cursor()
        film =cursor.execute("SELECT * FROM customer WHERE active = FALSE LIMIT(3)")
        data = cursor.fetchall()
    return(data)

# print(select_three())

# Function 7. SELECT movies with a running time of less than two hours using WHERE. LIMIT results to first 10 records.

def select_ten():
    with sqlite3.connect ("sakila.db") as conn:
        cursor = conn.cursor()
        film =cursor.execute("SELECT * FROM film WHERE length <120 LIMIT(10)")
        data = cursor.fetchall()
    return(data)


#print(select_ten())


# Function 8. DELETE inactive customer records. List all remaining records.

def delete_inactives():
    with sqlite3.connect ("sakila.db") as conn:
        cursor = conn.cursor()
        customerIn = cursor.execute ("DELETE FROM customer WHERE active = FALSE")
        customer =cursor.execute ("SELECT * FROM customer;")
        data = cursor.fetchall()
    return(data)

#print(delete_inactives())



# Function 9. Uma Wood has married Ed Chase, taking his last name and combining it with hers. UPDATE her record to reflect this. 

def update_record():
    with sqlite3.connect ("sakila.db") as conn:
        cursor = conn.cursor()
        actor_update = cursor.execute ("UPDATE actor SET first_name ='UMA', last_name ='CHASE-WOOD' WHERE actor_id = 13;")
        actor_new =cursor.execute ("SELECT * FROM actor WHERE actor_id = 13;")
        data = cursor.fetchall()
    return(data)

#print(update_record())

#Function 10. (1) INSERT a new record for the actor Dirk Diggler INTO the actor table. 

def insert_new_actor():
    with sqlite3.connect ("sakila.db") as conn:
        cursor = conn.cursor()
        actor_new = cursor.execute ("INSERT INTO actor (first_name,last_name,last_update) VALUES ('Dirk','Diggler',datetime('now'))")
        actor_newrec = cursor.execute ("SELECT * FROM actor WHERE last_name = 'Diggler';")
        data = cursor.fetchall()
    return(data)

#print(insert_new_actor())


# Function 11. (2) INSERT a new film title, "The Adventures of Buckaroo Banzai Across the 8th Dimension" INTO the films table.


def insert_new_actor():
    with sqlite3.connect ("sakila.db") as conn:
        cursor = conn.cursor()
        film_new = cursor.execute ("INSERT INTO film (title,description,release_year,language_id,original_language_id,rental_duration,rental_rate,length,replacement_cost,rating,special_features,last_update)  VALUES ('The Adventures of Buckaroo Banzai Across the 8th Dimension','Best movie you never saw.',1984,1,NULL,6,6.99,103,30.99,'PG','Trailers,Deleted scenes',datetime('now'))")
        film_newrec = cursor.execute ("SELECT * FROM film WHERE title = 'The Adventures of Buckaroo Banzai Across the 8th Dimension';")
        data = cursor.fetchall()
    return(data)

#print(insert_new_actor())


# Function 12. (3) INSERT a record for new staff member, "Jim Smalllberries" INTO the staff table.


def insert_new_staff():
    with sqlite3.connect ("sakila.db") as conn:
        cursor = conn.cursor()
        store_new_id = cursor.execute("INSERT INTO store (manager_staff_id,address_id,last_update) VALUES (3,3,datetime('now'))")
        staff_new = cursor.execute ("INSERT INTO staff (first_name,last_name,address_id,email,store_id,active,username,last_update)  VALUES ('Jim','Smallberries',4,'jim.smallberries@sakila.com','','Jimbo',TRUE,datetime('now'))")
        staff_newrec = cursor.execute ("SELECT * FROM staff WHERE last_name = 'Smallberries';")
        data = cursor.fetchall()
    return(data)

#print(insert_new_staff())


