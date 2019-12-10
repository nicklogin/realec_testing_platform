// var deleteElem = function(elem_id) {
//     var elem = document.getElementById(elem_id);
//     elem.parentNode.removeChild(elem);
// };

// var deleteQuestion = function(question_id) {
//     alert("Delete Question "+question_id+"?");
// };

// var deleteAnswer = function(answer_id, question_id) {
//     alert("Delete Answer "+answer_id+" to Question "+question_id+"?");
// };

var currAddedAnswerId = -1;

//taken from https://stackoverflow.com/questions/4793604/how-to-insert-an-element-after-another-element-in-javascript-without-using-a-lib :
var insertAfter = function(newNode, referenceNode) {
    referenceNode.parentNode.insertBefore(newNode, referenceNode.nextSibling);
}

var addAnswer = function(last, question_id) {
    newAnswer = document.createElement("TEXTAREA");
    newAnswer.name = "answer_"+question_id+"_"+currAddedAnswerId;
    newAnswer.id = question_id+"_"+currAddedAnswerId;
    newAnswer.cols = 80;
    newAnswer.rows = 3;
    currAddedAnswerId -= 1;
    //insert linebreak before textarea:
    linebreak = document.createElement("br");
    insertAfter(linebreak, last)
    //insert textarea:
    insertAfter(newAnswer, linebreak);
    //set nicEditor instance on the textarea:
    editor = new nicEditor().panelInstance(newAnswer.id);
    // add <br /> before Delete checkbox and :
    linebreak = document.createElement("br");
    insertAfter(linebreak, newAnswer);
    //sets label div for Delete checkbox:
    label = document.createElement("label");
    insertAfter(label, linebreak);
    //add Delete checkbox:
    deletebox = document.createElement("input");
    deletebox.type = "checkbox";
    deletebox.name = "delete_" + newAnswer.id;
    label.appendChild(deletebox);
    //sets text span for deleteCheckbox label:
    textSpan = document.createElement("span");
    textSpan.innerText = "Delete answer from question";
    label.appendChild(textSpan)
    //add space after Delete checkbox:
    space = document.createTextNode(" ")
    insertAfter(space, label);
    //add "Restore to default" button:
    restoreButton = document.createElement("button");
    restoreButton.type = "button";
    restoreButton.innerText = "Restore to default";
    insertAfter(restoreButton, space);
    //add br to the end of the answer area:
    // linebreak = document.createElement("br");
    // insertAfter(linebreak, restoreButton);
};

var submitEditingForm = function() {
    $('textarea').each(function () {
        var id_nic = $(this).attr('id');
        var nic = new nicEditors.findEditor(id_nic);
        var newContent = nic.getContent()
        document.getElementById(id_nic).value = newContent;
    });
    document.getElementById("editForm").submit();
};

var restoreQuestion = function(question_id) {
    console.log(question_id);
    question = document.getElementById(question_id);
    nic = new nicEditors.findEditor("question_"+question_id);
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.status == 200) {
            nic.setContent(this.responseText);
        };
    };
    xhttp.open("GET", "?question_id="+question_id, true);
    xhttp.send();
};

var restoreAnswer = function(restoreButton) {
    answer_id = restoreButton.id.slice(8);
    answer = document.getElementById(answer_id);
    nic = new nicEditors.findEditor(answer_id);
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.status == 200) {
            nic.setContent(this.responseText);
        };
    };
    answer_id = answer_id.split("_")[1];
    xhttp.open("GET", "?answer_id="+answer_id, true);
    xhttp.send();
};

var changeNumQuest = function() {
    numSelector = document.getElementById("QuestionCount");
    window.location.replace(window.location.href.split('?')[0]+"?max_q="+numSelector.value)
};

var toBottom = function() {
    window.scrollTo(0,document.body.scrollHeight);
}

var toTop = function() {
    window.scrollTo(0,0);
}