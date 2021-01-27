#!/usr/bin/python3
"""Init of module views"""
from flask import Blueprint


app_views = Blueprint(
    'app_views', __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/api/v1'
)

from api.v1.views.index import *