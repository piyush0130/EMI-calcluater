from django.http import HttpResponse

def google_verification_view(request):
    return HttpResponse("google-site-verification: googleb66a2a1986aafb83.html")
