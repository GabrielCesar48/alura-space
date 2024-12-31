
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
     nome_cadastro = forms.CharField(
         label="Nome Completo",
         widget=forms.TextInput(attrs={
             "autofocus": True,
             "class": "form-control",
             "placeholder": "Ex.: João Silva",
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





