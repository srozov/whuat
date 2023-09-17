question_id = null
var requestFlag = true
async function fetchQuestion() {
    try {
        const response = await fetch('/get_random_question/');
        const data = await response.json();

        
        if (data.new_url) {
            window.location.href = data.new_url;
            return; 
        }

        document.getElementById('question').innerText = data.question.question_text
        document.getElementById('choice1').innerText = data.answers.A
        document.getElementById('choice2').innerText = data.answers.B
        document.getElementById('choice3').innerText = data.answers.C
        document.getElementById('choice4').innerText = data.answers.D

        question_id = data.question.id

    } catch (error) {
        console.error('Error fetching health data:', error);
    }
}

fetchQuestion()


function sendResponse(question, choice) {
    if (requestFlag){
    requestFlag = false
    var UPLOAD_URL = "/submit_selected_answer/"; // Your URL endpoint

    var data = {
        question: question,
        choice: choice
    };

    var jsonString = JSON.stringify(data);

    var xhr = new XMLHttpRequest();
    xhr.open("POST", UPLOAD_URL, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.setRequestHeader("X-CSRFTOKEN", CSRF_TOKEN);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            requestFlag = true
        }
    };
    xhr.send(jsonString);
    fetchQuestion()
}
}

// Function to generate fading string at (x, y) relative to the image
function generateFadingString(x, y, textMessage) {
    var imgElement = document.getElementById("egg_svg");
    var fadingStringElement = document.createElement("div");
    fadingStringElement.classList.add("fading-string");
    fadingStringElement.textContent = textMessage;

    // Position it
    fadingStringElement.style.left = x + "px";
    fadingStringElement.style.top = y + "px";

    imgElement.parentElement.appendChild(fadingStringElement);

    // Trigger animation
    setTimeout(function() {
        fadingStringElement.style.opacity = 0;
        fadingStringElement.style.transform = "translateY(-50px)";
    }, 100);

    // Remove element after animation is complete
    setTimeout(function() {
        fadingStringElement.remove();
    }, 2100);
}

// Attach an event listener for when the window is loaded
window.addEventListener("load", function() {
    // Generate a fading string at (50, 50) relative to the image
    var height = 50;
    var i = 0;
    var a = setInterval(() => {
        if (i % 2 === 0) {
            generateFadingString(220, 70);
        }
        if (i % 2 === 1) {
            generateFadingString(230, 70);
        }
        i++;
        if (i === 10) {
            clearInterval(a);
        }
    }, 700);
});

function getRandomCoordinate(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

document.getElementById('choice1').addEventListener('click', function() {
    sendResponse(question = question_id, choice = "A");
    const x = getRandomCoordinate(190, 220);
    const y = getRandomCoordinate(30, 80);
    generateFadingString(x, y, '+1');
});

document.getElementById('choice2').addEventListener('click', function () {
    sendResponse(question = question_id, choice = "B");
    const x = getRandomCoordinate(190, 220);
    const y = getRandomCoordinate(30, 80);
    generateFadingString(x, y, '+1');
});

document.getElementById('choice3').addEventListener('click', function () {
    sendResponse(question = question_id, choice = "C");
    const x = getRandomCoordinate(190, 220);
    const y = getRandomCoordinate(30, 80);
    generateFadingString(x, y, '+1');
});

document.getElementById('choice4').addEventListener('click', function () {
    sendResponse(question = question_id, choice = "D");
    const x = getRandomCoordinate(190, 220);
    const y = getRandomCoordinate(30, 80);
    generateFadingString(x, y, '+1');
});
