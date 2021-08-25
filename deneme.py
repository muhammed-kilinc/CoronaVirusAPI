import http.client
from tkinter import * 
import json  


  
root =Tk()

def search ():
    

    app= Tk()
    app.title (countryEntry.get())

    app_width = 350
    app_height = 260



    screen_height = app.winfo_screenheight()
    screen_width = app.winfo_screenwidth()


    x= (screen_width / 2) - (app_width / 2)
    y= (screen_height / 2) - (app_height / 2)


    app.geometry (f'{app_width}x{app_height}+{int(x)}+{int(y)}')
    app.resizable (0,0)


    country =countryEntry.get()

    conn = http.client.HTTPSConnection("api.collectapi.com")

    headers = {
        'content-type': "application/json",
        'authorization': " "

        }
    conn.request("GET", f"/corona/countriesData?country={country}", headers=headers)
    res = conn.getresponse()
    data = res.read().decode()
    json_data = json.loads(data)
    


    
    countryName =(json_data["result"][0]["country"])
    totalCases =(json_data["result"][0]["totalCases"])
    newCases =(json_data["result"][0]["newCases"])
    totalDeaths =(json_data["result"][0]["totalDeaths"])
    newDeaths =(json_data["result"][0]["newDeaths"])
    activeCases =(json_data["result"][0]["activeCases"])
    
    countryNameL = Label (app,text=countryName, font=("calibri",15))
    countryNameL.pack(fill=BOTH, ipady="10",padx="20")


    totalCasesL = Label(app,text=f"total cases: {totalCases}",font=("calibri",11))
    totalCasesL.pack(fill=BOTH, ipady="10",padx="20")

    newCasesL = Label (app,text=f"new cases: {newCases}",font=("calibri",11))
    newCasesL.pack(fill=BOTH, ipady="10",padx="20") 


    totalDeathsL = Label(app,text=f"total deaths: {totalDeaths}",font=("calibri",11))
    totalDeathsL.pack(fill=BOTH, ipady="10",padx="20")

    newDeathsL = Label (app,text=f"new deaths: {newDeaths}",font=("calibri",11))
    newDeathsL.pack(fill=BOTH, ipady="10",padx="20")


    activeCasesL = Label(app,text=f"active cases: {activeCases}",font=("calibri",11))
    activeCasesL.pack(fill=BOTH, ipady="10",padx="20")

    app.mainloop()





root.title ("CoronaVirus")






app_width = 350
app_height = 140



screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()


x= (screen_width / 2) - (app_width / 2)
y= (screen_height / 2) - (app_height / 2)


root.geometry (f'{app_width}x{app_height}+{int(x)}+{int(y)}')
root.resizable (0,0)

countryEntry = Entry(font=("Arial",15) )
countryEntry.focus()
countryEntry.pack(fill=BOTH, ipady="10",padx="20")


searchButon = Button(text="search", font=("Arial",15) ,command=search)
searchButon.pack(fill=BOTH, ipady="10",padx="20")





    

root.mainloop()