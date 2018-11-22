import unicodecsv
from apps.doctors.models import Doctor
from apps.accounts.models import User
with open('claimeddoctor.csv', 'wb') as csvfile:
    csv_writer = unicodecsv.writer(csvfile, delimiter=',', quotechar='"', quoting=unicodecsv.QUOTE_MINIMAL)
    csv_writer.writerow(('ID', 'Doctor', 'Specialty', 'City', 'Province', 'Country', 'Phone', 'Email',
                 'Rating', 'Verified On', 'URL', 'Tagged', 'Customer ID', 'Stripe Customer ID', 'Profile Ads', 'Marketing OK'))
    doctors = Doctor.objects.filter(owner__isnull=False).distinct().all()
    for doctor in doctors:
        if doctor.location is None:
            continue
        try:
            accepted_on = (doctor.doctor_verification_request.first().accepted_on) \
                           .strftime('%Y-%m-%d %H:%M:%S')
        except (KeyError, AttributeError):
            accepted_on = None
        csv_writer.writerow((
            str(doctor.id),
            doctor.full_name(),
            str(doctor.specialty),
            str(doctor.location.city),
            str(doctor.location.city.province),
            str(doctor.location.city.province.country),
            doctor.location.phone_number,
            str(doctor.owner.email),
            str(doctor.rating['average']),
            str(accepted_on),
            "https://ratemds.com/doctor-ratings/{}".format(doctor.slug),
            True if hasattr(doctor, 'sales_doctor') else False,
            str(doctor.owner.id),
            doctor.customer_id,
            doctor.profile_ads,
            doctor.owner.marketing_okay,
        ))