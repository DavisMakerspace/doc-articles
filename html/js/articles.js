$(document).ready(function() {
    var counter_h3 = 0;
    var counter_h4 = 0;
    var counter_h5 = 0;

    $('h3, h4, h5').each(function() {
        if ( $(this).prop('tagName') == 'H3' )
        {
            counter_h3 += 1;
            counter_h4  = 0;
            counter_h5  = 0;

	    this.label = "ARTICLE " + counter_h3;

            $(this).before("<div class='index bold'>" + this.label + "</div>");
        }

        if ( $(this).prop('tagName') == 'H4' )
        {
            counter_h4 += 1;
            counter_h5  = 0;

	    this.label = "Section " + counter_h3 + "." + counter_h4;

            $(this).before("<div class='index'>" + this.label + "</div>");
        }

        if ( $(this).prop('tagName') == 'H5' )
        {
            counter_h5 += 1;

	    this.label = counter_h3 + "." + counter_h4 + "." + counter_h5;

            $(this).before("<div class='index padded'>" + this.label + "</div>");
        }
    });

    $('a').each(function() {
	var target = $(this).attr('href');
	var label  = $(target)[0].label;

	$(this).html(label);
    });
})
