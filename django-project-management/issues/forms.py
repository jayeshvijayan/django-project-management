from django.forms import *
from django.contrib.admin import widgets                                       
from projects.models import *
from issues.models import *
#from misc.widgets import DateTimeWidget
#from backends.authlib import *


class IssueForm(ModelForm):
	class Meta:
		model = Issue
	def __init__(self, *args, **kwargs):
		super(IssueForm, self).__init__(*args, **kwargs)
		self.fields['author'].widget = HiddenInput()