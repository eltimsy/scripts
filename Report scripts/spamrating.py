import unicodecsv
from apps.doctors.models import DoctorRating

with open('genital_check.csv', 'wb') as csvfile:
    csv_writer = unicodecsv.writer(csvfile, delimiter=',', quotechar='"', quoting=unicodecsv.QUOTE_MINIMAL)
    csv_writer.writerow(('ID', 'Doctor ID', 'Comment', 'Created','Owner IP'))
    doctors = DoctorRating.objects.filter(comment__contains='Genital', created__gte='2018-07-01')
    for doctor in doctors:
        csv_writer.writerow((
            str(doctor.id),
            doctor.doctor_id,
            doctor.comment,
            doctor.created,
            doctor.owner_ip,
        ))
    doctors = DoctorRating.objects.filter(comment__contains='GENITAL', created__gte='2018-07-01')
    for doctor in doctors:
        csv_writer.writerow((
            str(doctor.id),
            doctor.doctor_id,
            doctor.comment,
            doctor.created,
            doctor.owner_ip,
        ))
    doctors = DoctorRating.objects.filter(comment__contains='Genitals', created__gte='2018-07-01')
    for doctor in doctors:
        csv_writer.writerow((
            str(doctor.id),
            doctor.doctor_id,
            doctor.comment,
            doctor.created,
            doctor.owner_ip,
        ))
    doctors = DoctorRating.objects.filter(comment__contains='GENITALS', created__gte='2018-07-01')
    for doctor in doctors:
        csv_writer.writerow((
            str(doctor.id),
            doctor.doctor_id,
            doctor.comment,
            doctor.created,
            doctor.owner_ip,
        ))
    doctors = DoctorRating.objects.filter(comment__contains='Genitalia', created__gte='2018-07-01')
    for doctor in doctors:
        csv_writer.writerow((
            str(doctor.id),
            doctor.doctor_id,
            doctor.comment,
            doctor.created,
            doctor.owner_ip,
        ))
    doctors = DoctorRating.objects.filter(comment__contains='GENITALIA', created__gte='2018-07-01')
    for doctor in doctors:
        csv_writer.writerow((
            str(doctor.id),
            doctor.doctor_id,
            doctor.comment,
            doctor.created,
            doctor.owner_ip,
        ))