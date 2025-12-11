let player = {
    name: "",
    country: "",
    lives: 5
};

// ✈️ Airplane animation
function playAirplaneAnimation() {
    const plane = document.getElementById("airplane-animation");
    plane.classList.remove("hidden");
    plane.classList.remove("fly");
    void plane.offsetWidth; 
    plane.classList.add("fly");

    setTimeout(() => {
        plane.classList.add("hidden");
    }, 2500);
}

// 🎯 Start game using Flask API
async function startGame() {
    const name = document.getElementById("player_name").value;
    const country = document.getElementById("country").value;

    if (!name || !country) {
        alert("Syötä nimi ja valitse maa.");
        return;
    }

    const response = await fetch("/api/start", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name: name, country: country })
    });

    const data = await response.json();

    // Show game screen
    document.getElementById("start-screen").style.display = "none";
    document.getElementById("game-screen").style.display = "block";

    // Player basic info
    document.getElementById("player-info").innerText = "Pelaaja: " + data.player;
    document.getElementById("lives-info").innerText = "Elämät: " + data.lives;

    // 🌍 Airport information from SQL
    if (data.airport) {
        document.getElementById("airport-info").innerText =
            `Saapunut lentokentälle: ${data.airport.airport} (${data.airport.code})`;
    } else {
        document.getElementById("airport-info").innerText =
            "Lentokenttää ei löytynyt tälle maalle.";
    }

    // Story text
    document.getElementById("story-box").innerText = data.story;

    // Play animation
    playAirplaneAnimation();
}

function resetGame() {
    document.getElementById("start-screen").style.display = "block";
    document.getElementById("game-screen").style.display = "none";
    document.getElementById("player_name").value = "";
    document.getElementById("country").value = "";
}
