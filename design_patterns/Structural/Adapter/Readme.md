This is the "Adapter" design pattern implementation in python.

There is a "Database" interface. It supports the following common functionalities:
1. insert
2. update
3. select
4. remove

We have a "PythonApplication" which has the following methods:
1. saveObject
2. updateObject
3. loadObject
4. deleteObject


We have a client called "DatabaseRunner".
Inside of it the client should call all methods of our database.

As we see the method of the "Database" and the "PythonApplication" do the same,
but we can not interact with it directly
due to the difference between the methods' names.


In this case we create an adapter ("AdapterPythonToDatabase")
which will inherit PythonApplication and Database.
In each overriden method of the database
we will call the corresponding method of the application.

At last step we should create an instance of the "AdapterPythonToDatabase"
inside of the "DatabaseRunner" and call the database related methods that we need.
