! function(e) {
    function o(e, o) {
        l++, d = l / c, TweenLite.to(u, .7, {
            progress: d,
            ease: Linear.easeNone
        })
    }

    function t() {
        d = Math.round(100 * u.progress()), e(".txt-perc").text(d + "%")
    }

    function a() {
        var o = new TimelineMax;
        return o.to(e(".txt-perc"), .3, {
            y: 100,
            autoAlpha: 0,
            ease: Back.easeIn
        }, .1).set(e("body"), {
            className: "-=is-loading"
        }).set(e("#intro"), {
            className: "+=is-loaded"
        }).to(e("#preloader"), .7, {
            yPercent: 100,
            ease: Power4.easeInOut
        }).set(e("#preloader"), {
            className: "+=is-hidden"
        }).from(e("#intro .title"), 1, {
            autoAlpha: 0,
            ease: Power1.easeOut
        }, "-=0.2").from(e("#intro p"), .7, {
            autoAlpha: 0,
            ease: Power1.easeOut
        }, "+=0.2")
    }
    var s = new ScrollMagic.Controller,
        r = ["#slide02","#slide03"],
        n = ["#slide02 header", "#slide03 header"],
        l = 0,
        c = e(".bcg").length,
        d = 0;
    e(".bcg").imagesLoaded({
        background: !0
    }).progress(function(e, t) {
        o()
    });
    var u = new TimelineMax({
        paused: !0,
        onUpdate: t,
        onComplete: a
    });
    if (u.to(e(".progress span"), 1, {
            width: 100,
            ease: Linear.easeNone
        }), !Modernizr.touch) {
        n.forEach(function(e, o) {
            {
                var t = o + 1;
                new ScrollMagic.Scene({
                    triggerElement: e,
                    offset: -95
                }).setClassToggle("#slide0" + t, "is-active").addTo(s)
            }
        }), r.forEach(function(o, t) {
            new ScrollMagic.Scene({
                triggerElement: o
            }).on("enter", function(o) {
                e("nav").removeAttr("class")
            }).addTo(s)
        }), r.forEach(function(o, t) {
            {
                var a = e(o).find(".bcg");
                new ScrollMagic.Scene({
                    triggerElement: o,
                    triggerHook: 1,
                    duration: "100%"
                }).setTween(TweenMax.from(a, 1, {
                    y: "-40%",
                    autoAlpha: .3,
                    ease: Power0.easeNone
                })).addTo(s)
            }
        });
        var w = new TimelineMax;

        w.to(e("#slide02 h1"), .2, {
            autoAlpha: 0,
            ease: Power1.easeNone
        }, 1.5).to(e("#slide02 section"), .2, {
            autoAlpha: 0,
            ease: Power1.easeNone
        }, 1.5)
        .set(e("#slide02 h1"), {
            text: "Some Text",
            src: "text"
        })
        .set(e("#slide02 p"), {
            text: "more text",
        })
        .to(e("#slide02 .bcg"), .6, {
            scale: 2,
            transformOrigin: "0% 0%",
            ease: Power0.easeNone
        })
        .fromTo(e("#slide02 h1"), .7, {
            y: "+=20"
        }, {
            y: 0,
            autoAlpha: 1,
            ease: Power1.easeOut
        }, "+=0.4")
        .fromTo(e("#slide02 section"), .6, {
            y: "+=20"
        }, {
            y: 0,
            autoAlpha: 1,
            ease: Power1.easeOut
        }, "-=0.6")
        .set(e("#slide02 h1"), {
            autoAlpha: 1
        }, "+=2.5")
        .fromTo(e("#slide02 h1"), .7, {
        }, {
            autoAlpha: 0,
            ease: Power1.easeNone
        }, "+=2.5")
        .fromTo(e("#slide02 section"), .6, {
        }, {
            autoAlpha: 0,
            ease: Power1.easeNone
        }, "+=0.4")
        .to(e("#slide02 .bcg"), .6, {
            scale: 1,
            transformOrigin: "0% 0%",
            ease: Power0.easeNone
        })
        .set(e("#slide02 h1"), {
            text: "More Text",
        })
        .set(e("#slide02 p"), {
            text: "text text"
        })
        .to(e("#slide02 .bcg"), .6, {
            scale:2,
            transformOrigin: "120% 20%",
            ease: Power0.easeNone
        })
        .fromTo(e("#slide02 h1"), .7, {
            y: "+=0"
        }, {
            y: 0,
            autoAlpha: 1,
            ease: Power1.easeOut
        }, "+=0.4").
        fromTo(e("#slide02 section"), .6, {
            y: "+=0"
        }, {
            y: 0,
            autoAlpha: 1,
            ease: Power1.easeOut
        }, "-=0.6");

        {
            new ScrollMagic.Scene({
                triggerElement: "#slide02",
                triggerHook: 0,
                duration: "400%"
            }).setPin("#slide02").setTween(w).addTo(s);
        }

        s.scrollTo(function(e) {
            TweenMax.to(window, 1, {
                scrollTo: {
                    y: e
                },
                ease: Power1.easeInOut
            })
        }), e(document).on("click", "a[href^='#']", function(o) {
            var t = e(this).attr("href");
            e(t).length > 0 && (o.preventDefault(), s.scrollTo(t), window.history && window.history.pushState && history.pushState("", document.title, t))
        })
    }
}(jQuery);