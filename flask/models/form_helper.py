"""Helper functions for form."""
import csv
import json


CACHEFILE = 'groups_cache_dc.json'


def csv_to_array(path):
    """Add non-title rows of CSV file to list."""
    csv_list = list()

    try:
        with open(path, 'r') as csvfile:
            csv_file = csvfile.read()
            data = csv_file.splitlines()
            data.pop(0)
            for value in data:
                csv_list.append(value)
        return csv_list
    except:
        pass


def build_sanitised_multi_select_values(path, sanitized_values):
    """Check values of a list are permitted and add to multi-select list."""
    values = list()
    allowed_values = csv_to_array(path)

    if (sanitized_values != list()):
        for requested_value in sanitized_values:
            if (requested_value in allowed_values) and (requested_value is not None):
                values.append(requested_value)

    if (values == list()):
        return None
    return values


def reporting_orgs(cache_file=CACHEFILE):
    """Return sorted dictionary for organisations."""
    reporting_orgs = dict()
    excluded_ids = ['To be confirmed.']

    with open(cache_file) as c_file:
        groups = json.load(c_file)

        for key, value in groups.items():
            if value['packages'] is not None:
                publisher_iati_id = value['extras']['publisher_iati_id']
                if publisher_iati_id is not None:
                    if publisher_iati_id not in excluded_ids:
                        reporting_orgs[value['display_name']] = publisher_iati_id

    sorted_dict = dict()

    for key in sorted(reporting_orgs.keys()):
        sorted_dict[key] = reporting_orgs[key]

    return sorted_dict


def get_countries(country_codelist="codelists/Country.csv"):
    """Format country list for multiselect."""
    countries = list()
    country_file = country_codelist

    try:
        with open(country_file) as country_f:
            country = country_f.read()
            data = country.splitlines()
            data.pop(0)
            for value in data:
                html_escape_value = value.replace('&', '&amp;').replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')

                convert_case_value = html_escape_value.lower().title()
                countries.append(convert_case_value)
                return countries
    except:
        pass

def get_sector_categories(sector_file='codelists/Sector.csv', sector_category_file='codelists/SectorCategory.csv'):
    """Create multiselect list for sectors."""
    pass # awaiting latest pyIATI changes
