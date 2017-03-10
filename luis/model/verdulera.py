# -*- coding: utf-8 -*-

from openerp import models, fields, api

class verdulera(models.Model):
	_name = 'verdulera.luis'

	nombre_fruta = fields.Char('Nombre de la Fruta')
	precio = fields.Integer('Precio de la Fruta')
	descripcion = fields.Char('tipo de fruta')
	cantidad = fields.Integer('cantidasd de fruta')
