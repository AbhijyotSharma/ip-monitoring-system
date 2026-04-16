function lookupIP() {
    const ip = document.getElementById("ip").value;

    fetch('/lookup', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ ip: ip })
    })
    .then(response => {
        console.log("Raw response:", response);
        return response.json();
    })
    .then(data => {
        console.log("Data:", data);

        const resultDiv = document.getElementById("result");

        if (data.status === "fail") {
            resultDiv.innerHTML = "❌ " + data.message;
        } else {
            resultDiv.innerHTML = `
                <p><b>IP:</b> ${data.ip}</p>
                <p><b>Country:</b> ${data.country}</p>
                <p><b>City:</b> ${data.city}</p>
                <p><b>ISP:</b> ${data.isp}</p>
                <p><b>Region:</b> ${data.region}</p>
                <p><b>Timezone:</b> ${data.timezone}</p>
            `;
        }
    })
    .catch(error => {
        console.error("Fetch error:", error);
        document.getElementById("result").innerHTML = "❌ Server error";
    });
}
