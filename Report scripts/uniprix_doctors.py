
import unicodecsv
from apps.doctors.models import Doctor

with open('locations.csv', 'wb') as csvfile:
    csv_writer = unicodecsv.writer(csvfile, delimiter=',', quotechar='"', quoting=unicodecsv.QUOTE_MINIMAL)
    csv_writer.writerow(('ID', 'Name', 'Specialty', 'Location ID', 'Location Name', 'City', 'Phone Number'))
    locations = Doctor.objects.filter(locations__name='Uniprix')
    for location in locations:
        try:
            phonenumber = location.location.phone_number
        except:
            phonenumber = None
            pass
        csv_writer.writerow((
            location.id,
            location.name,
            location.specialty,
            location.location.id,
            location.location.name,
            location.location.city,
            phonenumber,
        ))
