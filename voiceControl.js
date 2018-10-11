sendVoiceCommand = () => {
    let audioFile = $('#audioFile')[0].files[0];
    let formData = new FormData();
    formData.append('speech', audioFile);

    let request = new XMLHttpRequest();
    request.addEventListener('load', handleVoiceCommand);
    request.open('POST', 'http://127.0.0.1:5000/voice', true);
    request.send(formData);
}

handleVoiceCommand = res => {
    switch(res) {
        case 'open_mask':
            openMask();
            break;
        case 'close_mask':
            closeMask()
            break;
    }
}
