async function fetchEvents() {
  const res = await fetch("/events");
  const data = await res.json();
  const list = document.getElementById("eventList");
  list.innerHTML = "";
  data.forEach((event) => {
    const li = document.createElement("li");
    li.textContent = event.msg;
    list.appendChild(li);
  });
}

// Poll every 15 seconds
fetchEvents();
setInterval(fetchEvents, 15000);
