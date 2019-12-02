$(document).ready(function(){
  //for when DOM is ready

  // Smooth scrolling
  var $root = $('html, body');
  $('.navbar-nav a').click(function() {
    var href = $.attr(this, 'href');
    if (href != undefined && href != '#') {
      $root.animate({
        scrollTop: $(href).offset().top
      }, 500, function () {
        window.location.hash = href;
      });
    }
    return false;
  });

  //tooltip
  $(function () {
    $('#item1').tooltip();
    $('[data-toggle="tooltip"]').tooltip();
  });

});// end doc.ready function
