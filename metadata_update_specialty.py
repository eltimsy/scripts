import stripe
from apps.doctors.models import Doctor
from apps.sales.models import Sales

stripe_list = list(stripe.Customer.list(limit=100).auto_paging_iter())

for customer in stripe_list:
    try:
        doctor = Doctor.objects.get(customer_id=customer.id)
        try:
            sales_tagged = Sales.objects.get(doctor_id=doctor.id)
            customer.metadata = {
                'doctor__sales_object__modified': sales_tagged.modified,
                'doctor__sales_object__owner__id': sales_tagged.owner_id,
                'doctor__full_name': doctor.full_name(),
                'doctor__id': doctor.id,
                'doctor__owner__id': doctor.owner_id,
                'doctor__specialty': doctor.specialty
                }
            customer.save()
        except Sales.DoesNotExist:
            customer.metadata = {
                'doctor__full_name': doctor.full_name(),
                'doctor__id': doctor.id,
                'doctor__owner__id': doctor.owner_id,
                'doctor__specialty': doctor.specialty
                }
            customer.save()
    except Doctor.DoesNotExist:
        pass
