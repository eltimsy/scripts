import unicodecsv
from apps.doctors.models import Doctor
from apps.locations.models import Country
from apps.specialties.models import Specialty
with open('doctorcountryspecialty.csv', 'wb') as csvfile:
    csv_writer = unicodecsv.writer(csvfile, delimiter=',', quotechar='"', quoting=unicodecsv.QUOTE_MINIMAL)
    csv_writer.writerow(('Specialty', 'Country', 'Count'))
    specialties = Specialty.objects.all()
    countries = Country.objects.all()
    for specialty in specialties:
        for country in countries:
            doctors = Doctor.objects.filter(specialty_id=specialty.id, locations__city__province__country_id=country.id).count()
            csv_writer.writerow((
                specialty.name,
                country.name,
                str(doctors),
            ))