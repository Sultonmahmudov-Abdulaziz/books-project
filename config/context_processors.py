from users.models import Language

def mycontext_processors(request):
    langs = Language.objects.all()
    return {
        "langs":langs,
    }