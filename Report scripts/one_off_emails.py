

import unicodecsv
import stripe
from apps.doctors.models import Doctor
from apps.accounts.models import User

with open('Marketing_emails.csv', 'wb') as csvfile:
    csv_writer = unicodecsv.writer(csvfile, delimiter=',', quotechar='"', quoting=unicodecsv.QUOTE_MINIMAL)
    stripe_list = list(stripe.Customer.list(limit=100).auto_paging_iter())
    stripe_dic = {}
    for stripe_customer in stripe_list:
        try:
            stripe_dic[stripe_customer.metadata.doctor__owner__id] = stripe_customer
        except AttributeError:
            pass
    csv_writer.writerow(('ID', 'Email', 'Date registered', 'Last Login', 'Existing Customer', 'Specialty', 'Location', 'Country'))
    users = User.objects.exclude(marketing_okay=False).distinct().all()
    for user in users:
        specialty = []
        location = []
        try:
            existing = stripe_dic[str(user.id)].subscriptions.data[0].status
        except (IndexError, KeyError):
            existing = None
        try:
            doctors = Doctor.objects.filter(owner_id=str(user.id))
            country = doctors[0].location.city.province.country
            for doctor in doctors:
                specialty.append(doctor.specialty)
                location.append(doctor.location.city)
        except:
            pass
        csv_writer.writerow((
            user.id,
            user.email,
            user.created,
            user.last_login,
            existing,
            specialty,
            location,
            country,
        ))
