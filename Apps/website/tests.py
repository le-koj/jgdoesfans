from django.test import TestCase
from django.urls import reverse, resolve
from .models import HomePage, Poster, SocialMedia

# Create your tests here.
class HomeTests(TestCase):
    def setUp(self):
        self.homepage = HomePage.objects.create(name='index', heading='JAY GREENE', sub_title='CEILING FAN SPECIALIST', stamp='17 years experience', phone='7148873880', email='sample@mail.com')
        #url = reverse('home')
        #self.response = self.client.get(url)

    def test_HomePage_properties(self):
        home_page_name = self.homepage.name
        heading = self.homepage.heading
        sub_title = self.homepage.sub_title
        stamp = self.homepage.stamp
        phone = self.homepage.phone
        email = self.homepage.email

        self.assertEquals([home_page_name, heading, sub_title, stamp, phone, email], ['index', 'JAY GREENE', 'CEILING FAN SPECIALIST', '17 years experience', '7148873880', 'sample@mail.com'])


class PosterTests(TestCase):
    def setUp(self):
        img_1 = '/Users/lekoj/Developer/jgdoesfans/media/image/jgdoesfans_site_mock.jpg'
        self.poster = Poster.objects.create(name='site poster', imagefile=img_1, alternate_name='background image of Jay Greene and fan')

    def test_HomePage_properties(self):
        name = self.poster.name
        alternate = self.poster.alternate_name


        self.assertEquals([name, alternate], ['site poster', 'background image of Jay Greene and fan'])
