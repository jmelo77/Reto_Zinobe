import os
import requests 
import pandas as pd 
import time
import sqlite3
from hashlib import sha1

class requestsCountry():

    def getCountry(url):
        response=requests.get(url)

        if response:
            pass
        else:
            print('Response Failed')
        return response.json()


class getHash:
    
    def encrypt(language):
        result = sha1(language.encode()).hexdigest()
        return result


class countryDF():
    
    def create(res):
        df = pd.DataFrame(columns=['Region','CityName','Language','Time'])
        start_time = time.time_ns()

        for i in res:

            time.sleep(1e-9)  

            try:
                region=i['region']
                city=i['name']['common']
                lang=list(i['languages'].values())[0]         
                language=getHash.encrypt(lang)
                row = { 'Region':region , 'CityName':city,'Language':language}
                end_time=time.time_ns()-start_time
                row.update({'Time': end_time*1e-6})
                df = df.append(row, ignore_index=True)
                start_time=time.time_ns()

            except:
                pass

        print('--------- Dataframe data.json ----------')
        print(df)
        print(f"total time: {df.Time.sum()} Miliseconds")
        print(f"average time: {df.Time.mean()} Miliseconds")
        print(f"minimum time: {df.Time.min()} Miliseconds")
        print(f"maximum time: {df.Time.max()} Miliseconds")
        return df

    
    def save(df):
        os.makedirs("./DB", exist_ok=True)
        os.makedirs("./JSON", exist_ok=True)
        df.to_json('./JSON/data.json')
        return


class countryDB():

    def viewDB():
        try:
            conn = sqlite3.connect('DB/country.db')
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM country")
            rows = cursor.fetchall()
            return rows        
        except Exception as error:
            print ("Error displaying rows.", error)
        finally:
            conn.close()
    
    def createDB(df):
        conn = sqlite3.connect(os.getcwd()+'/DB/country.db')
        df.to_sql('country', conn, if_exists='replace', index=False)
        cursor = conn.cursor()

        for index in range(len(df)):
            cursor.execute("INSERT INTO country VALUES (?,?,?,?)", df.iloc[index])

        print("----------- Table sqlite ----------------")
        for k in countryDB.viewDB():
            print(k)

        conn.close()