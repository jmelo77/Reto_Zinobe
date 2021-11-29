import unittest
import country

class TestCountry(unittest.TestCase):

    def test_countryAPI(self):
        url = 'https://restcountries.com/v3.1/all'
        response=country.requestsCountry.getCountry(url)
        self.assertIsNotNone(response)

    def test_countryDF(self):
        url = 'https://restcountries.com/v3.1/all'
        res=country.requestsCountry.getCountry(url)
        response=country.countryDF.create(res)
        self.assertIsNotNone(response) 

    def test_countryDB(self):
        response = country.countryDB.viewDB()
        self.assertIsNotNone(response)  

    def test_encode(self):
        response = country.getHash.encrypt('Spanish')
        self.assertIsNotNone(response)  
         
if __name__ == "__main__":
    unittest.main()