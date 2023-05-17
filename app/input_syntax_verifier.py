import re

class InputSyntaxVerifier:

    def check_name(self, name):
        return re.search("^[a-zA-Z]{2,}", name) and len(name) <= 30
