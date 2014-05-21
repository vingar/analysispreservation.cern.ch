# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2014 CERN.
##
## Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

from wtforms import SelectField
from wtforms.widgets import Select
from invenio.modules.deposit.field_base import WebDepositField
from invenio.modules.deposit.field_widgets import ColumnInput

__all__ = ['CodeTypeField']


def other_processor(form, field, submit=False, fields=None):
    if field.data == 'strip' or field.data == 'fit':
        form.code_type_other.flags.hidden = True
        form.code_type_other.flags.disabled = True
    elif field.data == 'other':
        form.code_type_other.flags.hidden = False
        form.code_type_other.flags.disabled = False


class CodeTypeField(WebDepositField, SelectField):
    def __init__(self, **kwargs):
        defaults = dict(icon='flag',
                        widget_classes="form-control",
                        choices=[('strip', 'To select stripping line'),
                                 ('fit', 'To make fit'),
                                 ('other', 'Other (please specify)')],
                        label="Code Type",
                        default='strip',
                        processors=[other_processor, ]
                        )
        defaults.update(kwargs)
        super(CodeTypeField, self).__init__(**defaults)
