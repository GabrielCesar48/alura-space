# Importando as funções necessárias do Django:
# 'render' é usado para renderizar templates HTML com dados do contexto.
# 'get_object_or_404' é uma função que tenta buscar um objeto no banco de dados; caso não o encontre, gera um erro 404.
# 'Fotografia' é o modelo importado de 'galeria.models' que representa as fotografias na galeria.
from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

# A view index exibe uma lista de fotografias publicadas, ordenadas por data mais recente.
def index(request):
    # Filtra as fotografias publicadas e as ordena pela data de fotografia, do mais recente para o mais antigo.
    fotografias = Fotografia.objects.filter(publicada=True).order_by('-data_fotografia')
    # Renderiza o template 'index.html' passando as fotografias para o contexto como "cards".
    return render(request, 'galeria/index.html', {"cards": fotografias})

# A view imagem exibe uma fotografia específica, identificada por seu ID.
def imagem(request, foto_id):
    # Utiliza 'get_object_or_404' para buscar a fotografia pelo ID ('foto_id'). Se não encontrar, gera erro 404.
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    # Renderiza o template 'imagem.html', passando a fotografia encontrada para o contexto.
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

# A view buscar permite que o usuário busque fotografias por nome.
def buscar(request):
    # Filtra as fotografias publicadas e as ordena pela data de fotografia, do mais recente para o mais antigo.
    fotografias = Fotografia.objects.filter(publicada=True).order_by('-data_fotografia')
    
    # Verifica se o parâmetro 'buscar' está presente na URL.
    if "buscar" in request.GET:
        # Obtém o valor de busca inserido pelo usuário.
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:  # Se o nome de busca não estiver vazio.
            # Filtra as fotografias cujo nome contém a string fornecida pelo usuário (case insensitive).
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    # Renderiza o template 'buscar.html' com as fotografias filtradas como "cards".
    return render(request, "galeria/buscar.html", {"cards": fotografias})
