question_id = null

async function fetchQuestion() {
    try {
        const response = await fetch('/get_random_question');
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
            console.log('succesfully submited')
        }
    };
    xhr.send(jsonString);
    fetchQuestion()
}

document.getElementById('choice1').addEventListener('click', function () {
    sendResponse(
        question = question_id,
        choice = "A"
    )
})
document.getElementById('choice2').addEventListener('click', function () {
    sendResponse(
        question = question_id,
        choice = "B"
    )
})
document.getElementById('choice3').addEventListener('click', function () {
    sendResponse(
        question = question_id,
        choice = "C"
    )
})
document.getElementById('choice4').addEventListener('click', function () {
    sendResponse(
        question = question_id,
        choice = "D"
    )
})