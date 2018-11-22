import unicodecsv
from apps.doctors.models import Doctor# can't do all doctors too many
def datetime_to_datestring(dt):
    return dt.strftime('%Y-%m-%d %H:%M:%S')
with open('unclaimeddoctors1.csv', 'wb') as csvfile:
    csv_writer = unicodecsv.writer(csvfile, delimiter=',', quotechar='"', quoting=unicodecsv.QUOTE_MINIMAL)
    csv_writer.writerow(('ID', 'Doctor', 'City', 'State', 'Address', 'Phone Number', 'URL', 'Score', '# of Reviews', 'Created'))
    doctors = Doctor.objects.filter(owner=None, specialty__id__in=[2, 3, 5, 6, 11], locations__city__province__country=4)
    for doctor in doctors:
        if doctor.rating['count'] > 9:
            try:
                city = str(doctor.location.city.name)
                state = str(doctor.location.city.province)
            except:
                city = None
                state = None
            try:
                address = str(doctor.location.address)
            except:
                address = None
            try:
                phone = str(doctor.location.phone_number)
            except:
                phone = None
            csv_writer.writerow((
                str(doctor.id),
                doctor.full_name(),
                city,
                state,
                address,
                phone,
                "https://ratemds.com/doctor-ratings/{}".format(doctor.slug),
                doctor.rating['average'],
                doctor.rating['count'],
                datetime_to_datestring(doctor.created),
            ))
