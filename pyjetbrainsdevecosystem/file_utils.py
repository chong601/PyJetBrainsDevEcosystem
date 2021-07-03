import csv

# A dictionary that returns the correct delimiter to parse the questions
# 2019+ uses CSV which is handled by unpack_csv_data instead
dash_type_map = {
    2017: ' — ',
    2018: ' - '
}


def unpack_csv_data(csv_object):
    """
    Accepts a fle object and returns a csv.DictReader object for parsing.
    The CSV file syntax is autodetected before parsing.
    This function can be used for any CSV files for parsing.

    :param csv_object: The opened file object
    :return: csv.DictReader of the file
    """
    # Reads 2 MB of the file to detect the CSV dialect
    dialect = csv.Sniffer().sniff(csv_object.read(2097152))
    # Rewinds the file back to the start position
    csv_object.seek(0)
    csv_data = csv.DictReader(csv_object, dialect=dialect)
    return csv_data


def split_data_by_dash(entry: str, year):
    """
    Splits the data based on the delimiter for that particular year.
    The split delimiter will be obtained from dash_type_map dictionary using the year as the key.

    :param entry: The string to be splitted
    :param year: The year the string is from
    :return: A tuple in the form of (columnname, description)
    """
    column: str
    description: str
    column, description = entry.split(dash_type_map.get(year), maxsplit=1)
    return column, strip_double_quotes(description).strip()


def strip_double_quotes(entry: str):
    """
    Strips out the double-quotes from the string

    :param entry: The string with double-quotes
    :return: String without double-quotes
    """
    # WARNING: CHECK THE CONTENTS OF THE FILE WHETHER IT HAS DOUBLE-QUOTES ELSEWHERE OR IT WILL STRIP IT OUT.
    return entry.replace('"', '')
