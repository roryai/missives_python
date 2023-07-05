from app.missive import Missive
from app.printer import Printer
from app.operator_message import OperatorMessage
import app.styles as styles
from datetime import datetime


printer = Printer(True)

info_message = 'This is a test message to display the text formatting.' \
               '\nI am using this message as the real message is too long and will not ' \
               '\nfit on the same screen as everything else.' \

missive = Missive(name="Rory", message=info_message,
                  creation_time=datetime(2023, 4, 20, 8, 45, 20, 56178), printer=printer)

OperatorMessage('read_write_learn', printer)
OperatorMessage('name_only_letters', printer)
OperatorMessage('missive_recorded', printer)
OperatorMessage('what_is_your_name', printer)
printer.process([{'text': info_message, 'styling': styles.INFO}])
missive.display_missive()
OperatorMessage('enter_to_continue', printer)
