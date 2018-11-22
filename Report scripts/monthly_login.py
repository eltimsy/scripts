

import unicodecsv
from apps.doctors.models import Doctor
from apps.accounts.models import User

with open('last_login_report.csv', 'wb') as csvfile:
    csv_writer = unicodecsv.writer(csvfile, delimiter=',', quotechar='"', quoting=unicodecsv.QUOTE_MINIMAL)
    doctor_list = Doctor.objects.filter(customer_id__isnull=False)
    csv_writer.writerow(('Customer ID', 'Name', 'Email', 'Email Verified', 'City', 'Specialty', 'Created', 'Last Login'))
    for doctor in doctor_list:
        try:
            owner = User.objects.get(id=doctor.owner_id)
            csv_writer.writerow((
                doctor.customer_id,
                doctor.name,
                owner.email,
                owner.email_verified,
                doctor.location.city,
                doctor.specialty,
                doctor.created,
                owner.last_login,
            ))
        except:
            pass
