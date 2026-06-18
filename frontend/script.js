const tbody = document.querySelector("#device-table tbody");
const refreshButton = document.querySelector("#refresh-button");
const countdownEl = document.querySelector("#refresh-countdown");
const spinner = document.querySelector("#spinner");
const detailsPanel = document.querySelector("#details-panel");
const nmapOutput = document.querySelector("#nmap-output");
const closeDetailsBtn = document.querySelector("#close-details");

let nextRefresh = 300;
let countdownTimer;

async function loadDevices() {
  try {
    const res = await fetch("http://127.0.0.1:5000");
    if (!res.ok) throw new Error("Erreur réseau");
    const devices = await res.json();
    tbody.innerHTML = devices.map(deviceRow).join("");
  } catch (err) {
    tbody.innerHTML = `<tr><td colspan="4">Erreur : ${err.message}</td></tr>`;
  }
}

function deviceRow(device) {
  return `
    <tr>
      <td>${device.mac}</td>
      <td>${device.ip}</td>
      <td>${device.vendor}</td>
      <td><button class="action-btn nmap-btn" data-ip="${device.ip}">+</button></td>
    </tr>
  `;
}

async function scanWithNmap(ip) {
  spinner.classList.remove("hidden");
  detailsPanel.classList.remove("hidden");
  nmapOutput.textContent = "Scanning en cours...";
  
  try {
    const res = await fetch(`http://127.0.0.1:5000/nmap/${ip}`);
    if (!res.ok) throw new Error("Erreur serveur");
    const data = await res.json();
    console.log(data);
    nmapOutput.textContent = data.output || data.error || "Aucun résultat";
  } catch (err) {
    nmapOutput.textContent = `Erreur: ${err.message}`;
  } finally {
    spinner.classList.add("hidden");
  }
}

function updateCountdown() {
  countdownEl.textContent = `Prochain refresh dans ${nextRefresh}s`;
  nextRefresh = Math.max(0, nextRefresh - 1);
}

function resetCountdown() {
  nextRefresh = 300;
  updateCountdown();
  if (countdownTimer) {
    clearInterval(countdownTimer);
  }
  countdownTimer = setInterval(updateCountdown, 1000);
}

refreshButton.addEventListener("click", () => {
  loadDevices();
  resetCountdown();
});

closeDetailsBtn.addEventListener("click", () => {
  detailsPanel.classList.add("hidden");
});

document.addEventListener("click", (e) => {
  if (e.target.classList.contains("nmap-btn")) {
    const ip = e.target.dataset.ip;
    scanWithNmap(ip);
  }
});

loadDevices();
resetCountdown();
setInterval(() => {
  loadDevices();
  resetCountdown();
}, 300000);