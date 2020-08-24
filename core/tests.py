from django.test import TestCase
from django.utils import timezone
from .models import SystemMessage, EventMessage, Game

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

    def test_front_page( self ):
        response = self.client.get( '/' )
        self.assertEqual( response.status_code, 200 )
