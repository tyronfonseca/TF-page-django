var body = $('body');		
	var image = $('#backgroundImg');
	var tmp = 'nulo';
	  $('.work').mouseover(function(e) {
			e.preventDefault();
			var img = this.getAttribute('data-img');
		    var color = this.getAttribute('data-color');
		    if(tmp != img){
		    	tmp = img;
		    	image.fadeOut(300, function () {
			        image.css("background-image", "url(img/"+img+".png)");
			        image.fadeIn(400);
			    });
		    	body.css("background-color", color);
		    }			
});

$(document).ready(function() {
	var movementStrength = 25;
	var height = movementStrength / $(window).height();
	var width = movementStrength / $(window).width();
	$("#backgroundImg").mousemove(function(e){
	          var pageX = e.pageX - ($(window).width() / 2);
	          var pageY = e.pageY - ($(window).height() / 2);
	          var newvalueX = width * pageX * -1 - 25;
	          var newvalueY = height * pageY * -1 - 50;
	          $('#backgroundImg').css("background-position", newvalueX+"px     "+newvalueY+"px");
	});
});