import random
from typing import List

class UserAgentGenerator:
    def __init__(self):
        # Khởi tạo các thuộc tính với dữ liệu cần thiết
        self.app_version = 'FBAV/486.0.0.55.70'  # Phiên bản ứng dụng cố định
        self.build_version = 'FBBV/652720741'   # Phiên bản build cố định
        self.languages = ['vi_VN', 'en_US', 'en_GB']
        self.carriers = [
            'Viettel', 'Verizon', 'O2', 'MobiFone', 
            'T-Mobile', 'Vinaphone', 'Sprint', 'EE'
        ]
        self.device_models = [
            'SM-G988B', 'SM-G988U', 'SM-G988W', 
            'SM-G988F', 'SM-G988N', 'SM-S908N'
            'SM-S901N','SM-S906N','SM-G977N',
            'SM-G973N','SM-G975N','SM-N976N',
        ]
        self.android_versions = [f'FBSV/{version}' for version in ['11', '12', '13']]
        self.optimization_profiles = [f'FBOP/{i}' for i in range(1, 4)]
        self.manufacturer = 'samsung'
        self.brand = 'samsung'

    @staticmethod
    def generate_display_metrics() -> str:
        """Generate random display metrics."""
        density = round(random.uniform(2.0, 3.5), 1)  # Density between 2.0 and 3.5
        width = random.choice([1080, 1440, 2400, 720])      # Common screen widths
        height = random.choice([2340, 3200, 3040 , 1208])      # Common screen heights
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
            "FBDV": random.choice(self.device_models),
            "FBSV": random.choice(self.android_versions),
            "FBOP": random.choice(self.optimization_profiles),
            "FBCA": "arm64-v8a"
        }

        user_agent = ";".join(f"{key}/{value}" for key, value in user_agent_components.items())
        return f"[{user_agent}]"

