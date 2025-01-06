from django.core.exceptions import ValidationError
from django import forms



class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label="Nome de Login",
        widget=forms.TextInput(attrs={
            "autofocus": True,
            "class": "form-control",
            "placeholder": "Ex.: João Silva",
            }),
        required=True,
        max_length=100,
    )

    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite Sua Senha"
            }
        ),
    )

class CadastroForms(forms.Form):
     first_name = forms.CharField(
         label="Nome Usuario",
         widget=forms.TextInput(attrs={
             "autofocus": True,
             "class": "form-control",
             "placeholder": "Ex.: João123",
             }),
         required=True,
         max_length=100,
     )
     
     email = forms.EmailField(
         label="Email",
         widget=forms.EmailInput(attrs={
             "class": "form-control",
             "placeholder": "Ex.: joaosilva@xpto.com",
             }),
         required=True,
         validators=[],
     )
     
     senha1 = forms.CharField(
         label="Senha",
         required=True,
         max_length=70,
         widget=forms.PasswordInput(
             attrs={
                 "class": "form-control",
                 "placeholder": "Digite Sua Senha"
             }
         ),
     )
     
     senha2 = forms.CharField(     
         label="Confirme sua senha",
         required=True,
         max_length=70,
         widget=forms.PasswordInput(
             attrs={
                 "class": "form-control",
                 "placeholder": "Digite Sua Senha"
             }
         ),
         )
     
     from django.core.exceptions import ValidationError

    
     def clean_email(self):
         email = self.cleaned_data.get('email', '').strip()
         print(f"Validando email: {email}")  # Teste para ver se a validação é executada
         
         if not email:
             self.add_error("email", "O campo email deve ser preenchido.")
         
         if '@' not in email:
             self.add_error("email", "O email deve conter um @.")
         
         if '.' not in email.split('@')[-1]:
             self.add_error("email", "O domínio do e-mail deve conter um ponto (exemplo: '.com').")
         
         return email

     
     def clean_first_name(self):
         nome = self.cleaned_data['first_name']
         if nome:
             nome = nome.strip()
             if ' ' in nome:
                 self.add_error(
                     "first_name",
                     "O nome não pode conter espaços."
                 )
                 return nome
             return nome
     def clean(self):
        # Limpa e valida os dados do formulário
        cleaned_data = super().clean()
        senha_1 = cleaned_data.get('senha1')
        senha_2 = cleaned_data.get('senha2')

        print("Metodo clean chamado")

        # Verifica se as senhas coincidem
        if senha_1 and senha_2 and senha_1 != senha_2:
            # raise forms.ValidationError("As senhas não coincidem.")
            # Adiciona um erro específico ao campo email
            self.add_error("senha2", "Senhas não coincidem.")
        return cleaned_data





