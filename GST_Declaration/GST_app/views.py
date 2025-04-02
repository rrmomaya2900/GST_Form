'''
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import GSTForm
from .models import GSTDeclaration
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import GSTDeclarationSerializer

# Home Page
def home(request):
    return render(request, 'home.html')

# View for GST Form (Template-Based Submission)
def gst_form_view(request):
    if request.method == 'POST':
        form = GSTForm(request.POST)
        if form.is_valid():
            # Process form data (e.g., save to database)
            gst_number = form.cleaned_data['gst_number']
            date_of_filing = form.cleaned_data['date_of_filing']
            mobile_number = form.cleaned_data['mobile_number']
            address = form.cleaned_data['address']
            pan_number = form.cleaned_data['pan_number']

            # Redirect to success page
            return redirect('success_page')  # This should match your URL name in urls.py

    else:
        form = GSTForm()

    return render(request, 'form.html', {'form': form})

# API Endpoint for GST Form Submission
@api_view(['POST'])
def submit_gst_form(request):
    if request.method == 'POST':
        form = GSTForm(request.POST)
        if form.is_valid():
            gst_number = form.cleaned_data['gst_number']
            date_of_filing = form.cleaned_data['date_of_filing']
            mobile_number = form.cleaned_data['mobile_number']
            address = form.cleaned_data['address']
            pan_number = form.cleaned_data['pan_number']

            # Redirect to success page
            return redirect('success_page')

    return render(request, 'form.html', {'form': GSTForm()})

# Success Page View (For Template-Based Submission)
def success_page(request):
    return render(request, 'success.html')
'''

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import GSTForm
from .models import GSTDeclaration
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import GSTDeclarationSerializer

# Home Page
def home(request):
    return render(request, 'home.html')

# View for GST Form (Template-Based Submission)
def gst_form_view(request):
    if request.method == 'POST':
        form = GSTForm(request.POST)
        if form.is_valid():
            # Save data to database
            GSTDeclaration.objects.create(
                gst_number=form.cleaned_data['gst_number'],
                date_of_filing=form.cleaned_data['date_of_filing'],
                mobile_number=form.cleaned_data['mobile_number'],
                address=form.cleaned_data['address'],
                pan_number=form.cleaned_data['pan_number']
            )

            # Redirect to success page
            return redirect('success_page')

    else:
        form = GSTForm()

    return render(request, 'form.html', {'form': form})

# ✅ Corrected API Endpoint for GST Form Submission
@api_view(['POST'])
def submit_gst_form(request):
    serializer = GSTDeclarationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "GST Declaration saved successfully!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Success Page View (For Template-Based Submission)
def success_page(request):
    return render(request, 'success.html')


