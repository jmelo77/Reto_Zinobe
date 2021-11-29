import country

if __name__ == "__main__":
    url = 'https://restcountries.com/v3.1/all'
    response=country.requestsCountry.getCountry(url)
    df=country.countryDF.create(response)
    country.countryDF.save(df)
    country.countryDB.createDB(df)