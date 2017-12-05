 $( document ).ready(function() {
    console.log( "ready!" );
});
    function ajaxCall() {
        $.ajax({
            url: "http://127.0.0.1:5000/star",
            datatype: 'json',
            cache: false,
            success: function (data) {
            var result = $('<div />').append(data).find('#showresults').html();
            $('#showresults').html(result);
        }})
    }
    setInterval(ajaxCall, 5000);
