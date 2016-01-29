# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.exceptions import except_orm, Warning, RedirectWarning
import openerp.addons.decimal_precision as dp
import datetime

import logging
_logger = logging.getLogger(__name__)

class event_event(models.Model):
    _inherit = 'event.event'

    @api.one
    @api.depends('date_begin','date_end')
    def _cal_days(self):
        result=[]
        _logger.info("cal.......")
        _logger.info("date_begin:"+ str(self.date_begin))
        date_begin=datetime.datetime.strptime(self.date_begin,'%Y-%m-%d %H:%M:%S')
        date_end=datetime.datetime.strptime(self.date_end,'%Y-%m-%d %H:%M:%S')
        _logger.info("result:"+str((date_end-date_begin).seconds))
        days=(date_end-date_begin).days
        hour=(date_end-date_begin).seconds/3600
        if days>0:
            self.duration_day=str(days)+"Days"
        else:
            self.duration_day=str(hour)+'Hours'

    @api.one
    @api.depends('event_ticket_ids')
    def _cal_price(self):
        vals=[]
        _logger.info("***************")
        if self.event_ticket_ids:
            for l in self.event_ticket_ids:
                vals.append(l.price)


        if len(vals)>0:
            self.price= vals[vals.index(min(vals))]
        else:
            self.price= 0

    duration_day=fields.Char(compute='_cal_days',string=u'天数')
    price =fields.Float(compute='_cal_price',string="价格")



