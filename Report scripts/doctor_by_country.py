import unicodecsv
from apps.doctors.models import Doctor # can't do all doctors too many
with open('doctorcountries.csv', 'wb') as csvfile:
    csv_writer = unicodecsv.writer(csvfile, delimiter=',', quotechar='"', quoting=unicodecsv.QUOTE_MINIMAL)
    csv_writer.writerow(('ID', 'Doctor', 'Country'))
    doctors = Doctor.objects.all().exclude(locations__isnull=True, deleted=True)
    for doctor in doctors:
        csv_writer.writerow((
            str(doctor.id),
            doctor.full_name(),
            str(doctor.location.city.province.country),
        ))
