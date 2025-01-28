"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http import JsonResponse
import requests  # For making API calls
import json

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def design(request):
    """Renders the design page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/design.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )


def generate_floor_plan(request):
    if request.method == 'POST':
        # Extract form data
        city = request.POST.get('city')
        state = request.POST.get('state')
        apartments = request.POST.get('apartments')
        living_rooms = request.POST.get('livingRooms')
        bedrooms = request.POST.get('bedrooms')
        bathrooms = request.POST.get('bathrooms')
        kitchens = request.POST.get('kitchens')
        additional_details = request.POST.get('additionalDetails')

        # Create a prompt for DALL-E
        prompt = (
            f"Design a floor plan for a building in {city}, {state} with: "
            f"{apartments} apartments, {living_rooms} living rooms, {bedrooms} bedrooms, "
            f"{bathrooms} bathrooms, {kitchens} kitchens. Additional details: {additional_details}."
        )

        # Call DALL-E API (replace with your actual API call)
        api_key = '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'
        headers = {
            "Authorization": f"Bearer {app_key}",
            "Content-Type": "application/json"
        }
        data = {
            "prompt": prompt,
            "n": 1,  # Number of images to generate
            "size": "1024x1024"  # Image size
        }
        response = requests.post(
            "https://api.openai.com/v1/images/generations",
            headers=headers,
            data=json.dumps(data)
        )

        if response.status_code == 200:
            # Extract the image URL from the API response
            image_url = response.json()['data'][0]['url']
            return JsonResponse({'image_url': image_url})
        else:
            return JsonResponse({'error': 'Failed to generate image'}, status=500)

    return render(request, 'app/design.html')

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
