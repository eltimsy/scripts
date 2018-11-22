

import unicodecsv
from apps.doctors.models import Doctor

with open('doctors.csv', 'wb') as csvfile:
    csv_writer = unicodecsv.writer(csvfile, delimiter=',', quotechar='"', quoting=unicodecsv.QUOTE_MINIMAL)
    doctor_list = Doctor.objects.filter(locations__city=25, specialty=2)
    csv_writer.writerow(('ID', 'Name'))
    for doctor in doctor_list:
        try:
            doctor
            csv_writer.writerow((
                doctor.id,
                '\''+doctor.name+'\',',
            ))
        except AttributeError:
            pass
