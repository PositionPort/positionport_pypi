import requests

class PositionPortClient:
    def __init__(self, public_key: str, secret_key: str):
        self.base_url = "http://91.99.68.226:8001/external"
        self.public_key = public_key
        self.secret_key = secret_key 

    def _auth_headers(self):
        return {
            "X-API-KEY": self.public_key,
            "X-API-SECRET": self.secret_key
        }

    def start_binance_tracking(self, seed: float | None = None):
        params = {}
        if seed is not None and float(seed) > 0:
            params["seed"] = float(seed)
        res = requests.get(
            f"{self.base_url}/binance/start-tracking",
            headers=self._auth_headers(),
            params=params or None,
            timeout=60,
        )
        res.raise_for_status()
        return res.json()

    def stop_binance_tracking(self, *, discard_empty: bool = True):
        res = requests.get(
            f"{self.base_url}/binance/stop-tracking",
            headers=self._auth_headers(),
            params={"discard_empty": "true" if discard_empty else "false"},
        )
        res.raise_for_status()
        return res.json()

    def start_bybit_tracking(self, seed: float | None = None):
        params = {}
        if seed is not None and float(seed) > 0:
            params["seed"] = float(seed)
        res = requests.get(
            f"{self.base_url}/bybit/start-tracking",
            headers=self._auth_headers(),
            params=params or None,
            timeout=60,
        )
        res.raise_for_status()
        return res.json()

    def stop_bybit_tracking(self, *, discard_empty: bool = True):
        res = requests.get(
            f"{self.base_url}/bybit/stop-tracking",
            headers=self._auth_headers(),
            params={"discard_empty": "true" if discard_empty else "false"},
            timeout=60,
        )
        res.raise_for_status()
        return res.json()
