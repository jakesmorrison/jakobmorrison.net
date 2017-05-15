$(document).ready(function(){
	// Init ScrollMagic
	var controller = new ScrollMagic.Controller();

	// build a scene
	var ourScene = new ScrollMagic.Scene({
		triggerElement: '#project01',
		duration: "100%",
		triggerHook: .5,
		reverese: false
	})
	.setClassToggle('#project01', 'fade-in') // add class to project01
    .addIndicators({
		name: 'fade scene',
		colorTrigger: 'black',
		indent: 200,
		colorStart: '#75C695'
	})
    .addTo(controller);

//    var $word = $("path#korea0");
//    var tween = new TimelineMax()
//		.add(TweenMax.to($word, 0.9, {strokeDashoffset: 0, ease:Linear.easeNone})) // draw word for 0.9
//
//   //build a scene2
//	var ourScene2 = new ScrollMagic.Scene({
//		triggerElement: '#korea-svg',
//		duration: "200",
//		triggerHook: .5,
//		reverese: false
//	})
//    .setTween(tween)
//    .addIndicators({
//		name: 'fade scene',
//		colorTrigger: 'black',
//		indent: 200,
//		colorStart: '#75C695'
//	})
//    .addTo(controller);
})