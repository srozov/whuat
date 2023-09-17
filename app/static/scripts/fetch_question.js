question_id = null

async function fetchQuestion() {
    try {
        // because someone didn't want to have state in the FE we have to fetch it before everytime, great!
        const state_response = await fetch('/state/');
        const state_data = await state_response.json();
        if (state_data.health > 0.0) {

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
        }
        else {
            console.log('Redirecting to /results/');
            window.location.href = '/results/'; // Redirect the user to /results/
        }

    } catch (error) {
        console.error('Error fetching health data:', error);
    }
}

fetchQuestion()

async function shouldRedirectAsync () {

    const state_response = await fetch('/state/');
    const state_data = await state_response.json();

    if (state_data.health > 0.0) {
        return false
    }
    else {
        return true
    }


}

async function sendResponse(question, choice) {
    var UPLOAD_URL = "/submit_selected_answer/"; // Your URL endpoint

    var data = {
        question: question,
        choice: choice
    };

    const state_response = await fetch('/state/');
    const state_data = await state_response.json();
    if (state_data.health > 0.0) {

        var jsonString = JSON.stringify(data);
        var xhr = new XMLHttpRequest();
        xhr.open("POST", UPLOAD_URL, true);
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.setRequestHeader("X-CSRFTOKEN", CSRF_TOKEN);
        xhr.onreadystatechange = function () {
            if (xhr.readyState == 4 && xhr.status == 200) {
                console.log('succesfully submited')
            }
        };
        xhr.send(jsonString);
        fetchQuestion()
    }
        else {
        console.log('Redirecting to /results/');
        window.location.href = '/results/'; // Redirect the user to /results/
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

// choiceButton1 = document.getElementById('choice1');
// choiceButton1.addEventListener('click', function() {
//     choiceButton1.disabled = true;
//     sendResponse(question_id, "A")
//         .then(() => {
//             console.log('A')
//             const x = getRandomCoordinate(190, 220);
//             const y = getRandomCoordinate(30, 80);
//             generateFadingString(x, y, '+1');
//         })
//         .catch((error) => {
//             console.error('Error:', error);
//         })
//         .finally(() => {
//             // Re-enable the button after the operation is complete
//             choiceButton1.disabled = false;
//         });
// });

choiceButton1 = document.getElementById('choice1');
choiceButton1.addEventListener('click', async function() {
    // Enable the button to allow other actions
    choiceButton1.disabled = false;

    try {
        // Call the async method to determine whether to redirect
        const shouldRedirect = await shouldRedirectAsync();

        if (shouldRedirect) {
            // Disable the button again right before redirection
            choiceButton1.disabled = true;
            // Redirect the user to /results/
            window.location.href = '/results/';
        } else {
            // Continue with other actions if needed
            await sendResponse(question_id, "A");
            const x = getRandomCoordinate(190, 220);
            const y = getRandomCoordinate(30, 80);
            generateFadingString(x, y, '+1');
        }
    } catch (error) {
        console.error('Error:', error);
    }
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
