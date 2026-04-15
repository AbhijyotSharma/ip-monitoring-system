import requests

def get_ip_info(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        data = response.json()

        if data['status'] == 'fail':
            return {"status": "fail", "message": "Invalid IP"}

        return {
            "status": "success",
            "ip": data.get("query"),
            "country": data.get("country"),
            "city": data.get("city"),
            "isp": data.get("isp"),
            "region": data.get("regionName"),
            "timezone": data.get("timezone")
        }

    except Exception:
        return {"status": "fail", "message": "Server error"}
