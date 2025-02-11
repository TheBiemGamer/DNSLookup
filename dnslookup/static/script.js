document.body.classList.add("dark-theme");

async function fetchDNS() {
  const domain = document.getElementById("domain").value.trim();
  const recordType = document.getElementById("recordType").value;
  const resultDiv = document.getElementById("result");
  const loadingDiv = document.getElementById("loading");

  resultDiv.innerHTML = "";
  resultDiv.classList.remove("show");
  loadingDiv.classList.add("active");

  if (!domain) {
    resultDiv.innerHTML = '<p class="error">Please enter a domain name.</p>';
    resultDiv.classList.add("show");
    loadingDiv.classList.remove("active");
    return;
  }

  try {
    const response = await fetch(`/lookup?domain=${domain}&type=${recordType}`);
    const data = await response.json();

    if (response.ok) {
      let html = `<div class="record-type">${data.record_type} Records for ${data.domain}:</div>`;
      data.records.forEach((record) => {
        html += `<div class="record-item">${record}</div>`;
      });
      resultDiv.innerHTML = html;
    } else {
      resultDiv.innerHTML = `<p class="error">${
        data.error || "An error occurred."
      }</p>`;
    }
  } catch (error) {
    resultDiv.innerHTML =
      '<p class="error">Failed to fetch DNS records. Please try again.</p>';
  } finally {
    loadingDiv.classList.remove("active");
    setTimeout(() => {
      resultDiv.classList.add("show");
    }, 100);
  }
}

document
  .getElementById("domain")
  .addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
      fetchDNS();
    }
  });

function toggleTheme() {
  const body = document.body;
  if (body.classList.contains("dark-theme")) {
    body.classList.remove("dark-theme");
    body.classList.add("light-theme");
  } else {
    body.classList.remove("light-theme");
    body.classList.add("dark-theme");
  }
}
