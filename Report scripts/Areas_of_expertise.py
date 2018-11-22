

import unicodecsv
from apps.library.models import Article

with open('Areas_of_expertise.csv', 'wb') as csvfile:
    csv_writer = unicodecsv.writer(csvfile, delimiter=',', quotechar='"', quoting=unicodecsv.QUOTE_MINIMAL)
    articles = Article.objects.all()
    csv_writer.writerow(('ID', 'Name'))
    for article in articles:
        csv_writer.writerow((
            article.id,
            article.title,
        ))
