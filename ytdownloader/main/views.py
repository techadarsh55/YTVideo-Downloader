from django.shortcuts import render
from pytube import YouTube

# Create your views here.
def home(request):
	if request.method=='POST':
		url = request.POST.get("url")
		yt = YouTube(url).streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first().download();


	return render(request,'index.html')