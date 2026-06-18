const tbody = document.querySelector("#device-table tbody");
const refreshButton = document.querySelector("#refresh-button");
const countdownEl = document.querySelector("#refresh-countdown");

let nextRefresh = 60;
let countdownTimer;

async function loadDevices() {
  try {
    const res = await fetch("http://127.0.0.1:5000");
    if (!res.ok) throw new Error("Erreur réseau");
    const devices = await res.json();
    tbody.innerHTML = devices.map(deviceRow).join("");
  } catch (err) {
    tbody.innerHTML = `<tr><td colspan="3">Erreur : ${err.message}</td></tr>`;
  }
}

function deviceRow(device) {
  return `
    <tr>
      <td>${device.mac}</td>
      <td>${device.ip}</td>
      <td>${device.vendor}</td>
    </tr>
  `;
}

function updateCountdown() {
  countdownEl.textContent = `Prochain refresh dans ${nextRefresh}s`;
  nextRefresh = Math.max(0, nextRefresh - 1);
}

function resetCountdown() {
  nextRefresh = 60;
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

loadDevices();
resetCountdown();
setInterval(() => {
  loadDevices();
  resetCountdown();
}, 60000);