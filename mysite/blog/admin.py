from django.contrib import admin
from .models import Post            # Importanto e incluíndo o modelo Post

# Register your models here.

admin.site.register(Post)           # Tornando o modelo visível na página de administração
