import requests
from bs4 import BeautifulSoup
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def news_list(request):
    if request.method == 'GET' and 'HTTP_X_REQUESTED_WITH' in request.headers and request.headers[
        'HTTP_X_REQUESTED_WITH'] == 'XMLHttpRequest':
        # Replace the URL with the URL of the news website you want to scrape
        url = 'https://www.v2ex.com/'

        # Send a GET request to the URL
        response = requests.get(url)

        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract news headlines
            headlines = []
            for headline in soup.find_all('h2', class_='headline'):
                headlines.append(headline.text.strip())

            # Return the headlines as JSON response
            return JsonResponse({'headlines': headlines})
        else:
            # Return error message if unable to fetch data
            return JsonResponse({'error': 'Unable to fetch news data'}, status=500)
    else:
        # Return error message for invalid requests
        return JsonResponse({'error': 'Invalid request'}, status=400)
