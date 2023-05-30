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


def test_meteoalarmentry_nonamespace_clashing():
    """Check for clashing names if namespace is removed"""

    fields = meteoalarmentry.MeteoalarmEntry.__fields__
    fields_keys = fields.keys()
    # this is the same as :func:`~meteoalarmentry.MeteoalarmEntry.Config.alias_generator`
    fields_no_prefixes = [str(f).split("__", 1)[1] for f in fields_keys]
    fields_aliases = [v.alias for v in fields.values()]
    fields_no_prefixes_unique = list(set(fields_no_prefixes))
    assert len(fields_no_prefixes) == len(
        fields_no_prefixes_unique
    ), "There are two identicial fields in different namespaces"
    assert list(sorted(fields_no_prefixes)) == list(
        sorted(fields_aliases)
    ), "Field aliasing mechanism changed"
