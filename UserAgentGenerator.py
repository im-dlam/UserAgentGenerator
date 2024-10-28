import random
from typing import List
import logging
from colorlog import ColoredFormatter




class UserAgentGenerator:
    def __init__(self):
        # Khởi tạo các thuộc tính với dữ liệu cần thiết
        self.app_version = f'FBAV/4{random.randint(86,90)}.0.0.{random.randint(40,60)}.{random.randint(70,80)}'  # Phiên bản ứng dụng cố định
        self.build_version = f'FBBV/65{random.randint(7006653,8006653)}'   # Phiên bản build cố định
        self.languages = ['en_US', 'en_GB']
        self.carriers = [
             'Verizon', 'O2', 'Vinaphone', 'Sprint', 'EE'
        ]
        self.device_models = self.device_models = {
            'samsung': [
                'SM-G988B', 'SM-G988U', 'SM-G988W', 'SM-G988F', 'SM-G988N', 'SM-S908N', 'SM-S901N', 'SM-S906N', 'SM-G977N', 'SM-G973N', 'SM-G975N', 'SM-N976N','SM-A725F', 'SM-A525F', 'SM-A325F','SM-G996B', 'SM-G991B', 'SM-F926B',
                'SM-G996U', 'SM-G991U', 'SM-A425U','SM-A325U', 'SM-A135F', 'SM-M127F','SM-M225F', 'SM-G780G', 'SM-G778B','SM-A037F', 'SM-S901B', 'SM-G570F','SM-J260F', 'SM-J415F', 'SM-A705F',
                'SM-G973F', 'SM-G975F', 'SM-G960F','SM-G965F', 'SM-N960F', 'SM-A600FN','SM-A705N', 'SM-A516B', 'SM-A610F','SM-A715F', 'SM-S9070', 'SM-G532F','SM-J530F', 'SM-J600FN', 'SM-G925F',
                'SM-G930F', 'SM-G935F', 'SM-G950F','SM-G955F', 'SM-N950F', 'SM-A320FL','SM-G850F', 'SM-G930W8', 'SM-N950W','SM-G928W8', 'SM-G850Y', 'SM-J530Y','SM-A720F', 'SM-J810F', 'SM-A310F',
                'SM-F711B', 'SM-G996E', 'SM-G998B','SM-G998U', 'SM-S908E', 'SM-S908F','SM-A534U', 'SM-A536E', 'SM-M826F','SM-G9650', 'SM-G9500', 'SM-G9960','SM-G981B', 'SM-G990E', 'SM-G780F',
                'SM-A825F', 'SM-F926B', 'SM-M506B','SM-A115F', 'SM-G9960', 'SM-G9980','SM-G9100', 'SM-G9208', 'SM-G9008','SM-G8910', 'SM-G955N', 'SM-G8500','SM-G9860', 'SM-G9280', 'SM-G9198',
                'SM-G9608', 'SM-G9288', 'SM-N9608','SM-N970F', 'SM-S908W', 'SM-N985F','SM-G9910', 'SM-A507FN', 'SM-S510E','SM-M325F', 'SM-G9880', 'SM-G9300','SM-A5070', 'SM-J727V', 'SM-J737P',
                'SM-N975U', 'SM-N975N', 'SM-G9550'
            ],

                'OPPO': [
                    'CPH2401', 'CPH2307', 'CPH2173','CPH2025', 'PFEM10', 'PEEM00', 'PEEM10', 'PENM00', 'PFJM10', 'PHJM10', 'PFPM00', 'CPH1923', 'CPH1937', 'CPH2197', 'CPH2185', 'CPH2183','CPH2195', 'CPH2015', 'CPH2119', 
                    'CPH2055', 'CPH2045', 'CPH1901', 'CPH1911', 'CPH1983', 'CPH1823','CPH1719', 'CPH1871', 'CPH1853','CPH1831', 'CPH1833', 'CPH1617','CPH1865', 'CPH1893', 'CPH1981','CPH2201', 'CPH2217', 'CPH2301','CPH2361', 'CPH2399', 'CPH2435',
                    'CPH2453', 'CPH2471', 'CPH2475','CPH2481', 'CPH2573', 'CPH2579','CPH2601', 'CPH2603', 'CPH2647','CPH2745', 'CPH2751', 'CPH2805','CPH2847', 'CPH2901', 'CPH2903',
                    'CPH2905', 'CPH2907', 'CPH2909','CPH2913', 'CPH2915', 'CPH2917','CPH1941', 'CPH2021', 'CPH1955','CPH2035', 'CPH2037', 'CPH2133','CPH2151', 'CPH2153', 'CPH2155',
                    'CPH2157', 'CPH2175', 'CPH2177','CPH2205', 'CPH2209', 'CPH2215','CPH2231', 'CPH2245', 'CPH2247','CPH2251', 'CPH2255', 'CPH2275','CPH2277', 'CPH2295', 'CPH2299','CPH2305', 'CPH2309', 'CPH2311',
                    'CPH2321', 'CPH2325', 'CPH2331','CPH2335', 'CPH2337', 'CPH2351','CPH2367', 'CPH2371', 'CPH2381','CPH2395', 'CPH2403', 'CPH2411','CPH2415', 'CPH2421', 'CPH2425',
                    'CPH2431', 'CPH2433', 'CPH2445','CPH2451', 'CPH2461', 'CPH2473','CPH2485', 'CPH2495', 'CPH2501','CPH2513', 'CPH2521', 'CPH2531'
                ],

                'Xiaomi': [
                    '23049RAD8C', '2210132C', '2210132G', '2107113SG', '2201122C', '2112123AC', '2109119DG', 'M2102K1AC', 'M2011J18C', 'M2007J3SC', 'M2007J1SC', 'M2103K19C', 
                    'M2103K16I', 'M2102J20SG', 'M2101K9C', 'M2011K2C', 'M2012K11AC', 'M2012K11C', 'M2102K20C', 'M2102K20I', 'M2102K20A', 'M2101K9A', 'M2101K9B', 'M2101K9D', 
                    'M2101K9E', 'M2101K9F', 'M2011J18F','M2102K2C', 'M2102K3A', 'M2102K3B', 'M2102K4C', 'M2102K5C', 'M2103K1C', 'M2103K1D', 'M2103K1E', 'M2103K1F', 'M2103K2A', 'M2103K2B', 'M2103K2C', 
                    'M2103K2D', 'M2103K2E', 'M2103K2F', 'M2103K2G', 'M2103K2H', 'M2103K3A', 'M2103K3B', 'M2103K3C', 'M2103K3D', 'M2103K3E', 'M2103K3F', 'M2103K3G', 'M2103K3H', 'M2103K4A', 'M2103K4B', 
                    'M2103K4C', 'M2103K4D', 'M2103K5A', 'M2103K5B', 'M2103K5C', 'M2103K5D', 'M2103K5E', 'M2103K5F', 'M2103K5G', 'M2103K5H', 'M2103K6A', 'M2103K6B', 'M2103K6C', 'M2103K6D', 'M2103K6E',
                    'M2103K6F', 'M2103K7A', 'M2103K7B', 'M2103K7C', 'M2103K7D', 'M2103K7E', 'M2103K7F', 'M2103K8A', 'M2103K8B', 'M2103K8C', 'M2103K8D', 'M2103K8E', 'M2103K8F', 'M2103K9A', 'M2103K9B', 
                    'M2103K9C', 'M2103K9D', 'M2103K9E', 'M2103K9F', 'M2103K10A', 'M2103K10B', 'M2103K10C', 'M2103K10D', 'M2103K10E'
                ]
            }


        self.android_versions = [f'FBSV/{version}' for version in ['11', '12', '13','9','10']]
        self.optimization_profiles = [f'FBOP/{i}' for i in range(1, 5)]
        self.manufacturer = random.choice(['samsung','OPPO','Xiaomi'])
        self.brand = self.manufacturer.lower() if self.manufacturer == 'Xiaomi' else self.manufacturer


    def generate_display_metrics(self) -> str:
        """Generate random display metrics."""
        density = round(random.uniform(2.0, 4), 1)  # Density between 2.0 and 3.5
        screen_sizes = {
            'Xiaomi': [
                {'width': 1080, 'height': 2400},  # Xiaomi Mi 11, Redmi Note 10
                {'width': 1080, 'height': 2340},  # Xiaomi Mi 9, Redmi Note 8
                {'width': 1440, 'height': 3200},  # Xiaomi Mi 11 Ultra
                {'width': 720,  'height': 1520},  # Redmi 7A
                {'width': 1080, 'height': 2160}   # Xiaomi Mi Mix 2
            ],
            'OPPO': [
                {'width': 1080, 'height': 2400},  # Oppo Find X3 Pro
                {'width': 1080, 'height': 2340},  # Oppo Reno 5
                {'width': 720,  'height': 1600},  # Oppo A53
                {'width': 1440, 'height': 3168},  # Oppo Find X2 Pro
                {'width': 1080, 'height': 1920}   # Oppo R9s
            ],
            'samsung': [
                {'width': 1440, 'height': 3200},  # Samsung Galaxy S21 Ultra
                {'width': 1080, 'height': 2400},  # Samsung Galaxy A72
                {'width': 720,  'height': 1600},  # Samsung Galaxy A12
                {'width': 1440, 'height': 2960},  # Samsung Galaxy S9+
                {'width': 1080, 'height': 2280}   # Samsung Galaxy A50
            ]
        }

        screen_choice = random.choice(screen_sizes[self.manufacturer])
        width = screen_choice['width']
        height = screen_choice['height']
        return f'density={density},width={width},height={height}'

    def generate_user_agent(self) -> str:
        """Generate a random user-agent string."""
        user_agent_components = {
            "FBAN": "FB4A",
            "FBAV": self.app_version,
            "FBBV": self.build_version,
            "FBDM": f"{{{self.generate_display_metrics()}}}",
            "FBLC": random.choice(self.languages),
            "FBRV": "0",
            "FBCR": random.choice(self.carriers),
            "FBMF": self.manufacturer,
            "FBBD": self.brand,
            "FBPN": "com.facebook.katana",
            "FBDV": random.choice(self.device_models[self.manufacturer]),
            "FBSV": random.choice(self.android_versions),
            "FBOP": random.choice(self.optimization_profiles),
            "FBCA": "x84_64;arm64-v8a"
        }

        user_agent = ";".join(f"{key}/{value}" for key, value in user_agent_components.items())
        return f"[{user_agent}]"


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Formatter for colored console output
colored_formatter = ColoredFormatter(
    "%(log_color)s%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    log_colors={
        "DEBUG": "cyan",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "bold_red",
    },
)

# Console handler with colored formatter
console_handler = logging.StreamHandler()
console_handler.setFormatter(colored_formatter)
logger.addHandler(console_handler)

# File handler for critical errors only
file_handler = logging.FileHandler("errors.log")
file_handler.setLevel(logging.CRITICAL)
file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
