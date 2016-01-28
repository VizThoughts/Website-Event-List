# -*- encoding: utf-8 -*-
#                                                                            #
#   OpenERP Module                                                           #
#   Copyright (C) 2013 Author <email@email.fr>                               #
#                                                                            #
#   This program is free software: you can redistribute it and/or modify     #
#   it under the terms of the GNU Affero General Public License as           #
#   published by the Free Software Foundation, either version 3 of the       #
#   License, or (at your option) any later version.                          #
#                                                                            #
#   This program is distributed in the hope that it will be useful,          #
#   but WITHOUT ANY WARRANTY; without even the implied warranty of           #
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            #
#   GNU Affero General Public License for more details.                      #
#                                                                            #
#   You should have received a copy of the GNU Affero General Public License #
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.    #
#                                                                            #

{
    "name": "Website Event List",
    "version": "1.0",
    "depends": ["website_event_sale","event_sale"],
    "author": "sum1201@163.com",
    "category": "",
    "description": """
    """,
    "data":[
        'views/event_view.xml',
        'views/website_event.xml'
    ],
    "css":[
        'static/src/css/widget_event.css'
    ],
    "init_xml": [],
    'update_xml': [],
    'demo_xml': [],
    'installable': True,
    'active': True,
    #    'certificate': '',
}
