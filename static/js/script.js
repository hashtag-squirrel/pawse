document.addEventListener("DOMContentLoaded", function () {
    setTimeout(function () {
        let messages = document.getElementById('msg');
        if (messages === null) {
            return
        }
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }, 3000);
});