from dataclasses import dataclass
from typing import Optional, Tuple

from cap_types import CATEGORY, CERTAINTY, RESPONSE_TYPE, SEVERITY, URGENCY


@dataclass
class CAPInfo:
    """Class 'Info' of Common Alerting Protocol
    Based on https://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd"""

    language: Optional[str]
    category: CATEGORY
    event: str
    responseType: Optional[RESPONSE_TYPE]
    urgency: URGENCY
    severity: SEVERITY
    certainty: CERTAINTY
    audience: Optional[str]
    # FIXME: 'eventCode' does not conform yet
    # TODO: NamedTuple?
    eventCode: Optional[Tuple[str, str]]
    # FIXME: <xs:dateTime> parse time
    effective: Optional[str]
    # FIXME: <xs:dateTime>
    onset: Optional[str]
    # FIXME: <xs:dateTime>
    expires: Optional[str]

    senderName: Optional[str]
    headline: Optional[str]
    description: Optional[str]
    instruction: Optional[str]
    web: Optional[str]
    contact: Optional[str]
    # FIXME: complexType
    parameter: Optional[Tuple[str, str]]
    # FIXME: complexType
    resource: Optional
    # FIXME: complexType
    area: Optional
