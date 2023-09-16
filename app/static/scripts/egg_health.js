const slider = document.getElementById('slider');
  const percentageInput = document.getElementById('percentage');

  const scalePercentage = (percent) => {
    return 24 + (76 - 24) * (percent / 100);
  };

  const setWidth = (newX) => {
    const rect = slider.parentElement.getBoundingClientRect();
    let newWidth = newX - rect.left;

    newWidth = Math.max(rect.width * 0.24, Math.min(newWidth, rect.width * 0.76));
    const percent = ((newWidth / rect.width) - 0.24) / (0.76 - 0.24) * 100;

    document.querySelector('.after-img').style.width = newWidth + 'px';
    slider.style.left = newWidth + 'px';
    percentageInput.value = Math.round(percent);
  };

  slider.addEventListener('mousedown', (e) => {
    e.preventDefault();
    document.addEventListener('mousemove', onMouseMove);
    document.addEventListener('mouseup', onMouseUp);
  });

  function onMouseMove(e) {
    setWidth(e.clientX);
  }

  function onMouseUp() {
    document.removeEventListener('mousemove', onMouseMove);
    document.removeEventListener('mouseup', onMouseUp);
  }

  percentageInput.addEventListener('input', () => {
    const rect = slider.parentElement.getBoundingClientRect();
    const newWidth = rect.width * (scalePercentage(percentageInput.value) / 100);
    setWidth(rect.left + newWidth);
  });