let count = 2;
$("#send_btn").on("click", function(ev) {
    // add this to catch the submit event.
    ev.preventDefault();
    ev.stopPropagation();
    $("#send").after(`
    <div class="recv_message">
    <span id="userId1">user1:</span>
    <pre class="messageBox_left">messages1</pre>
    </div>`);

})