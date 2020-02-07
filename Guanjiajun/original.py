#Author:Guan Jiajun

import pymysql


conn = pymysql.connect(host = '127.0.0.1',user ='root',password = 'root',port = 3306,
    charset = 'utf8mb4',cursorclass = pymysql.cursors.DictCursor)
cursor = conn.cursor()

try:
    sql1 = "CREATE DATABASE bigz_order"
    cursor.execute(sql1)
    sql2 = "USE bigz_order"
    cursor.execute(sql2)

    conn.commit()

    sql3 = """CREATE TABLE ORDERCLERK
            ( OCID varchar(3) NOT NULL,
            OCName varchar(25) NOT NULL,
            PRIMARY KEY (OCID) );"""
    cursor.execute(sql3)
    conn.commit()
    sql_3_insert = "INSERT INTO ORDERCLERK(OCID, OCName) VALUES (%s,%s)"
    sql_3_content = (('OC1', 'Tony'), ('OC2', 'Wes'), ('OC3', 'Lilly'))
    cursor.executemany(sql_3_insert, sql_3_content)
    conn.commit()


    sql4 = """CREATE TABLE DEPOT
            ( DepotID varchar(2) NOT NULL,
            StoreSize varchar(25) NOT NULL,
            DepotZip varchar(5) NOT NULL,
            PRIMARY KEY (DepotID) );"""
    cursor.execute(sql4)
    conn.commit()

    sql_4_insert = "INSERT INTO DEPOT(DepotID, StoreSize, DepotZip) VALUES (%s,%s,%s)"
    sql_4_content = (('D1', 'Small', '60611'), ('D2', 'Large', '60660'), ('D3', 'Large', '60661'))

    cursor.executemany(sql_4_insert, sql_4_content)
    conn.commit()


    sql5 = """CREATE TABLE CUSTOMER
            ( CustomerID varchar(2) NOT NULL,
            CustomerName varchar(25) NOT NULL,
            CustomerType varchar(25) NOT NULL,
            CustomerZip varchar(5) NOT NULL,
            PRIMARY KEY (CustomerID) );"""
    cursor.execute(sql5)
    conn.commit()
    sql_5_insert = "INSERT INTO CUSTOMER(CustomerID, CustomerName, CustomerType, CustomerZip) VALUES (%s,%s,%s,%s)"
    sql_5_content = (('C1', 'Auto Doc', 'Repair Shop', '60137'), ('C2', 'Bos Car Repair', 'Repair Shop', '60140'), ('C3', 'JJ Auto Parts', 'Retiailer', '60605'))

    cursor.executemany(sql_5_insert, sql_5_content)
    conn.commit()


    sql6 = """CREATE TABLE ORDERLIST
            ( OrderID varchar(2) NOT NULL,
            OrderDate varchar(25) NOT NULL,
            OrderTime varchar(25) NOT NULL,
            CustomerID varchar(2) NOT NULL,
            OCID varchar(3) NOT NULL,
            DepotID varchar(2) NOT NULL,
            PRIMARY KEY (OrderID),
            FOREIGN KEY (CustomerID) REFERENCES CUSTOMER(CustomerID),
            FOREIGN KEY (OCID) REFERENCES ORDERCLERK(OCID),
            FOREIGN KEY (DepotID) REFERENCES DEPOT(DepotID) );"""
    cursor.execute(sql6)
    conn.commit()
    sql_6_insert = "INSERT INTO ORDERLIST(OrderID, CustomerID, DepotID, OCID, OrderDate, OrderTime) VALUES (%s,%s,%s,%s,%s,%s)"
    sql_6_content = (('O1', 'C1', 'D1', 'OC1', '1-Jan-2013','9:00:00 AM'), ('O2', 'C2', 'D1', 'OC2', '2-Jan-2013','9:00:00 AM'),('O3', 'C3', 'D2', 'OC3', '2-Jan-2013','9:30:00 AM'),('O4', 'C1', 'D2', 'OC1', '3-Jan-2013','9:00:00 AM'),('O5', 'C2', 'D3', 'OC2', '3-Jan-2013','9:15:00 AM'),('O6', 'C3', 'D3', 'OC3', '3-Jan-2013','9:30:00 AM'),('O7', 'C1', 'D2', 'OC3', '3-Jan-2013','9:45:00 AM'),('O8', 'C1', 'D2', 'OC3', '3-Jan-2013','9:45:00 AM'))

    cursor.executemany(sql_6_insert, sql_6_content)
    conn.commit()


    sql7 = """CREATE TABLE SUPPLIER
            ( SupplierID varchar(2) NOT NULL,
            SupplierName varchar(25) NOT NULL,
            PRIMARY KEY (SupplierID) );"""
    cursor.execute(sql7)
    conn.commit()
    sql_7_insert = "INSERT INTO SUPPLIER(SupplierID, SupplierName) VALUES (%s,%s)"
    sql_7_content = (('ST', 'Super Tires'), ('BE', 'Batteries Etc'))

    cursor.executemany(sql_7_insert, sql_7_content)
    conn.commit()

    sql8 = """CREATE TABLE PRODUCT
            ( ProductID varchar(5) NOT NULL,
            ProductName varchar(25) NOT NULL,
            ProductType varchar(25) NOT NULL,
            SupplierID varchar(2) NOT NULL,
            PRIMARY KEY (ProductID),
            FOREIGN KEY (SupplierID) REFERENCES SUPPLIER(SupplierID));"""
    cursor.execute(sql8)
    conn.commit()
    sql_8_insert = "INSERT INTO PRODUCT(ProductID, ProductName, ProductType, SupplierID) VALUES (%s,%s,%s,%s)"
    sql_8_content = (('P1', 'BigGripper', 'Tire', 'ST'), ('P2', 'TractionWiz', 'Tire', 'ST'), ('P3', 'SureStart', 'Battery', 'BE'))


    cursor.executemany(sql_8_insert, sql_8_content)
    conn.commit()


    sql9 = """CREATE TABLE ORDEREDVIA
            ( ProductID varchar(2) NOT NULL,
            OrderID varchar(2) NOT NULL,
            Quantity INT NOT NULL,
            PRIMARY KEY (ProductID, OrderID),
            FOREIGN KEY (ProductID) REFERENCES PRODUCT(ProductID),
            FOREIGN KEY (OrderID) REFERENCES ORDERLIST(OrderID));"""
    cursor.execute(sql9)
    conn.commit()
    sql_9_insert = "INSERT INTO ORDEREDVIA(ProductID, OrderID, Quantity) VALUES (%s,%s,%s)"
    sql_9_content = (('P1', 'O1', 4), ('P2', 'O1', 8), ('P1', 'O2', 12),('P2', 'O3', 4), ('P3', 'O4', 7), ('P3', 'O5', 5),('P2', 'O6', 8), ('P1', 'O6', 4), ('P1', 'O7', 6),('P2', 'O7', 6), ('P1', 'O8', 6), ('P2', 'O8', 6))

    cursor.executemany(sql_9_insert, sql_9_content)
    conn.commit()



    sql10 = """CREATE TABLE HRDEMPLOYEE
            ( EmployeeID varchar(3) NOT NULL,
            Name varchar(25) NOT NULL,
            Title varchar(25) NOT NULL,
            EducationLevel varchar(25) NOT NULL,
            YearOfHire varchar(4) NOT NULL,
            PRIMARY KEY (EmployeeID));"""
    cursor.execute(sql10)
    conn.commit()
    sql_10_insert = "INSERT INTO HRDEMPLOYEE(EmployeeID, Name, Title, EducationLevel, YearOfHire) VALUES (%s,%s,%s,%s,%s)"
    sql_10_content = (('OC1', 'Antonio', 'Order Clerk', 'High School', '2001'), ('OC2', 'Wesley', 'Order Clerk', 'College', '2005'),('OC3', 'Lilly', 'Order Clerk', 'College', '2005'))

    cursor.executemany(sql_10_insert, sql_10_content)
    conn.commit()

    cursor.close()
    conn.close()

except:
    cursor.close()
    conn.close()
