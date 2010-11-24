import csv

from django.core.management.base import BaseCommand, CommandError

from privatebeta.models import InviteRequest

class Command(BaseCommand):
	args = '<file_name>'
	help = 'Export invitations to CSV files'

	def handle(self, *args, **options):
		try:
			file_name = args[0]
		except IndexError, e:
			raise CommandError("You must provide a file name to export to.")

		csvWriter = csv.writer(open(file_name, 'w'), delimiter=';')

		invites = InviteRequest.objects.all()
		for invite in invites:
        		info = (invite.email, invite.created, invite.invited)
        		csvWriter.writerow(info)

