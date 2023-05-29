import json

from meteoalarmpy.models import meteoalarmentry


def test_meteoalarmentry_capgeocode():
    geocode = meteoalarmentry.CAPGeocode.parse_obj(
        {"EMMA_ID": "PL2137"}
    )  # type: meteoalarmentry.CAPGeocode
    geocode_json = geocode.json(indent=4)
    geocode_json_rev = meteoalarmentry.CAPGeocode.parse_obj(
        json.loads(geocode_json)
    )  # type:meteoalarmentry.CAPGeocode
    assert geocode is not None
    assert geocode.EMMA_ID == "PL2137"
    assert geocode_json_rev.EMMA_ID == "PL2137"
