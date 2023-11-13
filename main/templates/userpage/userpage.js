document.getElementById('submit_btn').addEventListener('click', function(event) {


    var userquestion = document.getElementById('question_text').value;
    var response = document.getElementById('response-container');

    response.innerHTML += '<p> 질문 내용: '+ userquestion + '</p>';
    event.preventDefault();
});