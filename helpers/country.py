"""
LineCMS - Content Management System (Product & Blogging) for Rapid website development
Website: www.linecms.com
Author: S. Jangra & Mark A.R. Pequeras
"""

# Stripe only support countries below
countries = {'AD': 'Andorra', 'AE': 'United Arab Emirates', 'AF': 'Afghanistan', 'AG': 'Antigua and Barbuda', 'AI': 'Anguilla',
              'AL': 'Albania', 'AM': 'Armenia', 'AO': 'Angola', 'AQ': 'Antarctica', 'AR': 'Argentina', 'AT': 'Austria', 'AU': 'Australia', 
              'AW': 'Aruba', 'AX': 'Aland Islands', 'AZ': 'Azerbaijan', 'BA': 'Bosnia and Herzegovina', 'BB': 'Barbados', 'BD': 'Bangladesh', 
              'BE': 'Belgium', 'BF': 'Burkina Faso', 'BG': 'Bulgaria', 'BH': 'Bahrain', 'BI': 'Burundi', 'BJ': 'Benin', 'BL': 'Saint Barthelemy', 
              'BM': 'Bermuda', 'BN': 'Brunei Darussalam', 'BO': 'Bolivia (Plurinational State of)', 'BQ': 'Bonaire, Sint Eustatius and Saba', 
              'BR': 'Brazil', 'BS': 'Bahamas', 'BT': 'Bhutan', 'BV': 'Bouvet Island', 'BW': 'Botswana', 'BY': 'Belarus', 'BZ': 'Belize', 
              'CA': 'Canada', 'CD': 'Congo, Democratic Republic of the', 'CF': 'Central African Republic', 'CG': 'Congo', 
              'CH': 'Switzerland', 'CI': "Cote d'Ivoire", 'CK': 'Cook Islands', 'CL': 'Chile', 'CM': 'Cameroon', 'CN': 'China', 'CO': 'Colombia', 
              'CR': 'Costa Rica', 'CV': 'Cabo Verde', 'CW': 'Curacao', 'CY': 'Cyprus', 'CZ': 'Czechia', 'DE': 'Germany', 'DJ': 'Djibouti', 
              'DK': 'Denmark', 'DM': 'Dominica', 'DO': 'Dominican Republic', 'DZ': 'Algeria', 'EC': 'Ecuador', 'EE': 'Estonia', 'EG': 'Egypt', 
              'EH': 'Western Sahara', 'ER': 'Eritrea', 'ES': 'Spain', 'ET': 'Ethiopia', 'FI': 'Finland', 'FJ': 'Fiji', 'FK': 'Falkland Islands (Malvinas)',
              'FO': 'Faroe Islands', 'FR': 'France', 'GA': 'Gabon', 'GB': 'United Kingdom of Great Britain and Northern Ireland', 'GD': 'Grenada', 'GE': 'Georgia', 
              'GF': 'French Guiana', 'GG': 'Guernsey', 'GH': 'Ghana', 'GI': 'Gibraltar', 'GL': 'Greenland', 'GM': 'Gambia', 'GN': 'Guinea', 'GP': 'Guadeloupe', 
              'GQ': 'Equatorial Guinea', 'GR': 'Greece', 'GS': 'South Georgia and the South Sandwich Islands', 'GT': 'Guatemala', 'GU': 'Guam', 'GW': 'Guinea-Bissau', 
              'GY': 'Guyana', 'HK': 'Hong Kong', 'HN': 'Honduras', 'HR': 'Croatia', 'HT': 'Haiti', 'HU': 'Hungary', 'ID': 'Indonesia', 'IE': 'Ireland', 'IL': 'Israel', 
              'IM': 'Isle of Man', 'IN': 'India', 'IO': 'British Indian Ocean Territory', 'IQ': 'Iraq', 'IS': 'Iceland', 'IT': 'Italy', 'JE': 'Jersey', 'JM': 'Jamaica', 
              'JO': 'Jordan', 'JP': 'Japan', 'KE': 'Kenya', 'KG': 'Kyrgyzstan', 'KH': 'Cambodia', 'KI': 'Kiribati', 'KM': 'Comoros', 'KN': 'Saint Kitts and Nevis', 
              'KR': 'Korea, Republic of', 'KW': 'Kuwait', 'KY': 'Cayman Islands', 'KZ': 'Kazakhstan', 'LA': "Lao People's Democratic Republic", 'LB': 'Lebanon', 
              'LC': 'Saint Lucia', 'LI': 'Liechtenstein', 'LK': 'Sri Lanka', 'LR': 'Liberia', 'LS': 'Lesotho', 'LT': 'Lithuania', 'LU': 'Luxembourg', 'LV': 'Latvia', 
              'LY': 'Libya', 'MA': 'Morocco', 'MC': 'Monaco', 'MD': 'Moldova, Republic of', 'ME': 'Montenegro', 'MF': 'Saint Martin (French part)', 'MG': 'Madagascar', 
              'MK': 'North Macedonia', 'ML': 'Mali', 'MM': 'Myanmar', 'MN': 'Mongolia', 'MO': 'Macao', 'MQ': 'Martinique', 'MR': 'Mauritania', 'MS': 'Montserrat',
              'MT': 'Malta', 'MU': 'Mauritius', 'MV': 'Maldives', 'MW': 'Malawi', 'MX': 'Mexico', 'MY': 'Malaysia', 'MZ': 'Mozambique', 'NA': 'Namibia', 
              'NC': 'New Caledonia', 'NE': 'Niger', 'NG': 'Nigeria', 'NI': 'Nicaragua', 'NL': 'Netherlands', 'NO': 'Norway', 'NP': 'Nepal', 'NR': 'Nauru', 'NU': 'Niue', 
              'NZ': 'New Zealand', 'OM': 'Oman', 'PA': 'Panama', 'PE': 'Peru', 'PF': 'French Polynesia', 'PG': 'Papua New Guinea', 'PH': 'Philippines', 'PK': 'Pakistan', 
              'PL': 'Poland', 'PM': 'Saint Pierre and Miquelon', 'PN': 'Pitcairn', 'PR': 'Puerto Rico', 'PS': 'Palestine, State of', 'PT': 'Portugal', 'PY': 'Paraguay', 
              'QA': 'Qatar', 'RE': 'Reunion', 'RO': 'Romania', 'RS': 'Serbia', 'RU': 'Russian Federation', 'RW': 'Rwanda', 'SA': 'Saudi Arabia', 'SB': 'Solomon Islands', 
              'SC': 'Seychelles', 'SE': 'Sweden', 'SG': 'Singapore', 'SH': 'Saint Helena, Ascension and Tristan da Cunha', 'SI': 'Slovenia', 'SJ': 'Svalbard and Jan Mayen',
              'SK': 'Slovakia', 'SL': 'Sierra Leone', 'SM': 'San Marino', 'SN': 'Senegal', 'SO': 'Somalia', 'SR': 'Suriname', 'SS': 'South Sudan', 'ST': 'Sao Tome and Principe', 
              'SV': 'El Salvador', 'SX': 'Sint Maarten (Dutch part)', 'SZ': 'Eswatini', 'TC': 'Turks and Caicos Islands', 'TD': 'Chad', 'TF': 'French Southern Territories', 
              'TG': 'Togo', 'TH': 'Thailand', 'TJ': 'Tajikistan', 'TK': 'Tokelau', 'TL': 'Timor-Leste', 'TM': 'Turkmenistan', 'TN': 'Tunisia', 'TO': 'Tonga', 'TR': 'Turkey',
              'TT': 'Trinidad and Tobago', 'TV': 'Tuvalu', 'TW': 'Taiwan, Province of China', 'TZ': 'Tanzania, United Republic of', 'UA': 'Ukraine', 'UG': 'Uganda', 
              'US': 'United States of America', 'UY': 'Uruguay', 'UZ': 'Uzbekistan', 'VA': 'Holy See', 'VC': 'Saint Vincent and the Grenadines', 'VE': 'Venezuela (Bolivarian Republic of)', 
              'VG': 'Virgin Islands (British)', 'VN': 'Viet Nam', 'VU': 'Vanuatu', 'WF': 'Wallis and Futuna', 'WS': 'Samoa', 'YE': 'Yemen', 'YT': 'Mayotte', 'ZA': 'South Africa', 'ZM': 'Zambia', 'ZW': 'Zimbabwe'}


# List of countries (for future)
all_countries = {"AF":"Afghanistan",
                "AX":"Aland Islands",
                "AL":"Albania",
                "DZ":"Algeria",
                "AS":"American Samoa",
                "AD":"Andorra",
                "AO":"Angola",
                "AI":"Anguilla",
                "AQ":"Antarctica",
                "AG":"Antigua and Barbuda",
                "AR":"Argentina",
                "AM":"Armenia",
                "AW":"Aruba",
                "AU":"Australia",
                "AT":"Austria", #
                "AZ":"Azerbaijan",
                "BS":"Bahamas",
                "BH":"Bahrain",
                "BD":"Bangladesh",
                "BB":"Barbados",
                "BY":"Belarus",
                "BE":"Belgium",
                "BZ":"Belize",
                "BJ":"Benin",
                "BM":"Bermuda",
                "BT":"Bhutan",
                "BO":"Bolivia, Plurinational State of",
                "BQ":"Bonaire, Sint Eustatius and Saba",
                "BA":"Bosnia and Herzegovina",
                "BW":"Botswana",
                "BV":"Bouvet Island",
                "BR":"Brazil",
                "IO":"British Indian Ocean Territory",
                "BN":"Brunei Darussalam",
                "BG":"Bulgaria", #
                "BF":"Burkina Faso",
                "BI":"Burundi",
                "KH":"Cambodia",
                "CM":"Cameroon",
                "CA":"Canada",
                "CV":"Cape Verde",
                "KY":"Cayman Islands",
                "CF":"Central African Republic",
                "TD":"Chad",
                "CL":"Chile",
                "CN":"China",
                "CX":"Christmas Island",
                "CC":"Cocos (Keeling) Islands",
                "CO":"Colombia",
                "KM":"Comoros",
                "CG":"Congo",
                "CD":"Congo, The Democratic Republic of the",
                "CK":"Cook Islands",
                "CR":"Costa Rica",
                "HR":"Croatia",
                "CU":"Cuba",
                "CY":"Cyprus",
                "CZ":"Czech Republic", #
                "DK":"Denmark",
                "DJ":"Djibouti",
                "DM":"Dominica",
                "DO":"Dominican Republic",
                "EC":"Ecuador",
                "EG":"Egypt",
                "SV":"El Salvador",
                "GQ":"Equatorial Guinea",
                "ER":"Eritrea",
                "EE":"Estonia",
                "ET":"Ethiopia",
                "FK":"Falkland Islands (Malvinas)",
                "FO":"Faroe Islands",
                "FJ":"Fiji",
                "FI":"Finland",
                "FR":"France", #
                "GF":"French Guiana",
                "PF":"French Polynesia",
                "TF":"French Southern Territories",
                "GA":"Gabon",
                "GM":"Gambia",
                "GE":"Georgia",
                "DE":"Germany",
                "GH":"Ghana",
                "GI":"Gibraltar",
                "GR":"Greece",
                "GL":"Greenland",
                "GD":"Grenada",
                "GP":"Guadeloupe",
                "GU":"Guam",
                "GT":"Guatemala",
                "GG":"Guernsey",
                "GN":"Guinea",
                "GW":"Guinea-Bissau",
                "GY":"Guyana",
                "HT":"Haiti",
                "HM":"Heard Island and McDonald Islands",
                "VA":"Holy See (Vatican City State)",
                "HN":"Honduras",
                "HK":"Hong Kong", #
                "HU":"Hungary",
                "IS":"Iceland",
                "IN":"India",
                "ID":"Indonesia",
                "IR":"Iran, Islamic Republic of",
                "IQ":"Iraq",
                "IE":"Ireland",
                "IM":"Isle of Man",
                "IL":"Israel",
                "IT":"Italy",
                "JM":"Jamaica",
                "JP":"Japan",
                "JE":"Jersey",
                "JO":"Jordan",
                "KZ":"Kazakhstan",
                "KE":"Kenya",
                "KI":"Kiribati",
                "KP":"Korea, Democratic People's Republic of",
                "KR":"Korea, Republic of",
                "KW":"Kuwait",
                "KG":"Kyrgyzstan",
                "LA":"Lao People's Democratic Republic",
                "LV":"Latvia",
                "LB":"Lebanon",
                "LS":"Lesotho",
                "LR":"Liberia",
                "LY":"Libya",
                "LI":"Liechtenstein",
                "LT":"Lithuania",
                "LU":"Luxembourg",
                "MO":"Macao",
                "MK":"Macedonia, Republic of",
                "MG":"Madagascar",
                "MW":"Malawi",
                "MY":"Malaysia",
                "MV":"Maldives",
                "ML":"Mali",
                "MT":"Malta",
                "MH":"Marshall Islands",
                "MQ":"Martinique",
                "MR":"Mauritania",
                "MU":"Mauritius",
                "YT":"Mayotte",
                "MX":"Mexico",
                "FM":"Micronesia, Federated States of",
                "MD":"Moldova, Republic of",
                "MC":"Monaco",
                "MN":"Mongolia",
                "ME":"Montenegro",
                "MS":"Montserrat",
                "MA":"Morocco",
                "MZ":"Mozambique",
                "MM":"Myanmar",
                "NA":"Namibia",
                "NR":"Nauru",
                "NP":"Nepal",
                "NL":"Netherlands",
                "NC":"New Caledonia",
                "NZ":"New Zealand",
                "NI":"Nicaragua",
                "NE":"Niger",
                "NG":"Nigeria",
                "NU":"Niue",
                "NF":"Norfolk Island",
                "MP":"Northern Mariana Islands",
                "NO":"Norway",
                "OM":"Oman",
                "PK":"Pakistan",
                "PW":"Palau",
                "PS":"Palestinian Territory, Occupied",
                "PA":"Panama",
                "PG":"Papua New Guinea",
                "PY":"Paraguay",
                "PE":"Peru",
                "PH":"Philippines",
                "PN":"Pitcairn",
                "PL":"Poland",
                "PT":"Portugal",
                "PR":"Puerto Rico",
                "QA":"Qatar",
                "RE":"Reunion",
                "RO":"Romania",
                "RU":"Russian Federation",
                "RW":"Rwanda",
                "BL":"Saint Barthelemy",
                "SH":"Saint Helena, Ascension and Tristan da Cunha",
                "KN":"Saint Kitts and Nevis",
                "LC":"Saint Lucia",
                "MF":"Saint Martin (French part)",
                "PM":"Saint Pierre and Miquelon",
                "VC":"Saint Vincent and the Grenadines",
                "WS":"Samoa",
                "SM":"San Marino",
                "ST":"Sao Tome and Principe",
                "SA":"Saudi Arabia",
                "SN":"Senegal",
                "RS":"Serbia",
                "SC":"Seychelles",
                "SL":"Sierra Leone",
                "SG":"Singapore",
                "SX":"Sint Maarten (Dutch part)",
                "SK":"Slovakia",
                "SI":"Slovenia",
                "SB":"Solomon Islands",
                "SO":"Somalia",
                "ZA":"South Africa",
                "GS":"South Georgia and the South Sandwich Islands",
                "ES":"Spain",
                "LK":"Sri Lanka",
                "SD":"Sudan",
                "SR":"Suriname",
                "SS":"South Sudan",
                "SJ":"Svalbard and Jan Mayen",
                "SZ":"Swaziland",
                "SE":"Sweden",
                "CH":"Switzerland",
                "SY":"Syrian Arab Republic",
                "TW":"Taiwan, Province of China",
                "TJ":"Tajikistan",
                "TZ":"Tanzania, United Republic of",
                "TH":"Thailand",
                "TL":"Timor-Leste",
                "TG":"Togo",
                "TK":"Tokelau",
                "TO":"Tonga",
                "TT":"Trinidad and Tobago",
                "TN":"Tunisia",
                "TR":"Turkey",
                "TM":"Turkmenistan",
                "TC":"Turks and Caicos Islands",
                "TV":"Tuvalu",
                "UG":"Uganda",
                "UA":"Ukraine",
                "AE":"United Arab Emirates",
                "GB":"United Kingdom",
                "US":"United States",
                "UM":"United States Minor Outlying Islands",
                "UY":"Uruguay",
                "UZ":"Uzbekistan",
                "VU":"Vanuatu",
                "VE":"Venezuela, Bolivarian Republic of",
                "VN":"Viet Nam",
                "VG":"Virgin Islands, British",
                "VI":"Virgin Islands, U.S.",
                "WF":"Wallis and Futuna",
                "YE":"Yemen",
                "ZM":"Zambia",
                "ZW":"Zimbabwe"}



all_countries_2L = {
    "Andorra": "AD",
    "United Arab Emirates": "AE",
    "Afghanistan": "AF",
    "Antigua and Barbuda": "AG",
    "Anguilla": "AI",
    "Albania": "AL",
    "Armenia": "AM",
    "Angola": "AO",
    "Antarctica": "AQ",
    "Argentina": "AR",
    "American Samoa": "AS",
    "Austria": "AT",
    "Australia": "AU",
    "Aruba": "AW",
    "Aland Islands": "AX",
    "Azerbaijan": "AZ",
    "Bosnia and Herzegovina": "BA",
    "Barbados": "BB",
    "Bangladesh": "BD",
    "Belgium": "BE",
    "Burkina Faso": "BF",
    "Bulgaria": "BG",
    "Bahrain": "BH",
    "Burundi": "BI",
    "Benin": "BJ",
    "Saint Barthelemy": "BL",
    "Bermuda": "BM",
    "Brunei Darussalam": "BN",
    "Bolivia (Plurinational State of)": "BO",
    "Bonaire, Sint Eustatius and Saba": "BQ",
    "Brazil": "BR",
    "Bahamas": "BS",
    "Bhutan": "BT",
    "Bouvet Island": "BV",
    "Botswana": "BW",
    "Belarus": "BY",
    "Belize": "BZ",
    "Canada": "CA",
    "Cocos (Keeling) Islands": "CC",
    "Congo, Democratic Republic of the": "CD",
    "Central African Republic": "CF",
    "Congo": "CG",
    "Switzerland": "CH",
    "Cote d'Ivoire": "CI",
    "Cook Islands": "CK",
    "Chile": "CL",
    "Cameroon": "CM",
    "China": "CN",
    "Colombia": "CO",
    "Costa Rica": "CR",
    "Cuba": "CU",
    "Cabo Verde": "CV",
    "Curacao": "CW",
    "Christmas Island": "CX",
    "Cyprus": "CY",
    "Czechia": "CZ",
    "Germany": "DE",
    "Djibouti": "DJ",
    "Denmark": "DK",
    "Dominica": "DM",
    "Dominican Republic": "DO",
    "Algeria": "DZ",
    "Ecuador": "EC",
    "Estonia": "EE",
    "Egypt": "EG",
    "Western Sahara": "EH",
    "Eritrea": "ER",
    "Spain": "ES",
    "Ethiopia": "ET",
    "Finland": "FI",
    "Fiji": "FJ",
    "Falkland Islands (Malvinas)": "FK",
    "Micronesia (Federated States of)": "FM",
    "Faroe Islands": "FO",
    "France": "FR",
    "Gabon": "GA",
    "United Kingdom of Great Britain and Northern Ireland": "GB",
    "Grenada": "GD",
    "Georgia": "GE",
    "French Guiana": "GF",
    "Guernsey": "GG",
    "Ghana": "GH",
    "Gibraltar": "GI",
    "Greenland": "GL",
    "Gambia": "GM",
    "Guinea": "GN",
    "Guadeloupe": "GP",
    "Equatorial Guinea": "GQ",
    "Greece": "GR",
    "South Georgia and the South Sandwich Islands": "GS",
    "Guatemala": "GT",
    "Guam": "GU",
    "Guinea-Bissau": "GW",
    "Guyana": "GY",
    "Hong Kong": "HK",
    "Heard Island and McDonald Islands": "HM",
    "Honduras": "HN",
    "Croatia": "HR",
    "Haiti": "HT",
    "Hungary": "HU",
    "Indonesia": "ID",
    "Ireland": "IE",
    "Israel": "IL",
    "Isle of Man": "IM",
    "India": "IN",
    "British Indian Ocean Territory": "IO",
    "Iraq": "IQ",
    "Iran (Islamic Republic of)": "IR",
    "Iceland": "IS",
    "Italy": "IT",
    "Jersey": "JE",
    "Jamaica": "JM",
    "Jordan": "JO",
    "Japan": "JP",
    "Kenya": "KE",
    "Kyrgyzstan": "KG",
    "Cambodia": "KH",
    "Kiribati": "KI",
    "Comoros": "KM",
    "Saint Kitts and Nevis": "KN",
    "Korea (Democratic People's Republic of)": "KP",
    "Korea, Republic of": "KR",
    "Kuwait": "KW",
    "Cayman Islands": "KY",
    "Kazakhstan": "KZ",
    "Lao People's Democratic Republic": "LA",
    "Lebanon": "LB",
    "Saint Lucia": "LC",
    "Liechtenstein": "LI",
    "Sri Lanka": "LK",
    "Liberia": "LR",
    "Lesotho": "LS",
    "Lithuania": "LT",
    "Luxembourg": "LU",
    "Latvia": "LV",
    "Libya": "LY",
    "Morocco": "MA",
    "Monaco": "MC",
    "Moldova, Republic of": "MD",
    "Montenegro": "ME",
    "Saint Martin (French part)": "MF",
    "Madagascar": "MG",
    "Marshall Islands": "MH",
    "North Macedonia": "MK",
    "Mali": "ML",
    "Myanmar": "MM",
    "Mongolia": "MN",
    "Macao": "MO",
    "Northern Mariana Islands": "MP",
    "Martinique": "MQ",
    "Mauritania": "MR",
    "Montserrat": "MS",
    "Malta": "MT",
    "Mauritius": "MU",
    "Maldives": "MV",
    "Malawi": "MW",
    "Mexico": "MX",
    "Malaysia": "MY",
    "Mozambique": "MZ",
    "Namibia": "NA",
    "New Caledonia": "NC",
    "Niger": "NE",
    "Norfolk Island": "NF",
    "Nigeria": "NG",
    "Nicaragua": "NI",
    "Netherlands": "NL",
    "Norway": "NO",
    "Nepal": "NP",
    "Nauru": "NR",
    "Niue": "NU",
    "New Zealand": "NZ",
    "Oman": "OM",
    "Panama": "PA",
    "Peru": "PE",
    "French Polynesia": "PF",
    "Papua New Guinea": "PG",
    "Philippines": "PH",
    "Pakistan": "PK",
    "Poland": "PL",
    "Saint Pierre and Miquelon": "PM",
    "Pitcairn": "PN",
    "Puerto Rico": "PR",
    "Palestine, State of": "PS",
    "Portugal": "PT",
    "Palau": "PW",
    "Paraguay": "PY",
    "Qatar": "QA",
    "Reunion": "RE",
    "Romania": "RO",
    "Serbia": "RS",
    "Russian Federation": "RU",
    "Rwanda": "RW",
    "Saudi Arabia": "SA",
    "Solomon Islands": "SB",
    "Seychelles": "SC",
    "Sudan": "SD",
    "Sweden": "SE",
    "Singapore": "SG",
    "Saint Helena, Ascension and Tristan da Cunha": "SH",
    "Slovenia": "SI",
    "Svalbard and Jan Mayen": "SJ",
    "Slovakia": "SK",
    "Sierra Leone": "SL",
    "San Marino": "SM",
    "Senegal": "SN",
    "Somalia": "SO",
    "Suriname": "SR",
    "South Sudan": "SS",
    "Sao Tome and Principe": "ST",
    "El Salvador": "SV",
    "Sint Maarten (Dutch part)": "SX",
    "Syrian Arab Republic": "SY",
    "Eswatini": "SZ",
    "Turks and Caicos Islands": "TC",
    "Chad": "TD",
    "French Southern Territories": "TF",
    "Togo": "TG",
    "Thailand": "TH",
    "Tajikistan": "TJ",
    "Tokelau": "TK",
    "Timor-Leste": "TL",
    "Turkmenistan": "TM",
    "Tunisia": "TN",
    "Tonga": "TO",
    "Turkey": "TR",
    "Trinidad and Tobago": "TT",
    "Tuvalu": "TV",
    "Taiwan, Province of China": "TW",
    "Tanzania, United Republic of": "TZ",
    "Ukraine": "UA",
    "Uganda": "UG",
    "United States Minor Outlying Islands": "UM",
    "United States of America": "US",
    "Uruguay": "UY",
    "Uzbekistan": "UZ",
    "Holy See": "VA",
    "Saint Vincent and the Grenadines": "VC",
    "Venezuela (Bolivarian Republic of)": "VE",
    "Virgin Islands (British)": "VG",
    "Virgin Islands (U.S.)": "VI",
    "Viet Nam": "VN",
    "Vanuatu": "VU",
    "Wallis and Futuna": "WF",
    "Samoa": "WS",
    "Yemen": "YE",
    "Mayotte": "YT",
    "South Africa": "ZA",
    "Zambia": "ZM",
    "Zimbabwe": "ZW",
}
    
all_countries_2LISO = dict(map(reversed, all_countries_2L.items()))
