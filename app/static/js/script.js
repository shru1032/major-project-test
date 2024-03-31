document.querySelector('form').addEventListener('submit', function(e) {
    e.preventDefault();
    var file = document.querySelector('input[type="file"]').files[0];
    var reader = new FileReader();
    reader.onloadend = function() {
        var base64 = reader.result.replace(/^data:image\/(png|jpg);base64,/, "");
        fetch('/predict', {
            method: 'POST',
            body: JSON.stringify({file: base64}),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(response => response.json())
        .then(data => {
            document.getElementById('result').innerHTML = `Prediction: ${data.classification}<br>Accuracy: ${data.accuracy}`;
        });
    };
    reader.readAsDataURL(file);
});
