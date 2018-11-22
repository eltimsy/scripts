

import unicodecsv
from apps.doctors.models import Doctor

with open('last_login_report.csv', 'wb') as csvfile:
    csv_writer = unicodecsv.writer(csvfile, delimiter=',', quotechar='"', quoting=unicodecsv.QUOTE_MINIMAL)
    doctor_list = Doctor.objects.filter(customer_id__isnull=False, appointments_enabled=True, appointments_available=True)
    csv_writer.writerow(('Customer ID', 'Name', 'City', 'Specialty', 'Created'))
    for doctor in doctor_list:
        try:
            city = doctor.location.city
        except AttributeError:
            city = None
        csv_writer.writerow((
            doctor.customer_id,
            doctor.name,
            city,
            doctor.specialty,
            doctor.created,
        ))

