import requests
from bs4 import BeautifulSoup
import re

# Source: https://www.myallgarbage.com/p/oviggota.html

# List of URLs to scrape
urls = [
    "https://www.myallgarbage.com/2022/03/shah-jalal-mazar.html",
    "https://www.myallgarbage.com/2022/03/nobo-theater.html",
    "https://www.myallgarbage.com/2022/03/nobin-boron.html",
    "https://www.myallgarbage.com/2022/03/bidyuthin-rat.html",
    "https://www.myallgarbage.com/2022/03/visiting-historical-place.html",
    "https://www.myallgarbage.com/2021/09/college-jiboner-gotona.html",
    "https://www.myallgarbage.com/2021/09/college-protom-din.html",
    "https://www.myallgarbage.com/2021/09/siter-sokaler-oviggotha.html",
    "https://www.myallgarbage.com/2021/09/paharpur-bowddhubihar.html",
    "https://www.myallgarbage.com/2021/09/borshon-mukor-shondha.html",
    "https://www.myallgarbage.com/2021/09/jathiyo-sritishowdh.html",
    "https://www.myallgarbage.com/2021/09/pohela-boisak.html",
    "https://www.myallgarbage.com/2021/09/shohidh-minar.html",
    "https://www.myallgarbage.com/2021/09/janjot-oviggotha.html",
    "https://www.myallgarbage.com/2021/09/borendru-jadugor.html",
    "https://www.myallgarbage.com/2021/09/moinamothi-poridorshon.html",
    "https://www.myallgarbage.com/2021/09/purnima-rat.html",
    "https://www.myallgarbage.com/2021/09/biggan-mela.html",
    "https://www.myallgarbage.com/2021/09/ahsan-monjil-oviggotha.html",
    "https://www.myallgarbage.com/2021/09/mukthijoddhu-jadhugor.html",
    "https://www.myallgarbage.com/2021/09/sadhinotha-dibosh.html",
    "https://www.myallgarbage.com/2021/09/jathiyo-jadhugor.html",
    "https://www.myallgarbage.com/2021/09/lokshilpo-jadhugor.html",
    "https://www.myallgarbage.com/2021/09/sandmartin-vromon.html",
    "https://www.myallgarbage.com/2021/09/kanthujir-mondhir.html",
    "https://www.myallgarbage.com/2021/09/boishabi-uthsobh.html",
    "https://www.myallgarbage.com/2021/09/sundorvon-vromon.html",
    "https://www.myallgarbage.com/2021/09/bangabandhu-sriti-jadugor.html",
    "https://www.myallgarbage.com/2021/09/bangabandhu-somadhisowdh.html",
    "https://www.myallgarbage.com/2021/09/porikkar-purbo-rat.html",
    "https://www.myallgarbage.com/2021/09/shitakundo-pahar.html",
    "https://www.myallgarbage.com/2021/09/kalboishakir-oviggotha.html",
    "https://www.myallgarbage.com/2021/09/lalon-akhra.html",
    "https://www.myallgarbage.com/2021/09/bodhuvomi-poridhorshon.html",
    "https://www.myallgarbage.com/2021/09/bangabandhu-cafari-park.html",
    "https://www.myallgarbage.com/2021/09/cha-bagan-vromon.html",
    "https://www.myallgarbage.com/2021/09/hostel-jibon.html",
    "https://www.myallgarbage.com/2021/09/purnima-raat.html",
    "https://www.myallgarbage.com/2021/09/osusthu-bondhuke-deka.html",
    "https://www.myallgarbage.com/2021/09/cintaiyer-oviggotha.html",
    "https://www.myallgarbage.com/2021/09/atithu-grohon.html",
    "https://www.myallgarbage.com/2021/09/dokker-oviggotha.html",
    "https://www.myallgarbage.com/2021/09/vikarir-mohanuvovotha.html",
    "https://www.myallgarbage.com/2021/09/bonghopsagorer-oviggotha.html",
    "https://www.myallgarbage.com/2021/09/nodhite-habodobo.html",
    "https://www.myallgarbage.com/2021/09/nowka-baich.html",
    "https://www.myallgarbage.com/2021/09/sidorer-rater-oviggotha.html",
    "https://www.myallgarbage.com/2021/09/nawka-dobi.html",
    "https://www.myallgarbage.com/2021/09/rate-ekaki-poth-cola.html",
    "https://www.myallgarbage.com/2021/09/mojar-oviggutha.html",
    "https://www.myallgarbage.com/2021/09/rail-station.html",
    "https://www.myallgarbage.com/2021/09/cycle-vromon.html"
]

# Open the file in write mode
with open('01.txt', 'w', encoding='utf-8') as file:
    for url in urls:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find the main div with class and id
            post_body = soup.find('div', class_='post-body entry-content', id='post-body')
            
            if post_body:
                # Find the div with the specified style within the main div
                justified_div = post_body.find('div', style='text-align: justify;')
                
                if justified_div:
                    # Extract the text
                    bangla_text = justified_div.get_text(separator='\n', strip=True)
                    
                    # Split the text into lines
                    lines = bangla_text.split('\n')
                    
                    # Filter out lines that end with a colon
                    filtered_lines = [line for line in lines if not line.strip().endswith(':')]
                    
                    # Join the filtered lines into a single string
                    filtered_text = ' '.join(filtered_lines)
                    
                    # Split the text into sentences
                    sentences = re.split(r'(?<=[।])\s*', filtered_text)
                    
                    # Write each sentence to a new line in the file
                    for sentence in sentences:
                        if sentence.strip():
                            file.write(sentence.strip() + '\n')
                    
                    # Add a separator between different URLs
                    # file.write('\n')
        else: 
            print(f"Failed to retrieve the webpage at {url}. Status code: {response.status_code}")

print("Output has been written to '01.txt'")
