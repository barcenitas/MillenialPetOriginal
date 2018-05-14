from django import forms
from suit.widgets import SuitDateWidget, SuitTimeWidget, SuitSplitDateTimeWidget
from django.contrib.admin import widgets
from django.forms.widgets import DateTimeInput, SelectDateWidget, SplitDateTimeWidget
class LoginForm(forms.Form):
    username= forms.CharField(label=("Nombre de usuario"), required=True, widget=forms.TextInput(attrs={'size': '40'}))
    password= forms.CharField(widget=forms.PasswordInput,required=True,label=("Password"))

class RegistroForm(forms.Form):
    user=forms.CharField(label="Nombre de usuario", widget=forms.TextInput(attrs={'size': '40'}))
    nombre=forms.CharField(label="Nombre",widget=forms.TextInput(attrs={'size':'100'}))
    email=forms.EmailField(label="Correo electronico")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput())
    password2=forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput())
class FormContra(forms.Form):
    user=forms.CharField(label="Nombre de usuario",widget=forms.TextInput(attrs={'size':'40'}))
    mail=forms.EmailField(label="Correo electronico")
#------------------------------------------ Para agendar las citas
class AgendarForm(forms.Form):
    CHOICES=(('1','Básico'),('2','Intermedio'),('3','Avanzado'))
    #hora_inicio= forms.DateTimeField(widget=widgets.AdminDateWidget())
    #hora_inicio= forms.DateTimeField(widget=)
    num_paquete= forms.ChoiceField(choices=CHOICES)
    #fecha = forms.DateField(widget=SelectDateWidget(empty_label="Nothing"),label="Fecha")
    hora= forms.DateField(widget=SuitTimeWidget(attrs={'placeholder':'Time'}))
    fecha2= forms.DateField(widget=SuitDateWidget)

    #widgets = {
    #        'hora_inicio': SuitSplitDateTimeWidget,
    #        'fecha': SuitSplitDateTimeWidget,
    #}

#--------------------------------------------------------------------------------------------------
