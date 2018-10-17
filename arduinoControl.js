openMask = () => {
	$.post("/MASK=OPEN", function(data, status){
        alert("Data: " + data + "\nStatus: " + status);
    });
}

closeMask = () => {
    $.post("/MASK=CLOSED", function(data, status){
        alert("Data: " + data + "\nStatus: " + status);
    });
}
