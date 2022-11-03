import json
from django import template
import datetime
from inspect import getmembers
from pprint import pprint
register = template.Library()

@register.simple_tag
def vardump(context):
	return json.dumps(context, indent=4)

@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)