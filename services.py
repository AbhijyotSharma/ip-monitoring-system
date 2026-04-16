import requests

def get_ip_info(ip):
    try:
        url = f"https://ipinfo.io/{ip}/json"
        response = requests.get(url, timeout=5)
        data = response.json()

        return {
            "status": "success",
            "ip": ip,
            "country": data.get("country"),
            "city": data.get("city"),
            "isp": data.get("org"),
            "region": data.get("region"),
            "timezone": data.get("timezone")
        }

    except Exception as e:
        print("🔥 ERROR:", e)
        return {
            "status": "fail",
            "message": "Server error"
        }