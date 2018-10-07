function getWit() {
    let audioFile = $('#audioFile')[0].files[0];
    console.log(audioFile)

    let req = new XMLHttpRequest();
    req.onload = e => {
        console.log(e)
    }

    req.open("POST", "https://api.wit.ai/speech");

    let reader = new FileReader();
    reader.onload = file => {
        console.log('loaded', file)
        req.send(file);
    }

    reader.readAsDataURL(audioFile);

//    $.ajax({
//      url: 'https://api.wit.ai/speech',
//      type: 'POST',
////      dataType: 'jsonp',
//      data: audioFile,
//      headers: {
//        'X-Requested-With': 'JSONHttpRequest',
//        'Authorization': 'Bearer DKZUYDUTBR3Z5XN6XR4VB2ORKLH7TJDT',
//        'Content-Type': 'audio/mpeg3'
//      },
//      success: function(response) {
//        console.log(response);
//      },
//    });
}

//function getWit() {
//    $.ajax({
//      url: 'https://api.wit.ai/message',
//      data: {
//        'q': 'close mask',
//        'access_token': 'DKZUYDUTBR3Z5XN6XR4VB2ORKLH7TJDT',
//      },
//      dataType: 'jsonp',
//      method: 'GET',
//      headers: {
//        'X-Requested-With': 'JSONHttpRequest',
//        'Content-Type': 'audio/mpeg3'
//      },
//      success: function(response) {
//        console.log(response);
//      },
//    });
//}

//function getWit() {
//    $.ajax({
//      url: 'https://api.wit.ai/speech',
//      data: {
//        'q': 'set an alarm in 10min',
//        'access_token' : 'DKZUYDUTBR3Z5XN6XR4VB2ORKLH7TJDT'
//      },
//      dataType: 'jsonp',
//      method: 'POST',
//      success: function(response) {
//          console.log("success!", response);
//      },
//
//    });
//
//}
