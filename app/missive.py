from datetime import datetime
from app.printer import Printer
import app.styles as styles


class Missive:

    def __init__(self,
                 name,
                 message,
                 creation_time=None,
                 location='Milky Way, Sol, Earth, British Isles, England, Devon',
                 gathering="Burning Nest '23",
                 printer=Printer()
                 ):
        self.name = name
        self.message = message
        self.creation_time = creation_time or datetime.now().__format__('%Y-%m-%d %H:%M:%S')
        self.location = location
        self.gathering = gathering
        self.printer = printer

    @classmethod
    def init_from_record(cls, record):
        return Missive(name=record[1],
                       message=record[2],
                       creation_time=record[3],
                       location=record[4],
                       gathering=record[5])

    def display_missive(self):
        return self.printer.process(self.__display_content())

    def __format_creation_time(self):
        datetime_object = datetime.strptime(self.creation_time, '%Y-%m-%d %H:%M:%S')
        return datetime_object.strftime('%a, %d %b %Y %H:%M')

    def __format_location(self):
        return f'Milky Way, Sol, Earth, {self.location}'

    def __display_content(self):
        return [
            {'text': '\nTime recorded:      ',      'styling': styles.MISSIVE_KEY},
            {'text': self.__format_creation_time(), 'styling': styles.MISSIVE_DEFAULT_VALUE},
            {'text': '\nRecording location: ',      'styling': styles.MISSIVE_KEY},
            {'text': self.location,                 'styling': styles.MISSIVE_DEFAULT_VALUE},
            {'text': '\nGathering:          ',      'styling': styles.MISSIVE_KEY},
            {'text': self.gathering,                'styling': styles.MISSIVE_DEFAULT_VALUE},
            {'text': '\n\nScribe:  ',               'styling': styles.MISSIVE_KEY},
            {'text': self.name,                     'styling': styles.MISSIVE_USER},
            {'text': '\nMissive: ',                 'styling': styles.MISSIVE_KEY},
            {'text': self.message,                  'styling': styles.MISSIVE_MESSAGE}
        ]

    def __eq__(self, other):
        return (
            self.name == other.name and
            self.message == other.message and
            self.creation_time == other.creation_time and
            self.location == other.location and
            self.gathering == other.gathering
        )
