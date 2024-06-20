from django.shortcuts import render
from rest_framework import generics, filters, status, viewsets
from globos.models import *
from globos.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail

# Create your views here.
#APIs
#Correos
class CorreoLista(generics.ListCreateAPIView):
	queryset = Correos.objects.all()
	serializer_class = CorreosSerializer
	filter_backend = [filters.SearchFilter]
	search_fields = ['direccion']

class CorreoDetalles(generics.RetrieveUpdateDestroyAPIView):
	queryset = Correos.objects.all()
	serializer_class = CorreosSerializer

#Personas
class PersonasLista(generics.ListCreateAPIView):
	queryset = Persona.objects.all()
	serializer_class = PersonasSerializer

class PersonasDetalles(generics.RetrieveUpdateDestroyAPIView):
	queryset = Persona.objects.all()
	serializer_class = PersonasSerializer

#Pais
class PaisLista(generics.ListCreateAPIView):
	queryset = Pais.objects.all()
	serializer_class = PaisSerializer

class PaisDetalles(generics.RetrieveUpdateDestroyAPIView):
	queryset = Pais.objects.all()
	serializer_class = PaisSerializer

#Provincia
class ProvinciaLista(generics.ListCreateAPIView):
	queryset = Provincia.objects.all()
	serializer_class = ProvinciaSerializer

class ProvinciaDetalles(generics.RetrieveUpdateDestroyAPIView):
	queryset = Provincia.objects.all()
	serializer_class = ProvinciaSerializer

#Municipio
class MunicipioLista(generics.ListCreateAPIView):
	queryset = Municipio.objects.all()
	serializer_class = MunicipioSerializer

class MunicipioDetalles(generics.RetrieveUpdateDestroyAPIView):
	queryset = Municipio.objects.all()
	serializer_class = MunicipioSerializer

#Productos
class ProductoLista(generics.ListCreateAPIView):
	queryset = Producto.objects.all()
	serializer_class = ProductoSerializer

class ProductoDetalles(generics.RetrieveUpdateDestroyAPIView):
	queryset = Producto.objects.all()
	serializer_class = ProductoSerializer

#Arco
class ArcoLista(generics.ListCreateAPIView):
	queryset = NArco.objects.all()
	serializer_class = ArcoSerializer

class ArcoDetalles(generics.RetrieveUpdateDestroyAPIView):
	queryset = NArco.objects.all()
	serializer_class = ArcoSerializer

#base
class BaseLista(generics.ListCreateAPIView):
	queryset = NBase.objects.all()
	serializer_class = BaseSerializer

class BaseDetalles(generics.RetrieveUpdateDestroyAPIView):
	queryset = NBase.objects.all()
	serializer_class = BaseSerializer

#cubiertos
class CubiertosLista(generics.ListCreateAPIView):
	queryset = NCubiertos.objects.all()
	serializer_class = CubiertosSerializer

class CubiertosDetalles(generics.RetrieveUpdateDestroyAPIView):
	queryset = NCubiertos.objects.all()
	serializer_class = CubiertosSerializer

#centro de mesa
class CentromesaLista(generics.ListCreateAPIView):
	queryset = NCentromesa.objects.all()
	serializer_class = CentromesaSerializer

class CentromesaDetalles(generics.RetrieveUpdateDestroyAPIView):
	queryset = NCentromesa.objects.all()
	serializer_class = CentromesaSerializer

#mes
class MesLista(generics.ListCreateAPIView):
	queryset = Mes.objects.all()
	serializer_class = MesSerializer

class MesDetalles(generics.RetrieveUpdateDestroyAPIView):
	queryset = Mes.objects.all()
	serializer_class = MesSerializer

#cartel
# class CartelLista(generics.ListCreateAPIView):
# 	queryset = Cartel.objects.all()
# 	serializer_class = CartelSerializer

# class CartelDetalles(generics.RetrieveUpdateDestroyAPIView):
# 	queryset = Cartel.objects.all()
# 	serializer_class = CartelSerializer

#contrato
class ContratoLista(generics.ListCreateAPIView):
	queryset = Contrato.objects.all()
	serializer_class = ContratoSerializer

class ContratoDetalles(generics.RetrieveUpdateDestroyAPIView):
	queryset = Contrato.objects.all()
	serializer_class = ContratoSerializer

#globos
class GlobosLista(generics.ListCreateAPIView):
	queryset = Globos.objects.all()
	serializer_class = GlobosSerializer

class GlobosDetalles(generics.RetrieveUpdateDestroyAPIView):
	queryset = Globos.objects.all()
	serializer_class = GlobosSerializer

#pinata
class PinataLista(generics.ListCreateAPIView):
	queryset = Pinata.objects.all()
	serializer_class = PinataSerializer

class PinataDetalles(generics.RetrieveUpdateDestroyAPIView):
	queryset = Pinata.objects.all()
	serializer_class = PinataSerializer

#evento
class EventoLista(generics.ListCreateAPIView):
	queryset = Evento.objects.all()
	serializer_class = EventoSerializer

class EventoDetalles(generics.RetrieveUpdateDestroyAPIView):
	queryset = Evento.objects.all()
	serializer_class = EventoSerializer

#combo
class ComboLista(generics.ListCreateAPIView):
	queryset = Combo.objects.all()
	serializer_class = ComboSerializer

class ComboDetalles(generics.RetrieveUpdateDestroyAPIView):
	queryset = Combo.objects.all()
	serializer_class = ComboSerializer

#Tematicas
class TematicaLista(generics.ListCreateAPIView):
	queryset = NTematica.objects.all()
	serializer_class = TematicaSerializer

class TematicaDetalles(generics.RetrieveUpdateDestroyAPIView):
	queryset = NTematica.objects.all()
	serializer_class = TematicaSerializer

class EmailApiView(APIView):
	def post(self, request):
		try:
			to_email = "pedro.moran93@yahoo.com"
			subject = "Probando"
			message = request.data.get('mensaje')
			send_mail(subject, message, None, [to_email])
			return Response({'message': "Correo enviado desde DRF."}, status=status.HTTP_200_OK)
		except Exception as e:
			error_message = str(e)
			return Response({'message': error_message}, status=status.HTTP_400_BAD_REQUEST)

