
async function predict() {
    const cgpa = Number(document.getElementById("cgpa").value);

    const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ cgpa: cgpa })
    });

    const data = await response.json();

    document.getElementById("result").innerText =
        "Predicted score: " + data.prediction;
}