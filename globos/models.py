from django.db import models

# Productos
PROD = {
	('1', 'Globos'),
	('2', 'Arcos'),
	('3', 'Cartel'),
	('4', 'Piñata'),
	('5', 'Centro de mesa'),
	('6', 'Cubiertos'),
	('7', 'Base'),
}

ARCOS = {
	('1', 'Globos'),
	('2', 'Flores'),
	('3', 'Luminarias'),
	('4', 'Tela'),
}
BASE = {
	('1', 'Corazón'),
	('2', 'Cubo'),
	('3', 'Cilindro'),
	('4', 'Cilindro medio'),
}
CUBIERTOS = {
	('1', 'Vasos'),
	('2', 'Platos'),
	('3', 'Servilletas'),
}
CENMESA = {
	('1', 'Adornos'),
	('2', 'Dulces'),
}
MESES = {
	('1', 'Enero'),
	('2', 'Febrero'),
	('3', 'Marzo'),
	('4', 'Abril'),
	('5', 'Mayo'),
	('6', 'Junio'),
	('7', 'Julio'),
	('8', 'Agosto'),
	('9', 'Septiembre'),
	('10', 'Octubre'),
	('11', 'Noviembre'),
	('12', 'Diciembre'),
}

FORMAPINATA = {
	('1', 'Cuadrado'),
	('2', 'Rectangular'),
	('3', 'Redondo'),
	('4', 'Corazón'),
}

FORMAGLOBO = {
	('1', 'Chiquito'),
	('2', 'Mediano'),
	('3', 'Grande'),
	('4', 'Extragrande'),
}
COLORGLOBO = {
	('1', 'Blanco'),
	('2', 'Rojo'),
	('3', 'Verde'),
	('4', 'Amarillo'),
    ('5', 'Azul'),
    ('6', 'Naranja'),
    ('7', 'Rosa'),
    ('8', 'Púrpura'),
    ('9', 'Marrón'),
    ('10', 'Gris'),
    ('11', 'Negro'),
}

TEMATICAS = {
	('1', 'Cumpleaños'),
	('2', 'Boda'),
	('3', 'Revelación de sexo'),
	('4', 'Baby shawers'),
	('5', 'Graduación'),
	('6', 'Aniversario de boda'),
	('7', '14 de febrero'),
	('8', 'Día San Valentín'),
	('9', 'Compromiso'),
	('10', 'Personalizada'),
}
# Create your models here.
class Correos(models.Model):
	idcorreo = models.AutoField(primary_key = True)
	direccion = models.EmailField(max_length = 100, blank = False, null = False)
	password = models.CharField(max_length = 50, null = False)
	activo = models.BooleanField(default = False)
	codigo = models.CharField(max_length = 6, null = True)
	fecharegistro = models.DateField(null = True)

	class Meta:
		verbose_name = 'Correo'
		verbose_name_plural = 'Correos'
		ordering = ['idcorreo']

	def __str__(self):
		return self.direccion

class Pais(models.Model):
	idpais = models.AutoField(primary_key = True)
	descripcion = models.CharField(max_length = 250)
	class Meta:
		verbose_name = 'Pais'
		verbose_name_plural = 'Paises'
		ordering = ['idpais']

	def __str__(self):
		return self.descripcion

class Municipio(models.Model):
	idmunicipio = models.AutoField(primary_key = True)
	descripcion = models.CharField(max_length = 250)
	class Meta:
		verbose_name = 'Municipio'
		verbose_name_plural = 'Municipios'
		ordering = ['idmunicipio']

	def __str__(self):
		return self.descripcion

class Provincia(models.Model):
	idprovincia = models.AutoField(primary_key = True)
	descripcion = models.CharField(max_length = 250)
	class Meta:
		verbose_name = 'Provincia'
		verbose_name_plural = 'Provincias'
		ordering = ['idprovincia']

	def __str__(self):
		return self.descripcion

class Producto(models.Model):
	idproducto = models.AutoField(primary_key = True)
	cantidad = models.IntegerField(null = True)
	precio = models.FloatField(null = True)
	descripcionProd = models.CharField(max_length = 50, choices = PROD)
	class Meta:
		verbose_name = 'Producto'
		verbose_name_plural = 'Productos'
		ordering = ['idproducto']

	def __str__(self):
		return self.descripcionProd

class NArco(models.Model):
	idarco = models.AutoField(primary_key = True)
	descripcion = models.CharField(max_length = 15, choices = ARCOS)
	class Meta:
		verbose_name = 'NArco'
		verbose_name_plural = 'NArcos'
		ordering = ['idarco']
	def __str__(self):
		return self.descripcion

class NBase(models.Model):
	idbase = models.AutoField(primary_key = True)
	descripcion = models.CharField(max_length = 15, choices = BASE)
	class Meta:
		verbose_name = 'NBase'
		verbose_name_plural = 'NBases'
		ordering = ['idbase']
	def __str__(self):
		return self.descripcion

class NCubiertos(models.Model):
	idcubierto = models.AutoField(primary_key = True)
	descripcion = models.CharField(max_length = 15, choices = CUBIERTOS)
	class Meta:
		verbose_name = 'NCubierto'
		verbose_name_plural = 'NCubiertos'
		ordering = ['idcubierto']
	def __str__(self):
		return self.descripcion

class NCentromesa(models.Model):
	idcentromesa = models.AutoField(primary_key = True)
	descripcion = models.CharField(max_length = 15, choices = CENMESA)
	class Meta:
		verbose_name = 'NCentromesa'
		verbose_name_plural = 'NCentromesas'
		ordering = ['idcentromesa']
	def __str__(self):
		return self.descripcion

class Mes(models.Model):
	idmes = models.AutoField(primary_key = True, unique = True)
	descripcion = models.CharField(max_length = 15, null = True, choices = MESES)
	class Meta:
		verbose_name = 'Mes'
		verbose_name_plural = 'Meses'
		ordering = ['idmes']
	def __str__(self):
		return self.descripcion

# class Cartel(models.Model):
# 	idcartel = models.AutoField(primary_key = True, unique = True)
# 	# tamano = models.IntegerField(null = True)
# 	# personalizacion = models.CharField(max_length = 100, null = True)
# 	class Meta:
# 		verbose_name = 'Cartel'
# 		verbose_name_plural = 'Carteles'
# 		ordering = ['idcartel']
# 	def __str__(self):
# 		return self.personalizacion

class NTematica(models.Model):
	idtematica = models.AutoField(primary_key = True, unique = True)
	descripcion = models.CharField(max_length = 100, null = True, choices = TEMATICAS)
	class Meta:
		verbose_name = 'Ntematica'
		verbose_name_plural = 'NTematicas'
		ordering = ['idtematica']
	def __str__(self):
		return self.descripcion

class Globos(models.Model):
	idglobos = models.AutoField(primary_key = True, unique = True)
	formaglobos = models.CharField(max_length = 20, null = True, choices = FORMAGLOBO)
	colorglobos = models.CharField(max_length = 20, null = True, choices = COLORGLOBO)
	# cantidad = models.IntegerField(null = True)
	precio = models.FloatField(null = True)
	class Meta:
		verbose_name = 'Globo'
		verbose_name_plural = 'Globos'
		ordering = ['idglobos']
	# def __str__(self):
	# 	return self.formaglobos

class Pinata(models.Model):
	idpinata = models.AutoField(primary_key = True, unique = True)
	formapinata = models.CharField(max_length = 15, null = True, choices = FORMAPINATA)
	colorpinata = models.CharField(max_length = 15, null = True, choices = COLORGLOBO)
	# tematica = models.CharField(max_length = 100, null = True)
	class Meta:
		verbose_name = 'Pinata'
		verbose_name_plural = 'Pinatas'
		ordering = ['idpinata']
	# def __str__(self):
	# 	return self.tematica


class Persona(models.Model):
	idpersona = models.AutoField(primary_key = True, unique = True)
	ci = models.CharField(max_length = 11, blank = True, null = True, unique = True)
	nombre = models.CharField(max_length = 50, null = True)
	apellido1 = models.CharField(max_length = 50, null = True)
	apellido2 = models.CharField(max_length = 50, null = True)
	direccion = models.CharField(max_length = 150, null = True)
	telefono = models.CharField(max_length = 10, null = True)
	pasaporte = models.CharField(max_length = 10, null = True, blank = True)
	idpais = models.ForeignKey(Pais, on_delete=models.CASCADE, null = True, default=1)
	idprovincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, null = True, default=1)
	idmunicipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, null = True, default=1)
	idcorreos = models.ForeignKey(Correos, on_delete=models.CASCADE, null = True, default=1)
	# idcontrato = models.ForeignKey(Contrato, on_delete=models.CASCADE, null = True)

	class Meta:
		verbose_name = 'Persona'
		verbose_name_plural = 'Personas'
		ordering = ['idpersona']
    
	def __str__(self):
		return self.nombre

class Contrato(models.Model):
	idcontrato = models.AutoField(primary_key = True, unique = True)
	fecha = models.DateField(null = True)
	# diaevento = models.CharField(max_length = 2, null = True)
	# anno = models.CharField(max_length = 4, null = True)
	nombparte1 = models.CharField(max_length = 50, null = True)
	nombparte2 = models.CharField(max_length = 50, null = True)
	dirlugarevento = models.CharField(max_length = 200, null = True)
	precioevento = models.FloatField(null = True)
	# idmes = models.ForeignKey(Mes, on_delete=models.CASCADE, null = True, default=1)
	idtematica = models.ForeignKey(NTematica, on_delete=models.CASCADE, null = True, default=1)
	idpersona = models.ForeignKey(Persona, on_delete=models.CASCADE, null = True, blank = False)
	
	class Meta:
		verbose_name = 'Contrato'
		verbose_name_plural = 'Contratos'
		ordering = ['idcontrato']
	def __str__(self):
		return self.nombparte1

class Evento(models.Model):
	idevento = models.AutoField(primary_key = True, unique = True)
	idcontrato = models.ForeignKey(Contrato, on_delete=models.CASCADE, null = True)
	idglobos = models.ForeignKey(Globos, on_delete=models.CASCADE, null = True)
	# idcartel = models.ForeignKey(Cartel, on_delete=models.CASCADE, null = True)
	idpinata = models.ForeignKey(Pinata, on_delete=models.CASCADE, null = True)
	idbase = models.ForeignKey(NBase, on_delete=models.CASCADE, null = True)
	idcentromesa = models.ForeignKey(NCentromesa, on_delete=models.CASCADE, null = True)
	idcubierto = models.ForeignKey(NCubiertos, on_delete=models.CASCADE, null = True)
	idarco = models.ForeignKey(NArco, on_delete=models.CASCADE, null = True)
	cantidadglobos = models.IntegerField(null = True)
	tamanocartel = models.IntegerField(null = True)
	personalizacioncartel = models.CharField(max_length = 100, null = True)
	tematicapinata = models.CharField(max_length = 100, null = True)
	aprobado = models.BooleanField(default = False)
	# idproducto = models.ForeignKey(Producto, on_delete=models.CASCADE, null = True)
	class Meta:
		verbose_name = 'Evento'
		verbose_name_plural = 'Eventos'
		ordering = ['idevento']
	# def __str__(self):
	# 	return self.idevento

class Combo(models.Model):
	idcombo = models.AutoField(primary_key = True, unique = True)
	idproducto = models.ForeignKey(Producto, on_delete=models.CASCADE, null = True)
	idevento = models.ForeignKey(Evento, on_delete=models.CASCADE, null = True)
	precio = models.FloatField(null = True)
	class Meta:
		verbose_name = 'Combo'
		verbose_name_plural = 'Combos'
		ordering = ['idcombo']
	# def __str__(self):
	# 	return self.idcombo