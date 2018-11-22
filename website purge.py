from apps.locations.models import Location
import re

websites = Location.objects.filter(id=151775)

abc = websites[0]
regex = re.match('http://www.mciindia.org/', abc.website)
if regex:
    abc.website = ''
    abc.save()