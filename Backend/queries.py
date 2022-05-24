from asyncio.windows_events import NULL
import email
import sqlite3
from tokenize import Special
import py
import datetime

from pyxel import title


#20 Python Functions. (Activate print(function) to get result.)

# Function 1. SELECT all cities

def select_all_cities():
    with sqlite3.connect ("sakila.db") as conn:
        cursor = conn.cursor()
        cities = f"SELECT city FROM city"
        cursor.execute(cities)
        data = cursor.fetchall()
        return data
    
for cityresult in select_all_cities():
    cityprint = cityresult [0]
    #print (cityprint)


 
# Function 2. ORDER actors BY first names

def order_by_one():
    with sqlite3.connect ("sakila.db") as conn:
        cursor = conn.cursor()
        fname = 'first_name'
        lstname = 'last_name'
        actors = f"SELECT {fname},{lstname} FROM actor ORDER BY first_name"  
        cursor.execute (actors)
        data = cursor.fetchall()
        return data

for actorresult in order_by_one():
    actorfirstname = actorresult[0]
    actorlastname = actorresult[1]
    #print (actorfirstname,actorlastname)
        

 
# Function 3. Order actors by last names.

def order_by_two():
    with sqlite3.connect ("sakila.db") as conn:
        cursor = conn.cursor()
        fname = 'first_name'
        lname = 'last_name'
        actors = f"SELECT {fname}, {lname} FROM actor ORDER BY last_name"
        cursor.execute(actors)
        data = cursor.fetchall()
    return data

for actororder in order_by_two():
    actorfname = actororder[0]
    actorlstname= actororder[1]
    #print (actorfname,actorlstname)
    



# Function 4. ORDER films by release year.

def select_films(ord):
    with sqlite3.connect ("sakila.db") as conn:
        cursor = conn.cursor()
        #ord = 'release_year'
        #movie = 'title'
        film = f"SELECT * FROM film ORDER BY {ord} LIMIT 5" 
        cursor.execute(film)
        data = cursor.fetchall()
    return data



#result = select_films("release_year")




# Function 5. SELECT film titles WHERE the rating is R. LIMIT to first 5 records.

def select_film_by_rating(rate):
    with sqlite3.connect ("sakila.db") as conn:
        cursor = conn.cursor()
       # rate = 'R'
       # ttl = 'title'
        film = f"SELECT * FROM film WHERE rating = '{rate}' LIMIT 5;"
        print (film)
        cursor.execute(film)
        data = cursor.fetchall()
    return data

films = select_film_by_rating("R")



  
    

# Function 6. SELECT customers using WHERE their surname begins with 'S'. LIMIT results to first 3 records.

def select_three():
    with sqlite3.connect ("sakila.db") as conn:
        cursor = conn.cursor()
        letter = 'S'
        fname = 'first_name'
        lstname = 'last_name'
        film = f"SELECT {fname}, {lstname} FROM customer WHERE last_name LIKE '{letter}%';"
        cursor.execute (film)
        data = cursor.fetchall()
    return(data)

for select_three_tidy in select_three():    
        fname = select_three_tidy [0]
        lname = select_three_tidy [1]
        #print (select_three_tidy)




# Function 7. SELECT movie titles with a running time of less than two hours using WHERE. LIMIT results to first 10 records.

def select_ten():
    with sqlite3.connect ("sakila.db") as conn:
        cursor = conn.cursor()
        twohr = 120
        film = f"SELECT title FROM film WHERE length <{twohr} LIMIT(10);"
        cursor.execute (film)
        data = cursor.fetchall()
    return(data)


for select_ten_tidy in select_ten():
    seltentidy = select_ten_tidy[0]
    #print (seltentidy)

# Function 8. (1) INSERT INTO customer table new customer, Ivana Movie for Store 2. Display new record.

# import sqlite3

def insert_user(active,address,district,cityid,postcode,fstname,lstname,email,store_id):
    with sqlite3.connect("sakila.db") as conn:
        cursor = conn.cursor()
        #active = 1
        #address = '5 Overdues Mews'
        #district = 'Grand Views'
        #cityid = 501
        #postcode = 1234
        #phone = 6494783767
        #fstnme = 'IVANA'
        #lstnme = 'MOVIE'
        #email = 'ivanamail@gmail.com'
        #store_id = 2

        new_address = f"INSERT INTO address (address,district, city_id, postal_code, phone,last_update) VALUES ('{address}', '{district}', {cityid}, {postcode},{ph},datetime('now'));" 
        cursor.execute (new_address)
        add_id_query = f"SELECT address_id FROM address WHERE phone = {ph};"
        cursor.execute(add_id_query)
        data = cursor.fetchall()
        address_id = data[0]
        customerADD = f"INSERT INTO customer (store_id,first_name,last_name,email,address_id,active,create_date,last_update) VALUES ({store_id},'{fstnme}','{lstnme}','{email}','{address_id}',{active},datetime('now'),datetime('now'))"
        cursor.execute (new_address)
        cursor.execute (customerADD)
        #printrec= f"SELECT customer_id,first_name,last_name,email FROM customer WHERE customer_id=600;"
        #cursor.execute (printrec)
        #data = cursor.fetchall()
    return (data)

#for printnewrec in insert_user(1):
    id = printnewrec[0]
    name = printnewrec[1]
    surname = printnewrec[2]
    email = printnewrec[3]
    id = printnewrec[0]
    print (id,name,surname,email)


# Function 9. DELETE Ivana Movie FROM customer records. List all remaining records.

# def delete_ivana():
#     with sqlite3.connect ("sakila.db") as conn:
#         cursor = conn.cursor()
#         customer_id = 600
#         fstnme = 'IVANA'
#         lstnme ='MOVIE'
#         phone = 54639062007
#         address_id = 606
#         addressDel = f"DELETE FROM address where address_id = {address_id};"
#         customerDel = f"DELETE FROM customer WHERE customer_id = {customer_id} AND first_name ='{fstnme}' AND last_name ='{lstnme}';"
#         customeraddDel = f"DELETE FROM address WHERE phone = 54639062007;"
#         cursor.execute (addressDel)
#         cursor.execute (customerDel)
#         data = cursor.fetchall()
#     return(data)
    
# def list_cust():
#     with sqlite3.connect ("sakila.db") as conn:
#         cursor = conn.cursor()
#         cursor.execute ("SELECT first_name, last_name FROM customer;")
#         data = cursor.fetchall()
#     return(data)

# print (delete_ivana())

# print(list_cust())
 



# Function 10. Uma Wood has married Ed Chase, taking his last name and combining it with hers. UPDATE her record to reflect this. 

def update_record():
    with sqlite3.connect ("sakila.db") as conn:
        cursor = conn.cursor()
        fname = 'UMA'
        newlname = 'CHASE-WOOD'
        actorid= 13
        actor_update =  f"UPDATE actor SET first_name ='{fname}', last_name ='{newlname}' WHERE actor_id = {actorid};"
        cursor.execute (actor_update)
        actor_new = f"SELECT * FROM actor WHERE actor_id = {actorid};"
        cursor.execute (actor_new)
        data = cursor.fetchall()
        return(data)

for updaterec in update_record(): 
    actid = updaterec[0]
    nmeone = updaterec [1] 
    nmetwo = updaterec [2]
    #print (actid,nmeone,nmetwo) 
    

#Function 11. (2) INSERT a new record for the actor Dirk Diggler INTO the actor table. 

def insert_new_actor():
    with sqlite3.connect ("sakila.db") as conn:
        cursor = conn.cursor()
        ftname = 'Dirk'
        ltname = 'Diggler'
        actor_new =  f"INSERT INTO actor (first_name,last_name,last_update) VALUES ('{ftname}','{ltname}',datetime('now'))"
        cursor.execute (actor_new)
        actor_newrec =  ("SELECT * FROM actor WHERE last_name = 'Diggler';")
        cursor.execute (actor_newrec)
        data = cursor.fetchall()
    return(data)
for actinst in insert_new_actor():
    ident = actinst [0]
    firnm = actinst [1]
    latnm = actinst [2]
    #print (ident,firnm,latnm)


# Function 12. (3) INSERT a new film title, "The Adventures of Buckaroo Banzai Across the 8th Dimension" INTO the films table.


def insert_new_film():
    with sqlite3.connect ("sakila.db") as conn:
        cursor = conn.cursor()
        ttle = 'The Adventures of Buckaroo Banzai Across the 8th Dimension'
        desc = 'Best movie you never saw.'
        year = '1984'
        langid = 1
        origlangid = None
        rentdur = 6
        rentpri = 6.99
        runti = 103
        replace = 30.99
        rting = 'PG'
        spec = 'Trailers, Deleted Scenes'
        film_new = f"INSERT INTO film (title,description,release_year,language_id,original_language_id,rental_duration,rental_rate,length,replacement_cost,rating,special_features,last_update)  VALUES ('{ttle}','{desc}',{year},{langid},'{origlangid}',{rentdur},{rentpri},{runti},{replace},'{rting}','{spec}',datetime('now'))"
        cursor.execute (film_new)
        film_newrec =  f"SELECT * FROM film WHERE title = '{ttle}';"
        cursor.execute (film_newrec)
        data = cursor.fetchall()
    return(data)

for newflm in insert_new_film():
    filmidn = newflm [0]
    tite = newflm [1]
    dec = newflm [2]
    yr = newflm [3]
    rtg= newflm [10]
    rcst = newflm[7]

    #print(filmidn,tite,dec,yr,rtg,rcst)




# Function 13. (4) INSERT a record for new staff member, "Jim Smalllberries" INTO the staff table.


def insert_new_staff():
    with sqlite3.connect ("sakila.db") as conn:
        cursor = conn.cursor()
        manager = 3
        add = 3
        fname = 'Jim'
        lname = 'Smallberries'
        address = 4
        email = 'jim.smallberries@sakila.com'
        usernme = 'Jimbo'
        active = 'TRUE'
        psswd = '1d192f70073521289c85368373daf45b6f13f320d620073a58d62b696f599000'
        store_new_id = f"INSERT INTO store (manager_staff_id,address_id,last_update) VALUES ({manager},{add},datetime('now'))"
        cursor.execute (store_new_id)
        
        storeID = f"SELECT store_id, manager_staff_id FROM store WHERE store_id = 3"
        cursor.execute (storeID)
        data= cursor.fetchall()[0]
        store_id = data[0]
        staff_new =  f"INSERT INTO staff (first_name,last_name,address_id,email,store_id,active,username,password,last_update)  VALUES ('{fname}','{lname}',{address},'{email}','{store_id}',{active},'{usernme}','{psswd}',datetime('now'))"
        cursor.execute (staff_new)
        
        staff_newrec =  f"SELECT * FROM staff WHERE last_name = '{lname}';"
        cursor.execute(staff_newrec)
        data = cursor.fetchall()
    return(data)


for newbie in insert_new_staff():
    id = newbie [0]
    firnam = newbie [1]
    lasnam =newbie[2]
    eml = newbie[5]
    usname = newbie[8]
    #print('ID:',id,'Name:',firnam,lasnam,'Email:',eml,'Username:',usname)

# Function 14. (5) INSERT a new country INTO country table, "Wakanda"


def insert_new_country(cntry):
    with sqlite3.connect ("sakila.db") as conn:
        cursor = conn.cursor()
        #cntry = 'Wakanda'
        country_new = f"INSERT INTO country (country, last_update)  VALUES ('{cntry}', datetime('now'));"
        print (country_new)
        cursor.execute (country_new)
        result = cursor.lastrowid
        return result

#cnt = insert_new_country("Wakanda")


# for newflm in insert_new_film():
#     filmidn = newflm [0]
#     tite = newflm [1]
#     dec = newflm [2]
#     yr = newflm [3]
#     rtg= newflm [10]
#     rcst = newflm[7]

#     #print(filmidn,tite,dec,yr,rtg,rcst)

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
    return(data)

result_joinA = table_joinA()

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
   
    

result_joinC = table_joinC()

#Function 17. (3) JOIN customer table with payment table.

def table_join():
   with sqlite3.connect ("sakila.db") as conn:
    cursor = conn.cursor()
    sql = f"""SELECT *
              FROM customer
              JOIN payment ON payment.customer_id = customer.customer_id 
              LIMIT 300 
               """

    print (sql)
    cursor.execute (sql)
  
    data = cursor.fetchall()
    return(data)
   
result_joinC = table_join()



#Function 18. SELECT all





#Function 19  SELECT all


#FUNCTION 20. SELECT all






