$( document ).ready(function() {
    var windowsize = $(window).width();
//    if (windowsize <= 1200) {
        $('.my_data_col').addClass('my_row');
//    }
});

$(window).resize(function() {
  $('.my_data_col').removeClass('my_row');
  windowsize = $(window).width();
  if (windowsize <= 1200) {
      $('.my_data_col').addClass('my_row');
  }
});


$(function() {
    $.scrollify({
        section : ".my_row",
        interstitialSection : "",
		easing: "easeOutExpo",
		scrollSpeed: 1100,
		offset : 0,
		scrollbars: true,
		standardScrollElements: "",
		setHeights: true,
		overflowScroll: true,
		updateHash: true,
		touchScroll:true,
		before:function() {},
		after:function() {},
		afterResize:function() {},
		afterRender:function() {}

    });
});
