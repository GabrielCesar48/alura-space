from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth


def login(request):
    form = LoginForms() # Inicializa o formulário

    if request.method == 'POST':
        #Lógica de Login
        # Preenche o formulário com os dados do POST
        form = LoginForms(request.POST)
        
        #Validar Formulário
        if form.is_valid():
            nome = form.cleaned_data['nome_login'] # Obtem o nome de usuário. Utilize cleaned_data para segurançar os dados
            senha = form.cleaned_data['senha'] # Obtem a senha. Utilize cleaned_data para segurança

            usuario = auth.authenticate(request, username=nome, password=senha) # Autentica o usuário
            if usuario is not None:
                auth.login(request, usuario) # Faz o login do usuário
                return redirect('index') # Redireciona para a página inicial
            else:
                form.add_error( # Adiciona um erro ao formulário
                    "senha",
                    "Nome de usuário ou senha inválidos."
                )
                return render(request, 'usuarios/login.html', {'form': form})
            
    # Se o formulário for inválido, ele será renderizado novamente com os erros        
    return render(request, 'usuarios/login.html', {'form': form}) #Renderiza o template com o formulário


def cadastro(request):
    form = CadastroForms()  # Cria um formulário vazio para exibição inicial.  Só existe uma instância

    if request.method == 'POST':
        form = CadastroForms(request.POST)  # Cria um formulário com os dados enviados pelo usuário.  Só existe uma instância
        
        if form.is_valid():  # Verifica se todos os campos do formulário são válidos
            # Recupera os dados do formulário limpo, garantindo que são válidos
            nome = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha1']
                
            if User.objects.filter(email=email).exists():
                form.add_error(  # Adiciona um erro específico ao campo email
                    "email",
                    "Email já cadastrado."
                )
                return render(request, 'usuarios/cadastro.html', {'form': form})
            
            try:  # Usa um bloco try-except para capturar erros de criação de usuário
                usuario = User.objects.create_user(
                    username=nome,
                    email=email,
                    password=senha,
                )
                usuario.save()
                return redirect('login')  # Redireciona para a página de login após cadastro bem-sucedido.
            except Exception as e:
                form.add_error(
                    "first_name", f"Erro ao criar usuário: {str(e)}"  # Informa o erro ao usuário
                )
                form.add_error(
                    "email", f"Erro ao criar usuário: {str(e)}"
                )
                return render(request, 'usuarios/cadastro.html', {'form': form})
            
        else:
            # Se o formulário não for válido, renderiza a mesma página com os erros.
            return render(request, 'usuarios/cadastro.html', {'form': form})
    return render(request, 'usuarios/cadastro.html', {'form': form})







def logout(request):
    auth.logout(request)
    return redirect('login')




