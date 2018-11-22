from apps.doctors.models import Doctor, DoctorRating

doctors = Doctor.objects.filter(customer_id__isnull=False, ads_enabled=False).exclude(customer_id__exact='')

for doctor in doctors:
    ratings = DoctorRating.objects.filter(doctor_id=doctor.id)
    for rating in ratings:
        if rating.featured:
            print doctor.id