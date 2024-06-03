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

