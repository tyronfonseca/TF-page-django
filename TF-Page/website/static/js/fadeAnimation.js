$(document).ready(function(){
			var content = $('#content');
			content.css("display","none");
			content.slideDown(1000);
			$('a.transition').click(function(e){
				e.preventDefault();
				var image = $('#backgroundImg');
				if(image != null){
					image.fadeOut(300);
				}
				linkLocation = this.href;
				content.slideUp(500,redirectPage);
			});

			function redirectPage(){
				window.location = linkLocation;
			}
		});