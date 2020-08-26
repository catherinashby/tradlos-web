from unittest import skip
from django.test import TestCase, RequestFactory
from django.utils import timezone
from .models import User, SystemMessage, EventMessage, Game
from .views import landing, entry_page

class ModelsTest( TestCase ):

    def test_system_messages( self ):
        txt = "system message"
        msg = SystemMessage(message_added=timezone.now(), message_text=txt)
        lbl = '{}'.format( msg )
        self.assertTrue( lbl.endswith(txt) )

    def test_event_messages( self ):
        txt = "event message"
        msg = EventMessage(event_added=timezone.now(), event_title=txt)
        lbl = '{}'.format( msg )
        self.assertTrue( lbl.endswith(txt) )

    def test_game_object( self ):
        txt = "game name"
        obj = Game(game_name=txt)
        lbl = '{}'.format(obj)
        self.assertEqual(lbl,txt)


class ViewsTest( TestCase ):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user( username='padraigh',
            email='padraigh@fallenacorn,com', password='gillespie')

    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_landing_page( self ):
        response = self.client.get( '/' )
        self.assertEqual( response.status_code, 200 )
        self.assertEqual( response.templates[0].name, 'frontpage.html' )

        self.client.login( username="padraigh",password="gillespie")
        response = self.client.get( '/' )
        self.assertEqual( response.status_code, 200 )
        self.assertEqual( response.templates[0].name, 'homepage.html' )

    def test_entry_page( self ):
        response = self.client.get( '/entry/' )
        self.assertEqual( response.status_code, 200 )
        self.assertEqual( response.templates[0].name, 'registration/entryPage.html' )

        request = self.factory.post('/entry/',{'user_name': "cory"})
        response = entry_page( request )
        rc = response.content
        bgn = rc.find(b'<p class="helptext ')
        end = rc.find(b'>',bgn)
        txt = rc[19+bgn:end-1].decode()
        self.assertEqual( txt, 'nop' )

        request = self.factory.post( '/entry/', { 'user_name': "padraigh" } )
        response = entry_page( request )
        rc = response.content
        bgn = rc.find(b'<div class="errmsg')
        mid = rc.find(b'>',bgn)
        end = rc.find(b'</div>',mid)
        txt = rc[1+mid:end].decode()
        self.assertEqual(txt, 'Name already in use')

        request = self.factory.post( '/entry/', { 'user_name': "padraigh",
                                                  'sign_in': ""} )
        response = entry_page( request )
        rc = response.content
        bgn = rc.find(b'<!-- TEMPLATE: ')
        end = rc.find(b'-->',bgn)
        txt = rc[15+bgn:end-1].decode()
        self.assertEqual( txt, 'registration/loginPage.html')


        request = self.factory.post( '/entry/', { 'user_name': "marilynn" } )
        response = entry_page( request )
        rc = response.content
        bgn = rc.find(b'<div class="errmsg')
        mid = rc.find(b'>',bgn)
        end = rc.find(b'</div>',mid)
        txt = rc[1+mid:end].decode()
        self.assertEqual(txt, 'Name not found')

        request = self.factory.post( '/entry/', { 'user_name': "marilynn",
                                                  'sign_up': ""} )
        response = entry_page( request )
        rc = response.content
        bgn = rc.find(b'<!-- TEMPLATE: ')
        end = rc.find(b'-->',bgn)
        txt = rc[15+bgn:end-1].decode()
        self.assertEqual( txt, 'registration/registerPage.html')

    @skip("login page")
    def test_login_page( self ):
       response = self.client.get( '//' )
       self.assertEqual( response.status_code, 200 )
       self.assertEqual( response.templates[0].name, 'registration/loginPage.html' )

    @skip("registry page")
    def test_registry_page( self ):
        response = self.client.get( '//' )
        self.assertEqual( response.status_code, 200 )
        self.assertEqual( response.templates[0].name, 'registration/registerPage.html' )

    def test_home_page( self ):
        response = self.client.get( '/home/' )
        self.assertEqual( response.status_code, 200 )
        self.assertEqual( response.templates[0].name, 'homepage.html' )
