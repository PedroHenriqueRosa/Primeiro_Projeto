from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <div style="text-align: center; background-color: black; color: white; height: 100vh; display: flex; flex-direction: column; justify-content: center; align-items: center;">
            <h1 style="font-size: 50px;">Vai dar certo!</h1>
        </div>
    """)
