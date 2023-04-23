class PlaceAgent:
    prefecture: str
    longitude: float # 緯度(-90~90)
    latitude: float # 経度(-180~180)

    def __init__(self) -> None:
        self.prefecture = "Kanagawa"
        self.longitude = 35.524680
        self.latitude = 139.649080