# -*- coding: utf-8 -*-

from odoo import models, fields, api


class receta(models.Model):
    _name = 'recetas.receta'

    _description = 'Recetas de Cocina'

    name = fields.Char(string="Nombre de receta",required=True)
    autor = fields.Many2one('recetas.autor',string="Nombre del Autor", help="Autor es el creador de la receta…¡NO ES LA PERSONA QUE LA ELABORA!")
    descripcion = fields.Text(string="Descripción de la receta")
    fotografia = fields.Binary(string="Imagen de la receta")
    fechacreacion=fields.Date(string="Fecha de creación de la receta")
    categoria = fields.Many2many('recetas.categoria',string="Categorías de la receta")
    vegana=fields.Boolean(string="Es receta vegana")
    tiempo=fields.Char(string="Tiempo de preparación estimado")
    ingredientes=fields.Html(string="Ingredientes principales")
    
    

class autor(models.Model):
    
    _name = 'recetas.autor'
    
    _description = 'Autores creadores de recetas'
    
    name = fields.Char(string="Identificador del autor",required=True)
    nombre = fields.Char(string="Nombre del autor",required=True)
    apellidos = fields.Char(string="Apellidos del autor",required=True)
    dni = fields.Char(string="DNI del autor",required=True)
    imagen = fields.Binary(string="Imagen del Autor")
    experiencia=fields.Integer(string="Años de experiencia")
    recetascreadas=fields.One2many('recetas.receta','autor',string="Lista de Recetas Creadas")
   

class categoria(models.Model):

    _name = 'recetas.categoria'

    _description = 'Categorias de recetas'

    name = fields.Char(string="Nombre de la categoria",required=True)
    recetas = fields.Many2many('recetas.receta',string="Lista de recetas de la categoría")