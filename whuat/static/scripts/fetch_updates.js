function update(health, users){
    active_user_count = document.getElementById("active-users")
    active_user_count.innerText = users
    health_state = document.getElementById('percentage').value;
    health_state.value = health
}

async function fetchHealthData() {
    try {
        const response = await fetch('/update');
        const data = await response.json();
        
        update(data.health, data.users)
    } catch (error) {
        console.error('Error fetching health data:', error);
    }
}

// Fetch health data every 3 seconds
setInterval(fetchHealthData, 3000);
