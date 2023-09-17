function start_max_multiplier() {
    document.getElementById('egg_svg').style.display = 'block'
    const choices = document.querySelectorAll('.choice');
    
    // Loop through each element and add the "rainbow-background" class
    choices.forEach(function (choice) {
        choice.classList.add('rainbow-background');
    });

    var imgElement = document.getElementsByClassName('image-container')[0];

    // Array of emojis
    const emojis = ["🎉", "🎊", "💃", "🕺", "🎈", "🥳", "🎵", "🎶", "🍻", "🍷", "🍸", "🍹", "🍾", "🍰", "🧁", "🎺", "🎸", "🥁", "🎆", "🎇"];

    // Function to generate fading emojis at (x, y) relative to the image
    function generateFadingString(x, y) {
        var fadingStringElement = document.createElement("div");
        fadingStringElement.classList.add("fading-string");
        fadingStringElement.textContent = emojis[Math.floor(Math.random() * emojis.length)];

        // Position it
        fadingStringElement.style.left = x + "px";
        fadingStringElement.style.top = y + "px";

        imgElement.parentElement.appendChild(fadingStringElement);

        // Trigger animation
        setTimeout(function () {
            fadingStringElement.style.opacity = 0;
            fadingStringElement.style.transform = "translateY(-50px)";
        }, 100);

        // Remove element after animation is complete
        setTimeout(function () {
            fadingStringElement.remove();
        }, 2100);
    }

    let i = 0;

    const intervalId = setInterval(() => {
        // Generate random x and y positions within a 300x300 area
        const x = Math.floor(Math.random() * 300);
        const y = Math.floor(Math.random() * 300);

        generateFadingString(x, y);
        i++;

        if (i >= 809) {
            clearInterval(intervalId);
        }
    }, 30);
}



function start_cracking_multiplier() {
    document.getElementById('orange_egg_svg').style.display = 'block';
    const choices = document.querySelectorAll('.choice');
    
    // Loop through each element and add the "orange-background" class
    choices.forEach(function (choice) {
        choice.classList.add('orange-background');
    });
    
    var imgElement = document.getElementsByClassName('image-container')[0];
    
    // Array of emojis
    const emojis = ["🏠", "🛒", "🦄", "🇨🇭", "🍎", "🍫", "☕", "🥖", "🍦", "🌱", "🐖", "🐟", "🐶", "👶", "🙋"];
    
    
    
    // Function to generate fading emojis at (x, y) relative to the image
    function generateFadingString(x, y) {
        var fadingStringElement = document.createElement("div");
        fadingStringElement.classList.add("fading-string");
        fadingStringElement.textContent = emojis[Math.floor(Math.random() * emojis.length)];
    
        // Position it
        fadingStringElement.style.left = x + "px";
        fadingStringElement.style.top = y + "px";
    
        imgElement.parentElement.appendChild(fadingStringElement);
    
        // Trigger animation
        setTimeout(function () {
            fadingStringElement.style.opacity = 0;
            fadingStringElement.style.transform = "translateY(-50px)";
        }, 100);
    
        // Remove element after animation is complete
        setTimeout(function () {
            fadingStringElement.remove();
        }, 2100);
    }
    
    let i = 0;
    
    const intervalId = setInterval(() => {
        // Generate random x and y positions within a 300x300 area
        const x = Math.floor(Math.random() * 300);
        const y = Math.floor(Math.random() * 300);
    
        generateFadingString(x, y);
        i++;
    
        if (i >= 809) {
            clearInterval(intervalId);
        }
    }, 30);    
}