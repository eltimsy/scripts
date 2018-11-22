
import unicodecsv
from apps.locations.models import Location

with open('arizona_locations.csv', 'wb') as csvfile:
    csv_writer = unicodecsv.writer(csvfile, delimiter=',', quotechar='"', quoting=unicodecsv.QUOTE_MINIMAL)
    csv_writer.writerow(('ID', 'Slug', 'Name', 'Address', 'Suite', 'City', 'Postal Code', 'Phone Number', 'Website', 'Category', 'Created', 'Latitude', 'Longitude', 'Owner ID'))
    locations = Location.objects.filter(city__province=12, deleted=False)
    for location in locations:
        try:
            address = location.address
        except:
            address = None
        try:
            suite = location.suite
        except:
            suite = None
        try:
            postal = location.postal_code
        except:
            postal = None
        try:
            phonenumber = location.phone_number
        except:
            phonenumber = None
        try:
            website = location.website
        except:
            website = None
        try:
            owner = location.owner_id
        except:
            owner = None
        csv_writer.writerow((
            location.id,
            location.slug,
            location.name,
            address,
            suite,
            location.city,
            postal,
            phonenumber,
            website,
            location.category,
            location.created,
            location.longitude,
            location.latitude,
            owner,
        ))
