from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from bootcamp.settings import ALLOWED_SIGNUP_DOMAINS

def Validardominio(value):
    if '*' not in ALLOWED_SIGNUP_DOMAINS:
        try:
            dominio = value[value.index("@"):]
            if dominio not in ALLOWED_SIGNUP_DOMAINS:
                raise ValidationError(u'Dominio no valido, esta aplicacion actualmente es solo para direcciones de correo especificas {0}'.format(','.join(ALLOWED_SIGNUP_DOMAINS)))
        except Exception, e:
            raise ValidationError(u'Dominio no valido {0}'.format(','.join(ALLOWED_SIGNUP_DOMAINS)))

def Palabras_reservadas(value):
    listado = ['admin', 'settings', 'news', 'about', 'help', 'signin', 'signup', 
        'signout', 'terms', 'privacy', 'cookie', 'new', 'login', 'logout', 'administrator', 
        'join', 'account', 'username', 'root', 'blog', 'user', 'users', 'billing', 'subscribe',
        'reviews', 'review', 'blog', 'blogs', 'edit', 'mail', 'email', 'home', 'job', 'jobs', 
        'contribute', 'newsletter', 'shop', 'profile', 'register', 'auth', 'authentication',
        'campaign', 'config', 'delete', 'remove', 'forum', 'forums', 'download', 'downloads', 
        'contact', 'blogs', 'feed', 'feeds', 'faq', 'intranet', 'log', 'registration', 'search', 
        'explore', 'rss', 'support', 'status', 'static', 'media', 'setting', 'css', 'js',
        'follow', 'activity', 'questions', 'articles', 'network',]
    if value.lower() in listado:
        raise ValidationError('Esta es una palabra Reservada')

def Usuario_no_valido(value):
    if '@' in value or '+' in value or '-' in value:
        raise ValidationError('Introduce un nombre de usuario valido')

def Registro_unico_correo(value):
    if User.objects.filter(email__iexact=value).exists():
        raise ValidationError('Esta direccion ya se encuentra registrada')

def Registro_unico_usuario(value):
    if User.objects.filter(username__iexact=value).exists():
        raise ValidationError('Ya existe un usuario con este nombre')

class SignUpForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),
        max_length=30,
        required=True,
        help_text='El nombre de usuario puede contener <strong>Alfanumericos</strong>, <strong>_</strong> y  <strong>.</strong> caracteres')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), 
        label="Confirm your password",
        required=True)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}), 
        required=True,
        max_length=75)

    class Meta:
        model = User
        exclude = ['last_login', 'date_joined']
        fields = ['username', 'email', 'password', 'confirm_password',]

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].validators.append(Palabras_reservadas)
        self.fields['username'].validators.append(Usuario_no_valido)
        self.fields['username'].validators.append(Registro_unico_usuario)
        self.fields['email'].validators.append(Registro_unico_correo)
        self.fields['email'].validators.append(Validardominio)

    def clean(self):
        super(SignUpForm, self).clean()
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and password != confirm_password:
            self._errors['password'] = self.error_class(['Passwords no coinciden'])
        return self.cleaned_data