import time
import requests

def lambda_handler(event, context):
    urls = [
        "https://omdena-laguna-ph-fisheries-recommender.streamlit.app/",
        "https://jplaulau14-dsf9-capstone-main-hauaqj.streamlit.app/"
    ]

    for url in urls:
        requests.get(url)
        time.sleep(5)
