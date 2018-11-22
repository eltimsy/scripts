

import unicodecsv
from apps.doctors.models import Doctor

with open('website_purge.csv', 'wb') as csvfile:
    csv_writer = unicodecsv.writer(csvfile, delimiter=',', quotechar='"', quoting=unicodecsv.QUOTE_MINIMAL)
    doctor_list = Doctor.objects.filter(locations__website__contains='http://www.mciindia.org/')
    csv_writer.writerow(('ID', 'Name', 'Owner', 'Verified', 'Location', 'City', 'Country', 'modified'))
    for doctor in doctor_list:
        try:
            doctor
            csv_writer.writerow((
                doctor.id,
                doctor.name,
                doctor.owner,
                doctor.verified,
                doctor.location.name,
                doctor.location.city.name,
                doctor.location.city.province.country.name,
                doctor.modified,
            ))
        except AttributeError:
            pass
