from django import forms
from .models import Contact  # modelos estão em website/models.py

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['nome', 'empresa', 'email', 'mensagem']
        widgets = {
            'nome': forms.TextInput(attrs={
                'placeholder': 'Seu nome',
                'class': 'form-input',
                'required': True
            }),
            'empresa': forms.TextInput(attrs={
                'placeholder': 'Empresa (opcional)',
                'class': 'form-input',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'seu@exemplo.com',
                'class': 'form-input',
                'required': True
            }),
            'mensagem': forms.Textarea(attrs={
                'placeholder': 'Escreva sua mensagem...',
                'class': 'form-textarea',
                'rows': 5
            }),
        }
