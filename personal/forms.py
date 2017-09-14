from django import forms

from .models import Persona

class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona
        fields = ('nombre', 'ap_paterno','ap_materno','edad',)



    def clean(self):
        
        cleaned_data = self.cleaned_data
        edad =cleaned_data.get("edad",None)
        print edad
        if edad >0:
            edad = int(edad) 
            raise forms.ValidationError("You have forgotten about Fred!")

            