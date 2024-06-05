# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Task(models.Model):
    _name = 'task'
    _description = 'Task'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')

class Room(models.Model):
    _name = 'room'
    _description = 'Room'

    name = fields.Char(string='Name')
    room_count = fields.Integer(string='Room Count')
    room_type = fields.Char(string='Room Type')

class RoomCategory(models.Model):
    _name = 'category'
    _description = 'Category'

    name = fields.Char(string='Name')
    is_open = fields.Boolean(string='Is Open', default=True)
    photo = fields.Binary(string='Photo')
    short_name = fields.Char(string="Short name")
    room_type = fields.Char(string='Room Type')