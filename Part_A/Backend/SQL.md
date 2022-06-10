# Task One: SQL Database
## A. Tables
* `actor`

* `address`

* `category`

* `city`

* `country`

* `customer`

* `film`

* `film_actor`

* `film_category`

* `film_text`

* `inventory`

* `language`

* `payment`

* `rental`

* `staff`

* `store`
  


**
[I've omitted the sqlite_sequence table as this would not normally count toward the number of tables]

---

## B. `autoincrement` Keyword
This keyword automatically generates a unique number when a new record is inserted in a table. The default starting value is one, but any starting value can be assigned.

---

## C. `references` Keyword
The primary key is a field that uniquely identifies other records in the database.  The foreign key is the field that refers to the primary key, linking tables in a database.


The references keyword specifies the field for the linking of the primary and foreign keys.

For example, the actor_id field is a primary key in the actor table which links to the actor_id foreign key in other tables.

---