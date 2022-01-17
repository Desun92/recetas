# -*- coding: utf-8 -*-
# from odoo import http


# class Yodamodule(http.Controller):
#     @http.route('/yodamodule/yodamodule/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/yodamodule/yodamodule/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('yodamodule.listing', {
#             'root': '/yodamodule/yodamodule',
#             'objects': http.request.env['yodamodule.yodamodule'].search([]),
#         })

#     @http.route('/yodamodule/yodamodule/objects/<model("yodamodule.yodamodule"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('yodamodule.object', {
#             'object': obj
#         })
