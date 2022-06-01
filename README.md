#spyMonkDB

### What is the spyMonkDB ?
Welcome! This project is a simple python3 library that uses .json files as a micro noSQL local database. While it is noSQL based database, it's functions are specifically designed with SQL statements in mind. spyMonkDB also enables you to write more complex and speed efficient queries.

## Sample usage
```python
from spyMonk.spyMonkDB import spyMonkDB, Query

db = spyMonkDB(connection="users.json", tablename="spyMonkDB")
User = Query(db)

print(db.length()) # int: number of columns

db.filter(User.name == "Shubhajeet")

print(db.all()) 
# List[Dict[str, Any]]: return columns where 
# that include -> {"name": "Shubhajeet"}

db.filter(User.age != 21)

print(db.all()) 
# List[Dict[str, Any]]: return table where 
# that don't include -> {"age": 21}

```
## SQL equivalent restructuring filter
### ALL
return result of query or whole table
```python
db.filter(User.name == "Shubhajeet")
print(db.all()) 
# List[Dict[str, Any]]: return columns where 
# that include -> {"name": 21} and limit to 5 return columns
```
### LIMIT
return number of rows up to a specified limit
```python
db.filter(User.age == 21)
print(db.limit(5)) 
# List[Dict[str, Any]]: return columns where 
# that include -> {"age": 21} and limit to 5 return columns
```
### ASC
Note: this is the natural order.
```python
db.filter(User.name == "Shubhajeet")
print(db.asc()) 
# List[Dict[str, Any]]: return columns where 
# that include -> {"name": "Shubhajeet"} 
```
### DESC
reverse of natural order
```python
db.filter(User.name == "Shubhajeet")

print(db.desc()) 
# List[Dict[str, Any]]: return columns where 
# that include -> {"name": "Shubhajeet"} and desc order
```

## SQL equivalent statements
### SELECTALL
Equivalent to SELECT * FROM _TABLENAME_;<br>
returns a result table
```python
db.selectall()
```
### SELECT
Equivalent to SELECT column1, ... FROM _TABLENAME_;<br>
returns columns the include specified keys
```python
db.select(["name"])
```
### INSERT
Insert new column into database <br>
```python
db.insert({"name": "Shubhajeet", "age": 21,
        "money": None, "Python": True
        "Java": True})
```
### UPDATE
UPDATE table_name SET _column1_=_'value1'_, ... WHERE _column1_=_'value1'_; <br>
Update specific column(s) 
```python
db.update({"seal": True}, {"name": "Shubhajeet"})
# add {"seal": True} where {"name": "Shubhajeet"}
```
### TRUNCATE
TRUNCATE TABLE _TABLENAME_; <br>
This command is **irreversible** and deletes all data inside a table, but not the table itself.
```python
db.truncate()
```
### DELETE
Equivalent to DELETE FROM _TABLENAME_ WHERE _KEY_=_'VALUE'_;<br>
Drop all columns with same key and value
```python
db.delete({"name": "Shubhajeet"})
```

