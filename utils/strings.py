TARGET = "critical"
DATE = "inspection_date"
LICENSE = "License"
INSPECTION_ID = ""
RESTAURANT_ID = "camis"

# features that we have built
FEATURES = [
 'tmax',
 'tmax_3d',
 'time_since_last',
 'past_critical',
 'past_score',
 'dsny_heat_score',
 'dep_heat_score',
 'dohmh_heat_score',
 'is_chain',
 'init_inspec'
]

# catagorical features that will need to be encoded
CAT_FEATURES = [
    'past_grade',
    'boro',
    'zipcode',
    'weekday'
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

# from the blue book
VIOLATIONS = [
    '02A', '02B', '02C', '02D', '02E', '02F', '02G', '02H', '02I', '03A',
    '03B', '03C', '03D', '03E', '03F', '04A', '04B', '04C', '04D', '04E',
    '04F', '04G', '04H', '04J', '04K', '04L', '04M', '04N', '04O', '05A',
    '05B', '05C', '05D', '05E', '05F', '05H', '06A', '06B', '06C', '06D',
    '06E', '06F', '06G', '06H', '06I', '07A', '08A', '08B', '08C', '09A',
    '09B', '09C', '10A', '10B', '10C', '10D', '10E', '10F', '10G', '10H',
    '10I', '10J'
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
