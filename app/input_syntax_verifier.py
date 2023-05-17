import re


class InputSyntaxVerifier:

    # name must begin with two letters and be up to 30 chars in length
    def check_name(self, name):
        return bool(re.search("^[a-zA-Z]{2,}", name)) and len(name) <= 30

    # message must be minimum 10 chars in length excluding spaces,
    def check_message_min_length(self, message):
        message = message.replace(" ", "")
        return bool(re.search(r"\S{10,}", message))

    # maximum message length is 1000 chars including spaces
    def check_message_max_length(self, message):
        return len(message) <= 1000
