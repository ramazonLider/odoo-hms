from odoo import models, fields, api 
import logging
_logger = logging.getLogger(__name__)



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
    main_places = fields.Integer(string="Main places count")
    is_open = fields.Boolean(string='Is Open', default=True)
    photo_count = fields.Integer(string='Photo')
    short_name = fields.Char(string="Short name")

class Booking(models.Model):
    _name = "booking"
    _description = 'Booking'

    name = fields.Char(string="name")
    address = fields.Char(string="address")
    user = fields.Char(string="username")
    pin_code = fields.Integer(string="Your pin code")
    surname = fields.Char(string="Your surname")

    def button_action_method(self):
        _logger.info("Button clicked!")
        return True
