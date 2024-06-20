from rest_framework import serializers
from globos.models import *

class CorreosSerializer(serializers.ModelSerializer):
	class Meta:
		model = Correos
		fields = ('idcorreo','direccion','password','activo','codigo','fecharegistro')

class PersonasSerializer(serializers.ModelSerializer):
	class Meta:
		model = Persona
		fields = ('idpersona','ci','nombre','apellido1','apellido2','direccion','telefono','pasaporte','idpais','idmunicipio','idprovincia','idcorreos')

class PaisSerializer(serializers.ModelSerializer):
	class Meta:
		model = Pais
		fields = ('idpais','descripcion')

class MunicipioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Municipio
		fields = ('idmunicipio','descripcion')

class ProvinciaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Provincia
		fields = ('idprovincia','descripcion')

class ProductoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Producto
		fields = ('idproducto','cantidad','precio','descripcionProd')

class ArcoSerializer(serializers.ModelSerializer):
	class Meta:
		model = NArco
		fields = ('idarco','descripcion')

class BaseSerializer(serializers.ModelSerializer):
	class Meta:
		model = NBase
		fields = ('idbase','descripcion')

class CubiertosSerializer(serializers.ModelSerializer):
	class Meta:
		model = NCubiertos
		fields = ('idcubierto','descripcion')

class CentromesaSerializer(serializers.ModelSerializer):
	class Meta:
		model = NCentromesa
		fields = ('idcentromesa','descripcion')

class MesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Mes
		fields = ('idmes','descripcion')

# class CartelSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Cartel
# 		fields = ('idcartel')

class ContratoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Contrato
		fields = ('idcontrato','fecha','nombparte1','nombparte2','dirlugarevento', 'idtematica','idpersona')

class GlobosSerializer(serializers.ModelSerializer):
	# globos = serializers.CharField(choices = FORMAGLOBO, default = 1)
	class Meta:
		model = Globos
		fields = '__all__'
		# fields = ('idglobos','formaglobos','colorglobos')

class PinataSerializer(serializers.ModelSerializer):
	class Meta:
		model = Pinata
		fields = ('idpinata','formapinata','colorpinata')

class EventoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Evento
		fields = ('idevento','idcontrato','idglobos','idpinata','idbase','idcentromesa','idcubierto','idarco','cantidadglobos','tamanocartel','personalizacioncartel','tematicapinata', 'aprobado')

class ComboSerializer(serializers.ModelSerializer):
	class Meta:
		model = Combo
		fields = ('idcombo','idproducto','idevento')

class TematicaSerializer(serializers.ModelSerializer):
	class Meta:
		model = NTematica
		fields = ('idtematica','descripcion')