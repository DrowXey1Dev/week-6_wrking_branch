#-----EXERCISE 1-----#
#-----IMPORTS-----#
import os
import pandas as pd
import genius_api
import requests

#class for Genius API
class Genius:
    #instantiate an instance of the class Genius
    def __init__(self, access_token = None):
        #take passed token to use, or fall back to environment variable if none is provided
        self.access_token = access_token or os.environ.get("ACCESS_TOKEN")

    #-----EXERCISE 2-----#
    #methods of the class Genius. This method gets the artist.
    def get_artist(self, search_term):
        #get the full list using the Genius API built in function
        hits = genius_api.genius(search_term)
        #if nothing found return None (very surface level error handling)
        if not hits:
            return None  

        # Step 2: Extract the artist ID from first hit
        #pull the artist ID from the returned array of hits
        first_hit = hits[0]["result"]
        artist_id = first_hit["primary_artist"]["id"]

        #use the Genius API to get artist info
        artist_url = f"https://api.genius.com/artists/{artist_id}"
        headers = {"Authorization": f"Bearer {self.access_token}"}
        response = requests.get(artist_url, headers=headers)
        #return JSON dictionary
        return response.json()

    #-----EXERCISE 3-----#
    #second method of the class Genius. This method takes a list of queries and returns a df
    def get_artists(self, search_terms):
        #empty data array
        data = []
        #parse the query array index by index. Each instance is an instance of class Genius so you can just the above function which is just
        #a method of the class itself, and pass the term into the above function for processing. 
        for term in search_terms:
            info = self.get_artist(term)

        #if info is None or if their is no key, then a blank result is added with None values to keep consistency
            if not info or "response" not in info:
                data.append({
                    "search_term": term,
                    "artist_name": None,
                    "artist_id": None,
                    "followers_count": None
                })
                continue


        #extract the artist information from the response
            artist = info["response"]["artist"]

        #append the clean structured data to our results list
            data.append({
                "search_term": term,
                "artist_name": artist.get("name"),
                "artist_id": artist.get("id"),
                "followers_count": artist.get("followers_count")
            })

        #return a dataframe 
        return pd.DataFrame(data)

        



#---------------------------------------------------------------------------------------------#
#test code (call from external main)
'''
from apputil import Genius
genius = Genius()
print(genius.access_token)
'''
#debug code for exercise 2 (currently does not work)
'''
genius = Genius()
genius.get_artist("Radiohead")
'''

#test code for exercise 3
'''
genius = Genius()
genius.get_artists(["Rihanna", "Tycho", "Seal", "U2"])
'''