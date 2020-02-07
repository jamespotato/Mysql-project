#Author Guan Jiajun


import pymysql
from datetime import datetime


conn = pymysql.connect(host = '127.0.0.1',user ='root',password = 'root',port = 3306,
    charset = 'utf8mb4',cursorclass = pymysql.cursors.DictCursor)
cursor = conn.cursor()

try:
    sql_useorder = "USE bigz_order"
    cursor.execute(sql_useorder)

    conn.commit()

    sql2 = """select ProductID, ProductName, ProductType, SupplierName
            from PRODUCT NATURAL JOIN SUPPLIER;"""
    cursor.execute(sql2)
    results_1 = cursor.fetchall()
    product_list = []

    for i in range(0,len(results_1)):
        product_list.append(list(results_1[i].values()))
        The_buffer = [i+1]
        product_list[i].extend(The_buffer)

    sql_usedwhb = "USE bigz_dwhb"
    cursor.execute(sql_usedwhb)

    conn.commit()

    sql_1_insert = "INSERT INTO PRODUCT(ProductID, ProductName, ProductType, ProductSupplierName, ProductKey) VALUES (%s,%s,%s,%s,%s)"

    cursor.executemany(sql_1_insert, product_list)
    conn.commit()


    cursor.execute(sql_useorder)

    conn.commit()

    sql3 = """select *
            from CUSTOMER;"""
    cursor.execute(sql3)
    results_2 = cursor.fetchall()
    customer_list = []

    for i in range(0,len(results_2)):
        customer_list.append(list(results_2[i].values()))
        The_buffer = [i+1]
        customer_list[i].extend(The_buffer)

    cursor.execute(sql_usedwhb)

    conn.commit()

    sql_2_insert = "INSERT INTO CUSTOMER(CustomerID, CustomerName, CustomerType, CustomerZip, CustomerKey) VALUES (%s,%s,%s,%s,%s)"

    cursor.executemany(sql_2_insert, customer_list)

    conn.commit()



    cursor.execute(sql_useorder)

    conn.commit()

    sql4 = """select *
            from DEPOT;"""
    cursor.execute(sql4)
    results_3 = cursor.fetchall()
    depot_list = []

    for i in range(0,len(results_3)):
        depot_list.append(list(results_3[i].values()))
        The_buffer = [i+1]
        depot_list[i].extend(The_buffer)


    cursor.execute(sql_usedwhb)
    conn.commit()

    sql_3_insert = "INSERT INTO DEPOT(DepotID, DepotSize, DepotZip, DepotKey) VALUES (%s,%s,%s,%s)"

    cursor.executemany(sql_3_insert, depot_list)
    conn.commit()


    cursor.execute(sql_useorder)

    conn.commit()


    sql5 = """select *from HRDEMPLOYEE join ORDERCLERK where HRDEMPLOYEE.EmployeeID = ORDERCLERK.OCID;"""
    cursor.execute(sql5)
    results_4 = cursor.fetchall()
    employee_list = []

    for i in range(0,len(results_4)):
        results_4[i] = list(results_4[i].values())
        if len(results_4[i][1]) > len(results_4[i][6]):
            Temperlist = [i+1,results_4[i][0],results_4[i][1],results_4[i][2],results_4[i][3],results_4[i][4]]
        else:
            Temperlist = [i+1,results_4[i][0],results_4[i][6],results_4[i][2],results_4[i][3],results_4[i][4]]
        employee_list.append(Temperlist)


    cursor.execute(sql_usedwhb)

    conn.commit()

    sql_4_insert = "INSERT INTO ORDERCLERK(OrderClerkKey, OrderClerkID, OrderClerkName, OrderClerkTitle, OrderClerkEducationLevel, OrderClerkYearOfHire) VALUES (%s,%s,%s,%s,%s,%s)"

    cursor.executemany(sql_4_insert, employee_list)
    conn.commit()



    cursor.execute(sql_useorder)

    conn.commit()

    sql6 = """select DISTINCT OrderDate
            from ORDERLIST;"""
    cursor.execute(sql6)
    results_5 = cursor.fetchall()

    orederdate_list = []

    for i in range(0,len(results_5)):
        date_data = list(results_5[i].values())[0].split('-')
        month = ""
        weekday = ""
        quarter = ""
        month_dict = {'Jan':'01','Feb':'02',"Mar":'03',"Apr":"04","May":"05","Jun":"06","Jul":'07',
        "Aug":"08","Sept":"09","Oct":"10","Nov":"11","Dec":"12"}

        month = month_dict[date_data[1]]

        dayofmonth = int(date_data[0])
        if len(date_data[0]) == 1:
            day = "0" + date_data[0]
        fulldate = date_data[2] + month + day
        week = datetime.strptime(fulldate, "%Y%m%d").weekday()

        week_dict = {1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday"}
        weekday = week_dict[week]

        monthnumber = int(month)
        quarter = "Q"+str((monthnumber-1)//3+1)

        Temperlist = [i+1, list(results_5[i].values())[0], weekday, int(date_data[0]), date_data[1], quarter, date_data[2]]
        orederdate_list.append(Temperlist)


    cursor.execute(sql_usedwhb)

    conn.commit()

    sql_5_insert = "INSERT INTO CALENDAR(CalendarKey, FullDate, DayOfWeek, DayOfMonth, Month, Quarter, Year) VALUES (%s,%s,%s,%s,%s,%s,%s)"

    cursor.executemany(sql_5_insert, orederdate_list)
    conn.commit()


    cursor.execute(sql_useorder)

    conn.commit()

    sql7 = """select *
            from ORDERLIST  natural join ORDEREDVIA;"""
    cursor.execute(sql7)
    results_6 = cursor.fetchall()
    oreder_list = []
    for i in range(0,len(results_6)):
        calendarkey = 0
        customerkey = 0
        depotkey = 0
        orderclerkkey = 0
        productkey = 0
        results_6[i] = list(results_6[i].values())
        for j in range(0,len(orederdate_list)):
            if results_6[i][1] == orederdate_list[j][1]:
                calendarkey = orederdate_list[j][0]
        for j in range(0,len(customer_list)):
            if results_6[i][3] == customer_list[j][0]:
                customerkey = customer_list[j][4]
        for j in range(0,len(depot_list)):
            if results_6[i][5] == depot_list[j][0]:
                depotkey = depot_list[j][3]
        for j in range(0,len(employee_list)):
            if results_6[i][4] == employee_list[j][1]:
                orderclerkkey = employee_list[j][0]
        for j in range(0,len(product_list)):
            if results_6[i][6] == product_list[j][0]:
                productkey = product_list[j][4]
        Temperlist = [calendarkey, customerkey, depotkey, orderclerkkey, productkey, results_6[i][0], results_6[i][2], results_6[i][7]]
        oreder_list.append(Temperlist)
    poplist = []
    for n in range(0,len(oreder_list)):
        for m in range(n+1,len(oreder_list)):
            if oreder_list[n][0] == oreder_list[m][0] and oreder_list[n][1] == oreder_list[m][1] and oreder_list[n][2] == oreder_list[m][2] and oreder_list[n][3] == oreder_list[m][3] and oreder_list[n][4] == oreder_list[m][4] and oreder_list[n][6] == oreder_list[m][6] and oreder_list[n][7] == oreder_list[m][7]:
                poplist.append(m)
    poplist.sort(reverse=True)
    for n in range(0,len(poplist)):
        oreder_list.pop(poplist[n])


    cursor.execute(sql_usedwhb)





    conn.commit()

    sql_6_insert = "INSERT INTO ORDERCHECK(CalendarKey, CustomerKey, DepotKey, OrderClerkKey, ProductKey, OrderID, Time, Quantity) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"


    cursor.executemany(sql_6_insert, oreder_list)
    conn.commit()
    print("finish")
    cursor.close()
    conn.close()



except Exception as e:
    cursor.close()
    conn.close()
    print(e)
