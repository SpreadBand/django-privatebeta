import csv

from django.core.management.base import BaseCommand, CommandError
from django.db import models
from django.utils.translation import ugettext_lazy as _

from privatebeta.models import InviteRequest
from privatebeta.utils import proc_queryset


class Command(BaseCommand, models.Model):
	args = _('<file_name>')
	help = _('Export invitations to CSV files')

	def handle(self, *args, **options):
		try:
			file_name = args[0]
		except IndexError, e:
			raise CommandError(_("You must provide a file name to export to."))

		csvexport = open(file_name, 'w')
		queryset = InviteRequest.objects.all()
		proc_queryset(queryset, csvexport)

