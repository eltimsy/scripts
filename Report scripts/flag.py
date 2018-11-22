

import unicodecsv
from apps.flags.models import Flag

with open('flags.csv', 'wb') as csvfile:
    csv_writer = unicodecsv.writer(csvfile, delimiter=',', quotechar='"', quoting=unicodecsv.QUOTE_MINIMAL)
    flag_list = Flag.objects.filter(resolved=False)
    csv_writer.writerow(('ID', 'Reason', 'Owner', 'Owner IP', 'Owner UA', 'Created', 'Rating ID', 'Doctor'))
    for flag in flag_list:
        try:
            flagid = flag.id
            csv_writer.writerow((
                flagid,
                flag.reason,
                flag.owner,
                flag.owner_ip,
                flag.owner_ua,
                flag.created,
                flag.rating.id,
                flag.rating.doctor,
            ))
        except:
            pass
