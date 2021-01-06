

class TextDetailRecord(object):
    def __init__(self, a_number, b_number, timestamp):

        self.a_number = a_number
        self.b_number = b_number
        self.timestamp = timestamp

    def to_string(self):
        return "{} calls {} at time {}".format(self.a_number, self.b_number, self.timestamp)


class CallDetailRecord(TextDetailRecord):
    def __init__(self, a_number, b_number, timestamp, duration):

        super(CallDetailRecord, self).__init__(a_number, b_number, timestamp)

        self.duration = duration

    def to_string(self):
        return "{} texts {} at time {}, lasting {} seconds".format(self.a_number, self.b_number, self.timestamp, self.duration)

    def is_telemarketing(self, number):
        """
        - Fixed lines start with an area code enclosed in brackets. The area
          codes vary in length but always begin with 0.
        - Mobile numbers have no parentheses, but have a space in the middle
          of the number to help readability. The prefix of a mobile number
          is its first four digits, and they always start with 7, 8 or 9.
        - Telemarketers' numbers have no parentheses or space, but they start
          with the area code 140.
        """

        import re
        match = re.search(r'(^140)', number)

        if match is not None:
            std = match.group(1)
            return std
        else:
            return None

    def is_mobile(self, number):
        """
        - Fixed lines start with an area code enclosed in brackets. The area
          codes vary in length but always begin with 0.
        - Mobile numbers have no parentheses, but have a space in the middle
          of the number to help readability. The prefix of a mobile number
          is its first four digits, and they always start with 7, 8 or 9.
        - Telemarketers' numbers have no parentheses or space, but they start
          with the area code 140.
        """

        import re
        match = re.search(r'(^[789]...)', number)

        if match is not None:
            std = match.group(1)
            return std
        else:
            return None

    def is_fixed(self, number):
        """
        - Fixed lines start with an area code enclosed in brackets. The area
          codes vary in length but always begin with 0.
        - Mobile numbers have no parentheses, but have a space in the middle
          of the number to help readability. The prefix of a mobile number
          is its first four digits, and they always start with 7, 8 or 9.
        - Telemarketers' numbers have no parentheses or space, but they start
          with the area code 140.
        """

        import re
        if re.search(r'\(.*?\)', number) is not None:

            search_results = re.finditer(r'\(.*?\)', number)
            for item in search_results:
                std = item.group(0)
                return std
        else:
            return None

    def is_fixed_bangalore(self, number):
        """
        - Fixed lines start with an area code enclosed in brackets. The area
          codes vary in length but always begin with 0.
        - Mobile numbers have no parentheses, but have a space in the middle
          of the number to help readability. The prefix of a mobile number
          is its first four digits, and they always start with 7, 8 or 9.
        - Telemarketers' numbers have no parentheses or space, but they start
          with the area code 140.
        """

        import re
        if re.search(r'\(080\)', number) is not None:

            search_results = re.finditer(r'\(.*?\)', number)
            for item in search_results:
                std = item.group(0)
                return std
        else:
            return None




class CdrParser:

    def parse_record(self, record):
        assert len(record) == 3 or len(record) == 4

        if len(record) == 3:
            return self.__parse_text_record(record)

        if len(record) == 4:
            return self.__parse_call_record(record)

    def __parse_text_record(self, record):
        assert len(record) == 3

        a_number = record[0]
        b_number = record[1]
        timestamp = record[2]

        return TextDetailRecord(a_number, b_number, timestamp)

    def __parse_call_record(self, record):
        assert len(record) == 4

        a_number = record[0]
        b_number = record[1]
        timestamp = record[2]
        duration = int(record[3])

        return CallDetailRecord(a_number, b_number, timestamp, duration)


