#va a contener mis formularios
from django.forms import ModelForm, TextInput, Textarea
from core.erp.models import Category 
from django.core.exceptions import NON_FIELD_ERRORS

class CategoryForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class']='form-control'
            form.field.widget.attrs['autocomplete']='off'
        #para definir atributos a uno especifico
        self.fields['name'].widget.attrs['autofocus']=True


    class Meta:
        model=Category#el modelo con el q se va trabajar
        fields='__all__'
        #exclude=['']#se puede aplicar cuando aceptan valores nulos
        #los labels por defecto toma el valor de atributo verbose_name, caso que no tenga verbosename se pone los labels
        #si no tiene verbose_name toma los atributos de mi entidd
        '''labels={
            'name':'Nombre:',
            'desc':'Descripcion:'
        }'''
        #widget;permite personalizar mis componentes, sobreescribiendo
        widgets={
            'name':TextInput(
                attrs={
                    #'class':'form-control',
                    'placeholder':'Ingrese un nombre',
                    #'autocomplete':'off'

                }
            ),
            'desc':Textarea(
                attrs={
                    #'class':'form-control',
                    'placeholder':'Ingrese un nombre',
                    #'autocomplete':'off',
                    'rows':3,
                    'cols':3

                }
            )
                
        }
    
    def save(self,commit=True):
        data={}
        form=super()#recupero el objeto del formulario
        try:
            if form.is_valid():
                form.save()
            else:
                data['error']=form.errors
        except Exception as e:
            data['error']=str(e)

        return data
    #usando el formview me permite hacer validaciones adicionales, sobreescribiendo el metodo clean
    def clean(self):#sobreescribiendo metodo para obtener sus componentes y validar, paa sobreescribir los tipos de errores
        cleaned=super().clean()#contiene un diccionario con todos los componentes del formulario
        if len(cleaned['name'])<=50:
            self.add_error('name','Le faltan caracteres')
            #raise form.ValidationError('validacion xxx')#presentar cualquier tipo de errores pero no esta relacionado a componentes
        print(cleaned)
        return cleaned