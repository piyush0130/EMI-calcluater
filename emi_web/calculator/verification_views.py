from django.http import HttpResponse

def robots_txt_view(request):
    robots_content = "User-agent: *\nAllow: /\n"
    return HttpResponse(robots_content, content_type="text/plain")

def google_verification_view(request):
    return HttpResponse("google-site-verification: googleb66a2a1986aafb83.html")

