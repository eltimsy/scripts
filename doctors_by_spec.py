from apps.doctors.models import Doctor
from apps.specialties.models import Specialty

specialty = Specialty.objects.filter()
for spec in specialty:
    doctors = Doctor.objects.filter(specialty_id=spec.id)
    print spec.name + ' number of doctors: ' + str(doctors.count())