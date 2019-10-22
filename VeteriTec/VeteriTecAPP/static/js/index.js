$(document).on("click", 'a[href*="#"]', function(e) {

    var target = $(this).attr("href"); //Get the target
    var scrollToPosition = $(target).offset().top - 60;

    $('html,body').animate({ 'scrollTop': scrollToPosition }, 600, function(){
       window.location.hash = target;
    });

    e.preventDefault();
});
