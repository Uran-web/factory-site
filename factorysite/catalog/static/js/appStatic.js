$(function() {
   
    /* Fixed header */
    
    let header = $("#header");
    let title = $("#title");
    let titleH = title.height();
    let scrollPos = $(window).scrollTop();
    let nav = $("#nav");
    let navToggle = $("#navToggle");
    
    checkScroll(scrollPos, titleH);
    
    $(window).on("scroll", function() {
        titleH = title.height();
        scrollPos = $(this).scrollTop();
        
        checkScroll(scrollPos, titleH);
    });
    
    function checkScroll(scrollPos, titleH) {
        
        if( scrollPos > titleH ) {
            header.addClass("fixed resize");
        } else {
            header.removeClass("fixed");
        }
    }
    
    /* Smooth scroll */
    
    $("[data-scroll]").on("click", function(event) {
        event.preventDefault();
        
        let elementId = $(this).data('scroll');
        let elementOffset = $(elementId).offset().top;
        
        nav.removeClass("show");
        
        $("html, body").animate({
           scrollTop: elementOffset - 65
        }, 700);
    });
    
    
    /* Toggle */
    
    navToggle.on("click", function(event) {
        event.preventDefault();
        
        
        nav.toggleClass("show");
    });
    
    
    /* Reviews https://kenwheeler.github.io/slick/*/
    
    let slider = $("#reviewsSlider");
    
    slider.slick({
        infinite: true,
        fade: true,
        dots: true,
        arrows: false
    });
    
    let slider1 = $("#galarySlider");
    
    slider1.slick({
        infinite: true,
        fade: true,
        arrows: true
    });
    
});