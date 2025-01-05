import requests
from bs4 import BeautifulSoup
import re
url={
    "Drama": 'https://www.imdb.com/search/title/?title_type=feature&genres=drama',
    "Action": 'https://www.imdb.com/search/title/?title_type=feature&genres=action',
    "Comedy": 'https://www.imdb.com/search/title/?title_type=feature&genres=comedy',
    "Horror": 'https://www.imdb.com/search/title/?title_type=feature&genres=horror',
    "Crime": 'https://www.imdb.com/search/title/?title_type=feature&genres=crime',
}
def main(emotion):
    Urls=url.get(emotion)
    print("correct",Urls)
    if not Urls: 
        print("invalid emotions.")
        return[]
    
    headers={
        'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
    try:
        response = requests.get(Urls,headers=headers)
        response.raise_for_status()
        
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return[]
    
    soup = BeautifulSoup(response.text, "lxml")  
    
    titles = [a.get_text() for a in soup.find_all('a', href=re.compile(r'/title/tt\d+/'))] 
    return titles

if __name__=='__main__':
    emotion = input("Enter the emotions:").strip()
    movie_titles = main(emotion)

if not movie_titles:
    print("No titles were found.")
else:
    max_titles = 14 if emotion in ["Drama", "Actions", "Comedy", "Horror", "Crime"] else 12
    for title in movie_titles[:max_titles]:
        print(title)
       
        
        