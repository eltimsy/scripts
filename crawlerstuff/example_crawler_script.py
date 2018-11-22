import requests
import html5lib
import csv
from bs4 import BeautifulSoup

notsure = ['https://www.ratemds.com/doctors/123/unsubscribe/1234/']

urls = ['https://www.ratemds.com/doctor-ratings/82090/Dr-Rafaele-D&apos;Agrosa-Toronto-ON.html', 
        'https://www.ratemds.com/about/',
        'https://www.ratemds.com/about/faq/',
        'https://www.ratemds.com/about/contact/',
        'https://www.ratemds.com/about/press/',
        'https://www.ratemds.com/about/advertise/',
        'https://www.ratemds.com/about/terms/',
        'https://www.ratemds.com/about/terms/paid/',
        'https://www.ratemds.com/about/privacy/',
        'https://www.ratemds.com/about/jasmine/',
        'https://www.ratemds.com/specialties/',
        'https://www.ratemds.com/specialties/family-gp/',
        'https://www.ratemds.com/facilities/local/',
        'https://www.ratemds.com/facilities/',
        'https://www.ratemds.com/facilities/bc/vancouver/',
        'https://www.ratemds.com/facilities/ca-bc-vancouver-dentist-false-creek/index.jsp',
        'https://www.ratemds.com/hospital/us-pa-philadelphia-kindred-hospital-south-philadelphia/',
        'https://www.ratemds.com/clinic/ca-on-toronto-dr-herbert-veisman-762/doctors/',
        'https://www.ratemds.com/doctors/local/index.jsp',
        'https://www.ratemds.com/doctors/create/',
        'https://www.ratemds.com/doctors/verify/',
        'https://www.ratemds.com/doctors/4003968/Dr-Prasanna-Moon-Nagpur-MH.html',
        'https://www.ratemds.com/doctors/',
        'https://www.ratemds.com/amp/doctor-ratings/3427441/KRISTA+R.-NICKERSON-Williston-VT.html',
        'https://www.ratemds.com/doctor-ratings/3427441/KRISTA+R.-NICKERSON-Williston-VT.html',
        'https://www.ratemds.com/best-doctors/',
        'https://www.ratemds.com/best-doctors/on/',
        'https://www.ratemds.com/best-doctors/wc/cape-town/index.jsp',
        'https://www.ratemds.com/best-doctors/ny/new-york/',
        'https://www.ratemds.com/best-doctors/wc/cape-town/family-gp/',
        'https://www.ratemds.com/plans/doctor/',
        'https://www.ratemds.com/plans/2138610/',
        'https://www.ratemds.com/plans/213133/',
        'https://www.ratemds.com/plans/213133/success/',
        'https://www.ratemds.com/index.jsp',
        'https://www.ratemds.com/m/ratings.jsp?did=1234',
        'https://www.ratemds.com/AddRating.jsp?did=1234',
        'https://www.ratemds.com/birdsofafeather.jsp?did=1234',
        'https://www.ratemds.com/embed-ratings.jsp?did=1234',
        'https://www.ratemds.com/filecache/doctor-ratings.jsp?did=1234',
        'https://www.ratemds.com/AddFact.jsp?did=1234',
        'https://www.ratemds.com/docImageAdd.jsp?did=1234',
        'https://www.ratemds.com/member/processSaveDoc.jsp?did=1234',
        'https://www.ratemds.com/subscribe.jsp?did=1234',
        'https://www.ratemds.com/search.jsp',
        'https://www.ratemds.com/m/search.jsp',
        'https://www.ratemds.com/m/searchresults.jsp',
        'https://www.ratemds.com/SelectState.jsp',
        'https://www.ratemds.com/filecache/SelectDoctor.jsp',
        'https://www.ratemds.com/SelectDoctor.jsp',
        'https://www.ratemds.com/filecache/topTen.jsp',
        'https://www.ratemds.com/getCityState.jsp',
        'https://www.ratemds.com/canada',
        'https://www.ratemds.com/AddDoctor.jsp',
        'https://www.ratemds.com/ConfirmAddDoctor.jsp',
        'https://www.ratemds.com/StartAddDoctor.jsp',
        'https://www.ratemds.com/filecache/hospitalDocs.jsp?hid=123',
        'https://www.ratemds.com/hospitals/hospitalRatings.jsp?hid=123',
        'https://www.ratemds.com/hospitals/AddHospitalRating.jsp?hid=123',
        'https://www.ratemds.com/hospitals/hospitalSearch.jsp',
        'https://www.ratemds.com/hospitals/hospSearchResults.jsp',
        'https://www.ratemds.com/hospitals/SelectHospital.jsp',
        'https://www.ratemds.com/hospitals/',
        'https://www.ratemds.com/tos.jsp',        
        'https://www.ratemds.com/privacy.html',
        'https://www.ratemds.com/contact',
        'https://www.ratemds.com/social',
        'https://www.ratemds.com/member',
        'https://www.ratemds.com/flagRating.jsp',
        'https://www.ratemds.com/flagDoctor.jsp',
        'https://www.ratemds.com/hospitals/AddHospital.jsp',
        'https://www.ratemds.com/ny/new-york/',
        'https://www.ratemds.com/404',
        'https://www.ratemds.com/500',
        'https://www.ratemds.com/503'
        ]

with open('testtest.csv', 'wb') as csvfile:
    fieldnames = ['url', 'canonical' , 'title', 'meta_description', 'robots', 'h1', 'h2', ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for url in urls:    
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html5lib")
        
        meta = soup.findAll(attrs={'name': 'description'})
        robots = soup.findAll(attrs={'name': 'robots'})
        canonical = soup.find_all('link', rel='canonical')
                        
        writer.writerow({'url': url,
                         'canonical': canonical[0]['href'] if canonical else "None",
                         'title': soup.title.text,
                         'meta_description': meta[0]['content'] if meta else "None",
                         'robots': robots[0]['content'] if robots else "None",
                         'h1': map(lambda x: x.text, soup.find_all('h1')),
                         'h2': map(lambda x: x.text, soup.find_all('h2')),
                         })    
        print [
            canonical[0]['href'] if canonical else "None",
            soup.title.text,
            meta[0]['content'] if meta else "None",
            robots[0]['content'] if robots else "None",
            map(lambda x: x.text, soup.find_all('h1')),
            map(lambda x: x.text, soup.find_all('h2')),
        ]