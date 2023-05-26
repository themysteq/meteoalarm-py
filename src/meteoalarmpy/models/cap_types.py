import enum
import typing

# FIXME: TypeAlias is only supported py>=310


class CAPCategory(enum.Enum):
    GEO = "Geo"
    METEO = "Met"
    SAFETY = "Safety"
    SECURITY = "Security"
    RESCUE = "Rescue"
    FIRE = "Fire"
    HEALTH = "Health"
    ENVIRONMENTAL = "Env"
    TRANSPORT = "Transport"
    INFRASTRUCTURE = "Infra"
    CBRNE = "CBRNE"
    OTHER = "Other"


CATEGORY = typing.Literal[
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


class CAPResponseType(enum.Enum):
    SHELTER = "Shelter"
    EVACUATE = "Evacuate"
    PREPARE = "Prepare"
    EXECUTE = "Execute"
    AVOID = "Avoid"
    MONITOR = "Monitor"
    ASSESS = "Assess"
    ALL_CLEAR = "AllClear"
    NONE = "None"


RESPONSE_TYPE = typing.Literal[
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


class CAPUrgency(enum.Enum):
    IMMEDIATE = "Immediate"
    EXPECTED = "Expected"
    FUTURE = "Future"
    PAST = "Past"
    UNKNOWN = "Unknown"


URGENCY = typing.Literal["Immediate", "Expected", "Future", "Past", "Unknown"]


class CAPSeverity(enum.Enum):
    EXTREME = "Extreme"
    SEVERE = "Severe"
    MODERATE = "Moderate"
    MINOR = "Minor"
    UNKOWN = "Unknown"


SEVERITY = typing.Literal["Extreme", "Severe", "Moderate", "Minor", "Unknown"]


class CAPCertainty(enum.Enum):
    OBSERVED = "Observed"
    LIKELY = "Likely"
    POSSIBLE = "Possible"
    UNLIKELY = "Unlikely"
    UNKNOWN = "Unknown"


CERTAINTY = typing.Literal["Observed", "Likely", "Possible", "Unlikely", "Unknown"]


class CAPMessageType(enum.Enum):
    ALERT = "Alert"
    UPDATE = "Update"
    CANCEL = "Cancel"
    ACK = "Ack"
    ERROR = "Error"


MESSAGE_TYPE = typing.Literal["Alert", "Update", "Cancel", "Ack", "Error"]


class CAPScope(enum.Enum):
    PUBLIC = "Public"
    RESTRICTED = "Restricted"
    PRIVATE = "Private"


SCOPE = typing.Literal["Public", "Restricted", "Private"]


class CAPStatus(enum.Enum):
    ACTUAL = "Actual"
    EXERCISE = "Exercise"
    SYSTEM = "System"
    TEST = "Test"
    DRAFT = "Draft"


STATUS = typing.Literal["Actual", "Exercise", "System", "Test", "Draft"]
