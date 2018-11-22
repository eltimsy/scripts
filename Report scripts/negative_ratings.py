

import unicodecsv
from apps.doctors.models import DoctorRating

with open('doctor.csv', 'wb') as csvfile:
    csv_writer = unicodecsv.writer(csvfile, delimiter=',', quotechar='"', quoting=unicodecsv.QUOTE_MINIMAL)
    csv_writer.writerow(('ID', 'Rating Average', 'Date Created', 'Owner IP', 'Owner UA', 'Comment'))
    ratings = DoctorRating.objects.filter(doctor_id=2116563)
    for rating in ratings:
        if rating.staff:
            score = (rating.staff + rating.punctuality + rating.helpfulness + rating.knowledge)/4
        else:
            score = (rating.punctuality + rating.helpfulness + rating.knowledge)/3
        csv_writer.writerow((
            rating.id,
            score,
            rating.created,
            rating.owner_ip,
            rating.owner_ua,
            rating.comment,
        ))
