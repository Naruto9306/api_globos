from django import forms
from .models import *

class CorreosForm(forms.ModelForm):
	class Meta:
		model = Correos
		fields = ['idcorreo','direccion','password','codigo']
		labels = {
		    'direccion': 'Correo electrónico',
		    'password': 'Contraseña',
		    'activo': 'Activo',
		    'codigo': 'Código'
		    }
		widgets = {
		   'direccion': forms.TextInput(
               attrs = {
                  'class': 'form-control',
                  'placeholder': 'Correo electrónico',
                  'id': 'correo',
               }
		   	),
		   'password': forms.TextInput(
               attrs = {
                  'class': 'form-control',
                  'placeholder': 'Contraseña',
                  'id': 'password',
               }
		   	),
         'codigo': forms.TextInput(
               attrs = {
                  'class': 'form-control',
                  'placeholder': 'Código',
                  'id': 'codigo',
               }
		   	),
		   	'activo': forms.TextInput(
               attrs = {
                  'class': 'form-control',
                  'placeholder': 'Activo',
                  'id': 'activo',
               }
		   	)      
		   }


class PaisForm(forms.ModelForm):
	class Meta:
		model = Pais
		fields = ['idpais','descripcion']
		labels = {
		    'descripcion': 'Descripcion',
		    }

class MunicipioForm(forms.ModelForm):
	class Meta:
		model = Municipio
		fields = ['idmunicipio','descripcion']
		labels = {
		    'descripcion': 'Descripcion',
		    }

class ProvinciaForm(forms.ModelForm):
	class Meta:
		model = Provincia
		fields = ['idprovincia','descripcion']
		labels = {
		    'descripcion': 'Descripcion',
		    }

class PersonaForm(forms.ModelForm):
	class Meta:
		model = Pais
		fields = ['idpersona','ci','nombre','apellido1','apellido2','telefono']
		labels = {
		    'ci': 'Carne de identidad',
		    'nombre': 'Nombre completo',
		    'apellido1': 'Primer apellido',
		    'apellido2': 'Segundo apellido',
		    'direccion': 'Direccion',
		    'telefono': 'Telefono',
		    'pasaporte': 'Pasaporte',
		    }

class ProductoForm(forms.ModelForm):
	class Meta:
		model = Producto
		fields = ['idproducto', 'cantidad', 'precio', 'descripcionProd']
		labels = {
		    'cantidad': 'Cantidad de productos',
		    'precio': 'Precio del producto',
		    'descripcionProd': 'Descripcion del producto',
		    }


class ArcoFrom(forms.ModelForm):
	class Meta:
		model = NArco
		fields = ['idarco','descripcion']
		labels = {
		    'descripcion': 'Descripcion del arco',
		    }

class BaseFrom(forms.ModelForm):
	class Meta:
		model = NBase
		fields = ['idbase','descripcion']
		labels = {
		    'descripcion': 'Descripcion de la base',
		    }

class CubiertoFrom(forms.ModelForm):
	class Meta:
		model = NCubiertos
		fields = ['idcubierto','descripcion']
		labels = {
		    'descripcion': 'Descripcion del cubierto',
		    }

class CentromesaFrom(forms.ModelForm):
	class Meta:
		model = NCentromesa
		fields = ['idcentromesa','descripcion']
		labels = {
		    'descripcion': 'Descripcion del centro de mesa',
		    }
