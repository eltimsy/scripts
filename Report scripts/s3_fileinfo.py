import unicodecsv
import boto

s3 = boto.connect_s3()
bucket = s3.get_bucket('prod-ratemds-com', validate=False)
with open('s3_fileinfo_locations.csv', 'wb') as csvfile:
    csv_writer = unicodecsv.writer(csvfile, delimiter=',', quotechar='"', quoting=unicodecsv.QUOTE_MINIMAL)
    csv_writer.writerow(('File Path', 'Creation/Modified Date'))
    for key in bucket.list(prefix='media/locations/location/image'):
        print key.name
        csv_writer.writerow((
            key.name,
            key.last_modified,
        ))