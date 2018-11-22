
import unicodecsv
from apps.doctors.models import DoctorAppointment

with open('doctor_appointments.csv', 'wb') as csvfile:
    csv_writer = unicodecsv.writer(csvfile, delimiter=',', quotechar='"', quoting=unicodecsv.QUOTE_MINIMAL)
    csv_writer.writerow(('Customer ID', 'Doctor', 'Doctor ID', 'Country', 'Specialty', 'Name', 'Description', 'Time', 'Profile Ads'))
    appointments = DoctorAppointment.objects.all()
    for appointment in appointments:
        csv_writer.writerow((
            appointment.doctor.customer_id,
            appointment.doctor.name,
            appointment.doctor.id,
            appointment.doctor.location.city.province.country,
            appointment.doctor.specialty,
            appointment.name,
            appointment.description,
            appointment.created,
            appointment.doctor.profile_ads,
        ))
