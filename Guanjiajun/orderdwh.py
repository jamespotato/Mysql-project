import pymysql

try:
      conn = pymysql.connect('localhost', 'root', 'root')
      cursor = conn.cursor()

      sql1 = "CREATE DATABASE bigz_dwhb"
      cursor.execute(sql1)

      sql2 = "USE bigz_dwhb"
      cursor.execute(sql2)

      conn.commit()

      sql3 = """CREATE TABLE CALENDAR
                  ( CalendarKey INT,
                  FullDate varchar(25),
                  DayOfWeek varchar(25),
                  Dayofmonth INT,
                  Month varchar(25),
                  Quarter varchar(2),
                  Year varchar(4),
                  PRIMARY KEY (CalendarKey));"""
      cursor.execute(sql3)
      conn.commit()

      sql4 = """CREATE TABLE PRODUCT
                  ( ProductKey INT,
                  ProductID varchar(2),
                  ProductName varchar(25),
                  ProductType varchar(25),
                  ProductSupplierName varchar(25),
                  PRIMARY KEY (ProductKey));"""
      cursor.execute(sql4)
      conn.commit()

      sql5 = """CREATE TABLE CUSTOMER
                  ( CustomerKey INT,
                  CustomerID varchar(2),
                  CustomerName varchar(25),
                  CustomerType varchar(25),
                  CustomerZip varchar(5),
                  PRIMARY KEY (CustomerKey));"""
      cursor.execute(sql5)
      conn.commit()

      sql6 = """CREATE TABLE ORDERCLERK
                  ( OrderClerkKey INT,
                  OrderClerkID varchar(3),
                  OrderClerkName varchar(25),
                  OrderClerkTitle varchar(25),
                  OrderClerkEducationLevel varchar(25),
                  OrderClerkYearOfHire varchar(4),
                  PRIMARY KEY (OrderClerkKey));"""
      cursor.execute(sql6)
      conn.commit()

      sql7 = """CREATE TABLE DEPOT
                  ( DepotKey INT,
                  DepotID varchar(2),
                  DepotSize varchar(25),
                  DepotZip varchar(5),
                  PRIMARY KEY (DepotKey));"""
      cursor.execute(sql7)
      conn.commit()

      sql8 = """CREATE TABLE ORDERCHECK
                  ( CalendarKey INT,
                  CustomerKey INT,
                  DepotKey INT,
                  OrderClerkKey INT,
                  ProductKey INT,
                  OrderID varchar(2),
                  Time varchar(25),
                  Quantity INT,
                  PRIMARY KEY (ProductKey, OrderID, CustomerKey));"""
      cursor.execute(sql8)
      conn.commit()

      cursor.close()
      conn.close()

except:
      cursor.close()
      conn.close()