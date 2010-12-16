import csv

def proc_queryset(queryset, empty_file):
        
    temp_queryset = csv.writer((empty_file), delimiter=';')
        
    for invite in queryset:
        info = (invite.email, invite.created, invite.invited)
        temp_queryset.writerow(info)