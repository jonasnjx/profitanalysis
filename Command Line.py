def importdata(): #import data from csv file
    import pandas as pd
    data = pd.read_csv("Merged_Cleaned.csv")
    df = pd.DataFrame(data)
    r = []
    for each in df.Date:  # creating new Year column
        if each[-4:] == "2015":
            r.append("2015")
        elif each[-4:] == "2016":
            r.append("2016")
        elif each[-4:] == "2017":
            r.append("2017")
        elif each[-4:] == "2018":
            r.append("2018")
        elif each[-4:] == "2019":
            r.append("2019")
    df["Year"] = r

    q = []
    for each1 in df.Date:  #creating new Month column
        if each1[0:2] == "1/":
            q.append(1)
        elif each1[0:2] == "2/":
            q.append(2)
        elif each1[0:2] == "3/":
            q.append(3)
        elif each1[0:2] == "4/":
            q.append(4)
        elif each1[0:2] == "5/":
            q.append(5)
        elif each1[0:2] == "6/":
            q.append(6)
        elif each1[0:2] == "7/":
            q.append(7)
        elif each1[0:2] == "8/":
            q.append(8)
        elif each1[0:2] == "9/":
            q.append(9)
        elif each1[0:2] == "10":
            q.append(10)
        elif each1[0:2] == "11":
            q.append(11)
        else:
            q.append(12)
    df["Month"] = q
    return df

def addnewdata(): #allow addition of new data to csv
    import csv
    #Profit = Worth - Amt
    #ER = -(ODAmt/Amt)
    #Quantity = ODAmt/TUPrice
    enter = ["Date e.g 1/31/2019", "Type", "RefNo", "Cur", "TUPrice", "ODAmt", "Amt","Worth", "Customer Code", "StkISN", "CatCode", "Profit", "Exchange Rate","Quantity", "Country"]
    import easygui as g
    title = "New data"
    msg = "Enter new data"
    list = g.multenterbox(msg,title,enter)
    with open("Merged_Cleaned.csv","a") as file_pointer:
        csv_pointer = csv.writer(file_pointer)
        csv_pointer.writerow(list)
    gui()

def monthgetfromyear(year):
    df = importdata()
    df = df[df["Year"] == year]
    month = []
    if df.Month.iloc[-1] == 1:
        month.append("1")
    elif df.Month.iloc[-1] == 2:
        month.append("2")
    elif df.Month.iloc[-1] == 3:
        month.append("3")
    elif df.Month.iloc[-1] == 4:
        month.append("4")
    elif df.Month.iloc[-1] == 5:
        month.append("5")
    elif df.Month.iloc[-1] == 6:
        month.append("6")
    elif df.Month.iloc[-1] == 7:
        month.append("7")
    elif df.Month.iloc[-1] == 8:
        month.append("8")
    elif df.Month.iloc[-1] == 9:
        month.append("9")
    elif df.Month.iloc[-1] == 10:
        month.append("10")
    elif df.Month.iloc[-1] == 11:
        month.append("11")
    else:
        month.append("12")
    return month

def listofmonths(year): #automating retrieval list of months
    #assumption that his business is continuous, cannot have a month without any transaction
    a = monthgetfromyear(year)
    x = int(a[0])
    monthss = []
    for each in range(x):
        monthss.append(each+1)
    return monthss


def listofyears(): #automatic retrieval list of years
    df = importdata()
    a = df.Year.iloc[1]
    b = df.Year.iloc[-1]
    years = int(b)-int(a)
    z = []
    low = 2014
    for each in range(years+1):
        low = low + 1
        z.append(low)
    return z

def first5row(): #print first 5 rows in gui
    df = importdata()
    df1 = df.head()
    import easygui as g
    g.codebox(df1)
    gui()

def last5row(): #print last 5 rows in gui
    df = importdata()
    df1 = df.tail()
    import easygui as g
    g.codebox(df1)
    gui()

def overviewsummary(): #give an overall summary of data
    df = importdata()
    profit = round(df.Profit.sum(),2)
    quantity = round(df.Quantity.sum(),2)
    import easygui as g
    g.codebox("""
    Summary
    --------------------------------------------
    Accumulated profit: ${}
    Accumulated quantity transacted: {} 
    --------------------------------------------""".format(profit, quantity))
    gui()

def profityear(): #give summary of profit by year
    df = importdata()
    year_profit = df.groupby('Year').sum()
    import easygui as g
    g.codebox(year_profit.Profit)
    df1 = df.groupby('Year').sum()
    df2 = df1.Profit
    r = []
    year = listofyears()
    for each in df2:
        r.append(int(each))
    import matplotlib.pyplot as plt
    plt.plot(year,r)
    choice2 = ["Yes","No"]
    msg = "Do you want to see plot?"
    reply3 = g.buttonbox(msg, choices=choice2)
    if reply3 == "Yes":
        plt.show()
        gui()
    else:
        gui()

def profitmonth(): #give summary of profit by months
    df = importdata()
    import easygui as g
    msg = "Choose year"
    reply3 = g.enterbox(msg)
    try:
        if reply3 == "2015":
            df = df[df.Year == "2015"]
            df1 = df.groupby('Month').sum()
            df2 = df1.Profit
            g.codebox(df2)
            profit = []
            month = listofmonths("2015")
            for each in df2:
                profit.append(each)
            import matplotlib.pyplot as plt
            plt.plot(month, profit)
            choice2 = ["Yes", "No"]
            msg = "Do you want to see plot?"
            reply3 = g.buttonbox(msg, choices=choice2)
            if reply3 == "Yes":
                plt.show()
                gui()
            else:
                gui()
        if reply3 == "2016":
            df = df[df.Year == "2016"]
            df1 = df.groupby('Month').sum()
            df2 = df1.Profit
            g.codebox(df2)
            profit = []
            month = listofmonths("2016")
            for each in df2:
                profit.append(each)
            import matplotlib.pyplot as plt
            plt.plot(month, profit)
            choice2 = ["Yes", "No"]
            msg = "Do you want to see plot?"
            reply3 = g.buttonbox(msg, choices=choice2)
            if reply3 == "Yes":
                plt.show()
                gui()
            else:
                gui()
        elif reply3 == "2017":
            df = df[df.Year == "2017"]
            df1 = df.groupby('Month').sum()
            df2 = df1.Profit
            g.codebox(df2)
            profit = []
            month = listofmonths("2017")
            for each in df2:
                profit.append(each)
            import matplotlib.pyplot as plt
            plt.plot(month, profit)
            choice2 = ["Yes", "No"]
            msg = "Do you want to see plot?"
            reply3 = g.buttonbox(msg, choices=choice2)
            if reply3 == "Yes":
                plt.show()
                gui()
            else:
                gui()
        elif reply3 == "2018":
            df = df[df.Year == "2018"]
            df1 = df.groupby('Month').sum()
            df2 = df1.Profit
            g.codebox(df2)
            profit = []
            month = listofmonths("2018")
            for each in df2:
                profit.append(each)
            import matplotlib.pyplot as plt
            plt.plot(month, profit)
            choice2 = ["Yes", "No"]
            msg = "Do you want to see plot?"
            reply3 = g.buttonbox(msg, choices=choice2)
            if reply3 == "Yes":
                plt.show()
                gui()
            else:
                gui()
        elif reply3 == "2019":
            df = df[df.Year == "2019"]
            df1 = df.groupby('Month').sum()
            df2 = df1.Profit
            g.codebox(df2)
            profit = []
            month = listofmonths("2019")
            for each in df2:
                profit.append(each)
            import matplotlib.pyplot as plt
            plt.plot(month, profit)
            choice2 = ["Yes", "No"]
            msg = "Do you want to see plot?"
            reply3 = g.buttonbox(msg, choices=choice2)
            if reply3 == "Yes":
                plt.show()
                gui()
            else:
                gui()
    except ValueError:
        gui()

def quit(): #to quit the program
    import easygui as g
    quit = "Thank you and Good Bye."
    g.msgbox(quit)

def columns(): #give list of column headings
    df = importdata()
    r = []
    for each in df:
        r.append(each)
    str1 = " ".join(str(x) for x in r)
    import easygui as g
    g.msgbox(str1)
    gui()


def customer(): #filter by customer code
    import easygui as g
    try:
        msg = "Type Cust Code: "
        reply3 = g.enterbox(msg)
        reply3 = reply3.upper()
        df = importdata()
        df1 = df[df["Customer Code"] == reply3]
        profit = round(df1.Profit.sum(), 2)
        quantity = round(df1.Quantity.sum(), 2)
        g.codebox(""" 
            {}
    
            Summary:
            --------------------------------------------
            Customer '{}' profit: ${}
            Customer '{}' quantity transacted: {} 
            --------------------------------------------""".format(df1, reply3, profit, reply3, quantity))
        gui()
    except:
        print("Empty DataFrame")


def stock(): #filter by stock code
    import easygui as g
    try:
        msg = "Type Stock Code: "
        reply3 = int(g.enterbox(msg))
        df = importdata()
        df1 = df[df["StkISN"] == reply3]
        profit = round(df1.Profit.sum(), 2)
        quantity = round(df1.Quantity.sum(), 2)
        g.codebox("""
            {}
    
            Summary:
            --------------------------------------------
            Stock '{}' profit: ${}
            Stock '{}' quantity transacted: {} 
            --------------------------------------------""".format(df1, reply3, profit, reply3, quantity))
        gui()
    except ValueError:
        stock()


def location(): #filter by country
    import easygui as g
    msg = "Choose country: "
    choice = ["Singapore", "Malaysia", "Indonesia"]
    reply3 = g.buttonbox(msg, choices=choice)
    df = importdata()
    df1 = df[df["Country"] == reply3]
    profit = round(df1.Profit.sum(), 2)
    quantity = round(df1.Quantity.sum(), 2)
    g.codebox(""" 
        {}

        Summary:
        --------------------------------------------
        Country '{}' profit: ${}
        Country '{}' quantity transacted: {} 
        --------------------------------------------""".format(df1, reply3, profit, reply3, quantity))
    gui()


def type(): #filter by type of product
    import easygui as g
    msg = "Choose type: "
    choice = ["ICG", "ICX"]
    reply3 = g.buttonbox(msg, choices=choice)
    df = importdata()
    df1 = df[df["Type"] == reply3]
    profit = round(df1.Profit.sum(), 2)
    quantity = round(df1.Quantity.sum(), 2)
    g.codebox("""
        {}

        Summary:
        --------------------------------------------
        Type '{}' profit: ${}
        Type '{}' quantity transacted: {}
        --------------------------------------------""".format(df1, reply3, profit, reply3, quantity))
    gui()


def catcode(): #filter by category
    try:
        import easygui as g
        msg = "Type Cat Code: "
        reply3 = g.enterbox(msg)
        reply3 = reply3.upper()
        df = importdata()
        df1 = df[df["CatCode"] == reply3]
        profit = round(df1.Profit.sum(), 2)
        quantity = round(df1.Quantity.sum(), 2)
        g.codebox("""
            {}
    
            Summary:
            --------------------------------------------
            Cat Code '{}' profit: ${}
            Cat Code '{}' quantity transacted: {} 
            --------------------------------------------""".format(df1, reply3, profit, reply3, quantity))
        gui()
    except:
        catcode()

def specific(): #apply many filters
    try:
        specificcol()
    except:
        gui()

def specificcol():
    import easygui as g
    df1 = codespecific()
    choice1 = ["Profit", "Quantity", "Unit Price", "Worth", "Quit"]
    title1 = "Do you want to see specific columns or quit?"
    col = g.choicebox(title1, choices=choice1)
    if col == "Profit":
        df2 = df1.Profit
        g.codebox(df2)
        gui()
    elif col == "Quantity":
        df2 = df1.Quantity
        g.codebox(df2)
        gui()
    elif col == "TUPrice":
        df2 = df1.TUPrice
        g.codebox(df2)
        gui()
    elif col == "Worth":
        df2 = df1.Worth
        g.codebox(df2)
        gui()
    else:
        gui()

def codespecific():
    import easygui as g
    title = "Choose following (Please follow format in data file)"
    choice = ["Date","Type", "CatCode","Customer Code","Country"]
    list = g.multenterbox(title, title, choice)
    df = importdata()
    df1 = df[(df.Date == list[0]) & (df.Type == list[1]) & (df.CatCode == list[2]) & (df["Customer Code"] == list[3]) & (df.Country == list[4])]
    g.codebox(df1)
    return df1

def back(): #allow to go back in the program
    import easygui as g
    msg = "Choose your options please"
    choice1 = ["Add New","Overview", "Profits", "Customer", "Stock", "Location", "Type", "CatCode", "Specific"]
    reply = g.buttonbox(msg, choices=choice1)
    return reply

def gui(): #creation of the gui
    import easygui as g
    msg = "BC0401: Do you want to continue?"
    choice = ["Yes", "No"]
    reply0 = g.buttonbox(msg, choices=choice)
    if reply0 == "Yes":
        reply = back()
        if reply == "Add New":
            msg1 = "Do you have new data to input"
            choice = ["Yes", "No"]
            reply20 = g.buttonbox(msg1, choices = choice)
            if reply20 == "Yes":
                try:
                    addnewdata()
                except:
                    gui()
            else:
                gui()
        elif reply == "Overview":
            try:
                msg = "Choose your options please"
                choice2 = ["Columns", "First 5 Data", "Last 5 Data", "Summary", "Back"]
                reply2 = g.buttonbox(msg, choices=choice2)
                if reply2 == "Columns":
                    columns()
                elif reply2 == "First 5 Data":
                    first5row()
                elif reply2 == "Last 5 Data":
                    last5row()
                elif reply2 == "Summary":
                    overviewsummary()
                elif reply2 == "Back":
                    gui()
            except:
                gui()
        elif reply == "Profits":
            msg = "Choose your options please"
            choice2 = ["Year", "Month","Back"]
            reply3 = g.buttonbox(msg, choices=choice2)
            if reply3 == "Year":
                profityear()
            elif reply3 == "Month":
                profitmonth()
            elif reply3 == "Back":
                gui()
        elif reply == "Customer":
            customer()
        elif reply == "Stock":
            stock()
        elif reply == "Location":
            location()
        elif reply == "Type":
            type()
        elif reply == "CatCode":
            catcode()
        elif reply == "Specific":
            specific()
        else:
            g.msgbox("Thank you and good bye!")
    else:
        quit()

#================================================================================================================
#start:
gui()

