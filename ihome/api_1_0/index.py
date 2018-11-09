# coding:utf-8
from ihome.api_1_0 import api
from ihome import db, models
import logging
from flask import current_app


@api.route('/index')
def index():
    current_app.logger.error("error msg")
    current_app.logger.warn("warn msg")
    current_app.logger.info("info msg")
    current_app.logger.debug("debug msg")
    return 'index page'
