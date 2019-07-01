import urllib.request
import re
import csv
from pathlib import Path


# Regex to match primary data row
# e.g. AADNV V  648330: N=Aedes albopictus densovirus (isolate Boublik/1994)
re_primary = re.compile(
    r'(?P<code>[A-Z0-9]{3,5})\s+(?P<kingdom>[A|B|E|V|O])\s+(?P<taxon_node>[0-9]+):\sN=(?P<scientific_name>[\w()\-\s\/]+)')

# Regex to match secondary rows
# e.g. C=Edeltanne / S = European silver fir
re_secondary = re.compile(r'C=(?P<common_name>[\w\s]+)|S=(?P<synonym>[\w\s]+)')

SPECLIST_URL = 'https://www.uniprot.org/docs/speclist.txt'
SPECLIST_PATH = Path('./speclist.txt')
SPECLIST_CSV_PATH = Path('./speclist.csv')


def get_records_from_speclist():

    record = None

    with open('data/speclist.txt') as f:
        for line in f:
            line = line.rstrip()

            # Have me matched a primary row e.g.
            # ABDAC E  515833: N=Abdopus aculeatus
            primary_match = re_primary.search(line)
            if primary_match:
                # If we have an existing record, yield it before creating
                # a new record
                if record:
                    yield record

                record = primary_match.groupdict()

            # If we have a record, see if we have a common name/synonym row
            # E.g. C=Algae octopus | S=Octopus aculeatus
            elif record:
                secondary_match = re_secondary.search(line)
                if secondary_match:
                    # Update the record with any secondary row matches
                    record.update(
                        {k: v for k, v in secondary_match.groupdict().items() if v})


def download_speclist_file():

    urllib.request.urlretrieve(SPECLIST_URL, SPECLIST_PATH)


def main():
    download_speclist_file()


if __name__ == "__main__":
    main()
