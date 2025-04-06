import requests
from bs4 import BeautifulSoup
import re

# source: https://www.myallgarbage.com/p/bn-dialogue.html

# List of URLs to scrape
urls = [
     "https://www.myallgarbage.com/2022/11/advertisement.html",
    "https://www.myallgarbage.com/2022/11/violence-against-children-and-women.html",
    "https://www.myallgarbage.com/2022/11/importance-of-reading-books.html",
    "https://www.myallgarbage.com/2022/11/road-accident.html",
    "https://www.myallgarbage.com/2022/11/importance-of-tree-planting.html",
    "https://www.myallgarbage.com/2022/11/full-moon-night.html",
    "https://www.myallgarbage.com/2022/11/facebook.html",
    "https://www.myallgarbage.com/2022/11/child-marriage.html",
    "https://www.myallgarbage.com/2022/11/nirapod-sorok-chai.html",
    "https://www.myallgarbage.com/2021/10/dialogue-world-temperature-global-warming.html",
    "https://www.myallgarbage.com/2021/10/dialogue-bd-cricket-team.html",
    "https://www.myallgarbage.com/2021/10/dialogue-bangladesh-cricket.html",
    "https://www.myallgarbage.com/2021/10/dialogue-culture-non-culture.html",
    "https://www.myallgarbage.com/2021/11/commodity-prices-rise.html",
    "https://www.myallgarbage.com/2021/10/dialogue-future-plan.html",
    "https://www.myallgarbage.com/2021/10/dialogue-coaching-banijjo.html",
    "https://www.myallgarbage.com/2021/10/dialogue-bangla-vasa-language.html",
    "https://www.myallgarbage.com/2021/10/dialogue-addicted-indian-serial.html",
    "https://www.myallgarbage.com/2021/11/dialogue-study-tour.html",
    "https://www.myallgarbage.com/2021/10/dialogue-language-movement.html",
    "https://www.myallgarbage.com/2021/10/dialogue-booimela-bookfair.html",
    "https://www.myallgarbage.com/2021/10/dialogue-technogoly-uses.html",
    "https://www.myallgarbage.com/2021/10/dialogue-harmfull-smoking.html",
    "https://www.myallgarbage.com/2021/10/dialogue-internet-use-abuse.html",
    "https://www.myallgarbage.com/2021/10/dialogue-cleen-dhaka.html",
    "https://www.myallgarbage.com/2021/10/dialogue-nagoriker-kortobbo.html",
    "https://www.myallgarbage.com/2022/11/female-education.html",
    "https://www.myallgarbage.com/2021/11/importance-of-female-education.html",
    "https://www.myallgarbage.com/2021/10/dialogue-1971-freedom-war.html",
    "https://www.myallgarbage.com/2021/10/dialogue-tree-plantition.html",
    "https://www.myallgarbage.com/2021/11/samprodaik-sompriti.html",
    "https://www.myallgarbage.com/2021/11/reading-newspaper.html",
    "https://www.myallgarbage.com/2021/11/pothochari-o-harano-shishu.html",
    "https://www.myallgarbage.com/2021/11/chor-polish.html",
    "https://www.myallgarbage.com/2021/10/dialogue-voter-candidate.html",
    "https://www.myallgarbage.com/2021/11/shopkeepers-children-and-shoppers.html",
    "https://www.myallgarbage.com/2021/11/birongona-and-sangbadik.html",
    "https://www.myallgarbage.com/2021/10/dialogue-bangladesh-cricket-team.html",
    "https://www.myallgarbage.com/2021/10/dialogue-saf-footbal.html",
    "https://www.myallgarbage.com/2021/10/dialogue-earthque.html",
    "https://www.myallgarbage.com/2021/10/dialogue-samprodaik-sompriti.html",
    "https://www.myallgarbage.com/2021/10/dialogue-bangla-noboborso.html",
    "https://www.myallgarbage.com/2021/11/higher-education.html",
    "https://www.myallgarbage.com/2021/10/dialogue-importance-female-education.html",
    "https://www.myallgarbage.com/2021/10/dialogue-importance-tree-plantion.html",
    "https://www.myallgarbage.com/2021/11/recent-read-book.html",
    "https://www.myallgarbage.com/2021/11/farmer-and-his-wife.html",
    "https://www.myallgarbage.com/2021/11/student-and-ticket-checker.html",
    "https://www.myallgarbage.com/2021/10/dialogue-piyon-officer.html",
    "https://www.myallgarbage.com/2021/10/dialogue-shohid-minar.html",
    "https://www.myallgarbage.com/2021/11/dialogue-on-two-friends.html",
    "https://www.myallgarbage.com/2021/10/dialogue-national-anthen.html",
    "https://www.myallgarbage.com/2021/10/dialoguee-rickshaw-puller.html",
    "https://www.myallgarbage.com/2021/10/dialogue-establish-library.html",
    "https://www.myallgarbage.com/2021/10/dialogue-independence-day.html",
    "https://www.myallgarbage.com/2021/10/dialogue-public-awaerness.html",
    "https://www.myallgarbage.com/2021/11/dui-vaiyer-songlap.html",
    "https://www.myallgarbage.com/2021/11/victory-day-event.html",
    "https://www.myallgarbage.com/2021/10/dialogue-exam-result.html",
    "https://www.myallgarbage.com/2021/11/dialogue-with-mohajon.html",
    "https://www.myallgarbage.com/2021/11/uses-of-mobile-phone.html",
    "https://www.myallgarbage.com/2021/10/dialogue-river-water.html",
    "https://www.myallgarbage.com/2021/10/dialogue-tokai-and-you.html",
    "https://www.myallgarbage.com/2021/11/dialogue-between-two-umpire.html",
    "https://www.myallgarbage.com/2021/11/dialogue-mango-tree-plantation.html",
    "https://www.myallgarbage.com/2021/10/dialogue-dadu-nati.html",
    "https://www.myallgarbage.com/2021/11/botgach-and-pakhi.html",
    "https://www.myallgarbage.com/2021/10/dialogue-study-tour.html",
    "https://www.myallgarbage.com/2021/11/gift-for-daughter.html",
    "https://www.myallgarbage.com/2021/10/dialogue-ideal-politics.html",
    "https://www.myallgarbage.com/2021/11/dialogue-for-buying-tv.html",
    "https://www.myallgarbage.com/2021/11/story-of-liberation-war.html",
    "https://www.myallgarbage.com/2021/10/dialogue-visit-zoo.html",
    "https://www.myallgarbage.com/2021/10/trees-also-have-life.html",
    "https://www.myallgarbage.com/2021/10/global-warming.html",
    "https://www.myallgarbage.com/2021/10/dialogue-traffic-jam.html",
    "https://www.myallgarbage.com/2021/10/dialogue-environment-pollution.html",
    "https://www.myallgarbage.com/2021/10/poetry-and-poet-lover.html",
    "https://www.myallgarbage.com/2021/10/dialogue-choose-friend.html",
    "https://www.myallgarbage.com/2021/10/dialogue-value-of-time.html",
    "https://www.myallgarbage.com/2021/10/dialogue-smoking-badside-effect.html",
    "https://www.myallgarbage.com/2021/10/dont-take-medicine-without-prescribed.html",
    "https://www.myallgarbage.com/2021/10/bariwala-bharatiya-problem.html",
    "https://www.myallgarbage.com/2021/10/dialogue-picnic-plan.html",
    "https://www.myallgarbage.com/2021/10/dialogue-celebrate-birthday.html",
    "https://www.myallgarbage.com/2021/10/dialogue-help-for-friend.html",
    "https://www.myallgarbage.com/2021/10/dialogue-eve-teasing.html",
    "https://www.myallgarbage.com/2021/10/dialogue-marriage-ceremony.html",
    "https://www.myallgarbage.com/2021/10/dialogue-satelite-channel.html",
    "https://www.myallgarbage.com/2021/10/science-effect-on-human-life.html",
    "https://www.myallgarbage.com/2021/10/dialogue-reading-newspaper.html",
    "https://www.myallgarbage.com/2021/10/dialogue-price-hike.html",
    "https://www.myallgarbage.com/2021/10/pros-and-cons-of-internet.html",
    "https://www.myallgarbage.com/2021/10/poromotsohishnuta.html",
    "https://www.myallgarbage.com/2021/10/dialogue-ganchorchay-biggan.html",
    "https://www.myallgarbage.com/2021/10/dialogue-abuse-mobile-phone.html",
    "https://www.myallgarbage.com/2021/10/dialogue-road-accident.html",
    "https://www.myallgarbage.com/2021/10/dialogue-freedomfighter-journalist.html",
    "https://www.myallgarbage.com/2021/10/dialogue-mother-language.html",
    "https://www.myallgarbage.com/2021/10/dialogue-science-effect-in-humanlife.html",
    "https://www.myallgarbage.com/2021/10/dialogue-kuruci-purno-cinema.html",
    "https://www.myallgarbage.com/2021/10/jute-mil-off.html",
    "https://www.myallgarbage.com/2021/10/job-interview.html",
    "https://www.myallgarbage.com/2021/10/khadye-bhejal.html",
    "https://www.myallgarbage.com/2021/10/rural-and-city-life.html",
    "https://www.myallgarbage.com/2021/10/accommodation-problem.html",
    "https://www.myallgarbage.com/2021/10/population-problem.html",
    "https://www.myallgarbage.com/2021/10/educational-violence.html",
    "https://www.myallgarbage.com/2021/10/dialogue-on-farmer-and-worker.html"
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

            # Find the div with the specified class and id
            post_body = soup.find('div', class_='post-body entry-content', id='post-body')
            
            if post_body:
                # Extract the text
                bangla_text = post_body.get_text(separator='\n', strip=True)
                
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
                file.write('\n---\n\n')
        else:
            print(f"Failed to retrieve the webpage at {url}. Status code: {response.status_code}")

print("Output has been written to '01.txt'")
