

import unicodecsv
from apps.doctors.models import Doctor
from apps.accounts.models import User

with open('pain_doctors_report.csv', 'wb') as csvfile:
    csv_writer = unicodecsv.writer(csvfile, delimiter=',', quotechar='"', quoting=unicodecsv.QUOTE_MINIMAL)
    doctor_list = Doctor.objects.filter(specialty_id=28)
    csv_writer.writerow(('ID', 'Name', 'Email'))
    for doctor in doctor_list:
        try:
            owner = User.objects.get(id=doctor.owner_id)
            email = owner.email
        except:
            email = None
            pass
        csv_writer.writerow((
            doctor.id,
            doctor.name,
            email,
        ))
