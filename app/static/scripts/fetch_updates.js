let currentHealth = 0; // Current health value (starts at 0)
let currentUsers = 0; // Current users value (starts at 0)

function update(health, users) {
    // Update active users by counting
    const active_user_count = document.getElementById("active-users");
    countFromTo(currentUsers, users, (value) => {
        active_user_count.innerText = value;
    });
    currentUsers = users; // Update the current users value

    // Update health by counting
    const health_state = document.getElementById('percentage');
    countFromTo(currentHealth, health, (value) => {
        health_state.value = value;
    });
    currentHealth = health; // Update the current health value
}

// Function to count from one value to another and update UI
function countFromTo(start, end, updateUI) {
    const step = start < end ? 1 : -1; // Determine the direction to count in
    let currentValue = start;

    function updateValue() {
        if ((step > 0 && currentValue <= end) || (step < 0 && currentValue >= end)) {
            updateUI(currentValue);
            currentValue += step;
            requestAnimationFrame(updateValue); // Use requestAnimationFrame for smoother transitions
        }
    }

    updateValue();
}

async function fetchHealthData() {
    try {
        const response = await fetch('/state');
        const data = await response.json();
        
        update(data.health, data.users);

        if (data.active_multiplier == 'MAX-CRACKING COMMUNITY MULTIPLIER'){
            start_max_multiplier()
        }
        else if (data.active_multiplier ==  'cracking multiplier') {
            start_cracking_multiplier()
        }

    } catch (error) {
        console.error('Error fetching health data:', error);
    }
}

setInterval(fetchHealthData, 1500);

