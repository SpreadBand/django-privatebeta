import csv
import cStringIO as StringIO

from django.contrib import admin
from django.http import HttpResponse
from privatebeta.models import InviteRequest
from privatebeta.utils import proc_queryset
from django.utils.translation import ugettext_lazy as _

class InviteRequestAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ('email', 'created', 'invited',)
    list_filter = ('created', 'invited',)
    
    def make_exported(self, request, queryset):
    
        temp_export = StringIO.StringIO()
        proc_queryset(queryset, temp_export)

        response = HttpResponse(temp_export.getvalue(), mimetype='application/force-download', content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=exportcsv.csv'
        response['Content-Length'] = temp_export.tell()

        return response
    
    make_exported.short_description = _("Export email to CSV Files")
    actions = [make_exported]
    

admin.site.register(InviteRequest, InviteRequestAdmin)
