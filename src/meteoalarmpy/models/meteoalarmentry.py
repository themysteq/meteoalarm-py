import datetime
import json

from pydantic import BaseModel

from .cap_types import (
    CAPCertainty,
    CAPMessageType,
    CAPScope,
    CAPSeverity,
    CAPStatus,
    CAPUrgency,
)


class CAPGeocode(BaseModel):
    EMMA_ID: str


class MeteoalarmEntry(BaseModel):
    cap__geocode: CAPGeocode
    cap__areaDesc: str
    cap__event: str
    cap__sent: datetime.datetime
    cap__expires: datetime.datetime
    cap__effective: datetime.datetime
    cap__onset: datetime.datetime
    cap__certainty: CAPCertainty
    cap__severity: CAPSeverity
    cap__urgency: CAPUrgency
    cap__scope: CAPScope
    cap__message_type: CAPMessageType
    cap__status: CAPStatus
    cap__identifier: str
    atom__published: str
    atom__id: str
    atom__title: str
    atom__updated: str

    class Config:
        @classmethod
        def alias_generator(cls, string: str) -> str:
            # strip "cap__" and "atom__"
            return string.split("__", 1)[1]

        allow_population_by_field_name = True


class JSONCapEncoder(json.JSONEncoder):
    pass


class JSONCapDecoder(json.JSONDecoder):
    pass
