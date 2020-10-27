# -*- coding: utf-8 -*-
# from odoo import http


# class Message(http.Controller):
#     @http.route('/message/message/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/message/message/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('message.listing', {
#             'root': '/message/message',
#             'objects': http.request.env['message.message'].search([]),
#         })

#     @http.route('/message/message/objects/<model("message.message"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('message.object', {
#             'object': obj
#         })
