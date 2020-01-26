TARGET = "critical"
DATE = "inspection_date"
LICENSE = "License"
INSPECTION_ID = ""
RESTAURANT_ID = "camis"

OTHER_PREDICTORS = [
    "pastPHH",
    "pastCritical",
    "timeSinceLast",
    "ageAtInspection",
    "temperatureMax",
    "heat_burglary",
    "heat_sanitation",
    "heat_garbage",
]
DETAILS = [
    'camis', 'dba', 'boro', 'zipcode', 'cuisine_description',
    'inspection_date', 'action', 'violation_code', 'violation_description',
    'critical_flag', 'score', 'grade', 'inspection_type', 'latitude',
    'longitude'
]

PHH_VIOLATIONS = [
    '02A', '02B', '02G', '02H', '02J', '03A', '03B', '03C', '03D', '03E',
    '03F', '04B', '04C', '04D', '04E', '04F', '04G', '04H', '05A', '05B', '06G'
]

VIOLATIONS = [
    '02A', '02B', '02C', '02D', '02E', '02F', '02G', '02H', '02I', '03A',
    '03B', '03C', '03D', '03E', '03F', '04A', '04B', '04C', '04D', '04E',
    '04F', '04G', '04H', '04J', '04K', '04L', '04M', '04N', '04O', '05A',
    '05B', '05C', '05D', '05E', '05F', '05H', '06A', '06B', '06C', '06D',
    '06E', '06F', '06G', '06H', '06I', '07A', '08A', '08B', '08C', '09A',
    '09B', '09C', '10A', '10B', '10C', '10D', '10E', '10F', '10G', '10H',
    '10I', '10J', '15A1', '15E2', '15E3', '15F1', '15F2', '15F6', '15F7',
    '15F8', '15I', '15J', '15K', '15L', '15S', '15T', '16A', '16B', '16C',
    '16D', '16E', '17A1', '18B', '18C', '18D', '18F', '19A3', '20A', '20D',
    '20E', '20F', '22A', '22B', '22C', '22E', '22F'
]

VIOLATION_MAP = {
    '02': 'FOOD TEMPERATURE',
    '03': 'FOOD SOURCE',
    '04': 'PERSONAL HYGIENE/FOOD PROTECTION',
    '05': 'FACILITY DESIGN',
    '06': 'PERSONAL HYGIENE/FOOD PROTECTION',
    '08': 'VERMIN/GARBAGE',
    '09': 'FACILITY MAINTENANCE',
    '10': 'FACILITY DESIGN',
    '07': 'OTHER',
    '20': 'LETTER GRADE CARD/OTHER POSTER ABSENT',
    '16': 'MENU DESCRIPTION IMPROPER',
    '22': 'OTHER',
    '15': 'NO SMOKING POLICY',
    '18': 'OTHER',
    'na': 'NONE'
}

MONTHS = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]

DAYS = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]

# 311 violation Strings
DSNY_311 = [
    'Missed Collection (All Materials)', 'Dirty Conditions', 'Graffiti',
    'Sanitation Condition', 'Other Enforcement', 'Litter Basket / Request',
    'Sweeping/Missed', 'Recycling Enforcement', 'Sweeping/Inadequate',
    'Overflowing Litter Baskets', 'Sweeping/Missed-Inadequate',
    'Overflowing Recycling Baskets'
]

DEP_311 = [
    'Sewer', 'Hazardous Materials', 'Air Quality', 'Water System',
    'Industrial Waste', 'FATF',
    'Asbestos', 'Plant', 'FCST', 'ATF', 'Water Quality', 'SRDE'
]

DOHMH_311 = [
    'Mobile Food Vendor', 'Food Establishment', 'Smoking', 'Trans Fat',
    'Calorie Labeling',
    'Indoor Air Quality', 'Rodent', 'Standing Water', 'Indoor Sewage',
    'Drinking Water', 'Bottled Water', 'Non-Residential Heat',
    'Food Poisoning', 'Unsanitary Pigeon Condition', 'Mold',
    'Radioactive Material', 'Cooling Tower', 'Asbestos/Garbage Nuisance'
]

NYPD_COMPLAINT_MAP = {
 109: 'GRAND LARCENY',
 104: 'RAPE',
 233: 'SEX CRIMES',
 578: 'HARRASSMENT 2',
 344: 'ASSAULT 3 & RELATED OFFENSES',
 110: 'GRAND LARCENY OF MOTOR VEHICLE',
 106: 'FELONY ASSAULT',
 351: 'CRIMINAL MISCHIEF & RELATED OF',
 361: 'OTHER',
 348: 'VEHICLE AND TRAFFIC LAWS',
 117: 'DANGEROUS DRUGS',
 112: 'THEFT-FRAUD',
 341: 'PETIT LARCENY',
 126: 'OTHER',
 118: 'DANGEROUS WEAPONS',
 235: 'DANGEROUS DRUGS',
 347: 'INTOXICATED & IMPAIRED DRIVING',
 105: 'ROBBERY',
 352: 'CRIMINAL TRESPASS',
 107: 'BURGLARY',
 121: 'CRIMINAL MISCHIEF & RELATED OF',
 236: 'DANGEROUS WEAPONS',
 359: 'OFFENSES AGAINST PUBLIC ADMINI',
 113: 'FORGERY',
 340: 'FRAUDS',
 116: 'SEX CRIMES',
 114: 'ARSON',
 364: 'OTHER STATE LAWS (NON PENAL LAW)',
 125: 'NYS LAWS-UNCLASSIFIED FELONY',
 675: 'ADMINISTRATIVE CODE',
 353: 'UNAUTHORIZED USE OF A VEHICLE',
 342: 'PETIT LARCENY OF MOTOR VEHICLE',
 358: 'OFFENSES INVOLVING FRAUD',
 355: 'OFFENSES AGAINST THE PERSON',
 343: 'THEFT OF SERVICES',
 678: 'MISCELLANEOUS PENAL LAW',
 120: 'CHILD ABANDONMENT/NON SUPPORT',
 111: 'POSSESSION OF STOLEN PROPERTY',
 115: 'PROSTITUTION & RELATED OFFENSES',
 231: "BURGLAR'S TOOLS",
 365: 'ADMINISTRATIVE CODE',
 345: 'OFFENSES RELATED TO CHILDREN',
 101: 'MURDER & NON-NEGL. MANSLAUGHTER',
 232: 'POSSESSION OF STOLEN PROPERTY',
 572: 'DISORDERLY CONDUCT',
 350: 'GAMBLING',
 238: 'FRAUDULENT ACCOSTING',
 363: 'OFFENSES AGAINST PUBLIC SAFETY',
 354: 'ANTICIPATORY OFFENSES',
 124: 'KIDNAPPING',
 346: 'ALCOHOLIC BEVERAGE CONTROL LAW',
 230: 'JOSTLING',
 677: 'OTHER STATE LAWS',
 685: 'ADMINISTRATIVE CODES',
 676: 'NEW YORK CITY HEALTH CODE',
 356: 'PROSTITUTION & RELATED OFFENSES',
 103: 'HOMICIDE-NEGLIGENT,UNCLASSIFIE',
 237: 'ESCAPE 3',
 349: 'DISRUPTION OF A RELIGIOUS SERV',
 455: 'UNLAWFUL POSS. WEAP. ON SCHOOL',
 571: 'LOITERING/GAMBLING (CARDS, DIC',
 122: 'GAMBLING',
 366: 'NEW YORK CITY HEALTH CODE'
}
