from dataclasses import dataclass
from typing import Literal, Optional, Tuple


@dataclass
class CAPInfo:
    """Class 'Info' of Common Alerting Protocol
    Based on https://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2.xsd"""

    language: Optional[str]
    category: Literal[
        "Geo",
        "Met",
        "Safety",
        "Security",
        "Rescue",
        "Fire",
        "Health",
        "Env",
        "Transport",
        "Infra",
        "CBRNE",
        "Other",
    ]
    event: str
    responseType: Optional[
        Literal[
            "Shelter",
            "Evacuate",
            "Prepare",
            "Execute",
            "Avoid",
            "Monitor",
            "Assess",
            "AllClear",
            "None",
        ]
    ]
    urgency: Literal["Immediate", "Expected", "Future", "Past", "Unknown"]
    severity: Literal["Extreme", "Severe", "Moderate", "Minor", "Unknown"]
    certainty: Literal["Observed", "Likely", "Possible", "Unlikely", "Unknown"]
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
