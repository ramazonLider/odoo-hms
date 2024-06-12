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
    
    name = fields.Char(string='Name')
    user_id = fields.Many2one('res.users', string='User')
    cart_id = fields.Many2one('cart', string='Cart')
    total_amount = fields.Float(string='Total Amount')
    payment_status = fields.Selection([
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('cancelled', 'Cancelled')
    ], string='Payment Status', default='pending')

    @api.model
    def create(self, vals):
        _logger.info('Booking created: %s', vals)
        return super(Booking, self).create(vals)

    def confirm_payment(self):
        self.payment_status = 'paid'
        _logger.info('Payment confirmed for Booking: %s', self.name)

    def cancel_payment(self):
        self.payment_status = 'cancelled'
        _logger.info('Payment cancelled for Booking: %s', self.name)


class Cart(models.Model):
    _name = 'cart'
    _description = 'Cart'

    name = fields.Char(string='Name')
    user_id = fields.Many2one('res.users', string='User')
    room_ids = fields.Many2many('room', string='Rooms')

    @api.model
    def create(self, vals):
        _logger.info('Cart created: %s', vals)
        return super(Cart, self).create(vals)

    def add_room(self, room_id):
        room = self.env['room'].browse(room_id)
        self.room_ids = [(4, room.id)]
        _logger.info('Room added to cart: %s', room.name)

    def remove_room(self, room_id):
        room = self.env['room'].browse(room_id)
        self.room_ids = [(3, room.id)]
        _logger.info('Room removed from cart: %s', room.name)